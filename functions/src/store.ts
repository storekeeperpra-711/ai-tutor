/**
 * Everything the AI functions read and write in Firestore, behind an
 * interface so the logic can be tested with an in-memory fake.
 *
 * Layout (only the server can read or write these, except where noted):
 * ```
 * accounts/{uid}/students/{sid}              (written by the app)
 * accounts/{uid}/students/{sid}/reports/{week}  weekly report (the app reads it)
 * ai_usage/{day}_{sid}     uid, student_id, day, calls, text, photo, steps, tokens, cost_usd
 * ai_usage_total/{day}     calls, cost_usd: the project's daily cap
 * ai_logs/{auto}           every call, for review; expires after 90 days
 * ai_queue/{id}            answers that waited offline (the app creates and reads them)
 * ai_batches/{batchId}     batches sent to the Batch API
 * ```
 */
import { FieldValue, Firestore, Timestamp } from "firebase-admin/firestore";

import { LOG_DAYS } from "./config";
import type { TokenUsage } from "./pricing";

export type Kind = "text" | "photo";

export interface Reservation {
  uid: string;
  studentId: string;
  day: string;
  kind: Kind;
  /** `{lessonId}/{stepId}`, for the per-step limit. */
  stepKey: string;
  kindLimit: number;
  stepLimit: number;
  globalDailyUsd: number;
}

export type ReserveResult = "ok" | "student_limit" | "step_limit" | "budget";

export interface UsageRecord {
  uid: string;
  studentId: string;
  day: string;
  calls: number;
  usage: TokenUsage;
  costUsd: number;
}

export interface LogEntry {
  uid: string;
  student_id: string;
  prompt_id: string;
  lesson_id: string;
  step_id: string;
  lang: string;
  input: string;
  output: unknown;
  model: string | null;
  checked_by: "ai" | "fallback";
  reason: string | null;
  concern: boolean;
  cost_usd: number;
  batch: boolean;
}

export interface QueuedAnswer {
  id: string;
  uid: string;
  student_id: string;
  lesson_id: string;
  step_id: string;
  lang: string;
  answer: string;
  created_at: Date;
}

export interface QueueResult {
  level: string;
  reply: string;
}

export interface BatchInfo {
  id: string;
  /** custom_id -> what it is for. */
  items: Record<string, { kind: "answer" | "report"; uid: string; student_id: string; week?: string; stats?: unknown }>;
}

export interface UsageRow {
  day: string;
  uid: string;
  student_id: string;
  calls: number;
  text: number;
  photo: number;
  cost_usd: number;
}

export interface StudentRef {
  uid: string;
  studentId: string;
  grade: number;
}

export interface Store {
  studentExists(uid: string, studentId: string): Promise<boolean>;
  /** Checks every limit and, if none is reached, counts this call. */
  reserve(r: Reservation): Promise<ReserveResult>;
  /** Gives back a reservation when the call failed (not the student's fault). */
  release(r: Reservation): Promise<void>;
  /** Adds tokens and cost to the student's day and the project's day. */
  recordUsage(record: UsageRecord): Promise<void>;
  log(entry: LogEntry): Promise<void>;
  /** The whole project's estimated cost on [day]. */
  projectCost(day: string): Promise<number>;

  waitingAnswers(limit: number): Promise<QueuedAnswer[]>;
  markQueued(ids: string[], status: "in_batch" | "skipped", batchId?: string): Promise<void>;
  answerQueued(id: string, result: QueueResult | null): Promise<void>;
  saveBatch(batch: BatchInfo): Promise<void>;
  openBatches(): Promise<BatchInfo[]>;
  closeBatch(id: string): Promise<void>;

  saveReport(uid: string, studentId: string, week: string, stats: unknown, note: unknown): Promise<void>;
  allStudents(): Promise<StudentRef[]>;
  /** The student's progress and skill documents (as stored by the app). */
  studentActivity(uid: string, studentId: string): Promise<{ progress: Record<string, unknown>[]; skills: Record<string, unknown>[] }>;

  studentsOf(uid: string): Promise<string[]>;
  usageFor(days: string[], students: { uid: string; studentId: string }[] | "all"): Promise<UsageRow[]>;
}

const usageId = (day: string, studentId: string) => `${day}_${studentId}`;

export class FirestoreStore implements Store {
  constructor(private readonly db: Firestore) {}

  private student(uid: string, studentId: string) {
    return this.db.collection("accounts").doc(uid).collection("students").doc(studentId);
  }

  async studentExists(uid: string, studentId: string): Promise<boolean> {
    return (await this.student(uid, studentId).get()).exists;
  }

  reserve(r: Reservation): Promise<ReserveResult> {
    const usageRef = this.db.collection("ai_usage").doc(usageId(r.day, r.studentId));
    const totalRef = this.db.collection("ai_usage_total").doc(r.day);
    return this.db.runTransaction(async (tx) => {
      const [usage, total] = await Promise.all([tx.get(usageRef), tx.get(totalRef)]);
      if ((total.get("cost_usd") ?? 0) >= r.globalDailyUsd) return "budget";
      if ((usage.get(r.kind) ?? 0) >= r.kindLimit) return "student_limit";
      const steps = (usage.get("steps") ?? {}) as Record<string, number>;
      if ((steps[r.stepKey] ?? 0) >= r.stepLimit) return "step_limit";
      tx.set(
        usageRef,
        {
          uid: r.uid,
          student_id: r.studentId,
          day: r.day,
          [r.kind]: FieldValue.increment(1),
          steps: { [r.stepKey]: FieldValue.increment(1) },
        },
        { merge: true },
      );
      return "ok";
    });
  }

  async release(r: Reservation): Promise<void> {
    await this.db
      .collection("ai_usage")
      .doc(usageId(r.day, r.studentId))
      .set(
        { [r.kind]: FieldValue.increment(-1), steps: { [r.stepKey]: FieldValue.increment(-1) } },
        { merge: true },
      );
  }

  async recordUsage(rec: UsageRecord): Promise<void> {
    const add = {
      calls: FieldValue.increment(rec.calls),
      input_tokens: FieldValue.increment(rec.usage.input_tokens),
      output_tokens: FieldValue.increment(rec.usage.output_tokens),
      cache_read_tokens: FieldValue.increment(rec.usage.cache_read_input_tokens ?? 0),
      cost_usd: FieldValue.increment(rec.costUsd),
    };
    const batch = this.db.batch();
    batch.set(
      this.db.collection("ai_usage").doc(usageId(rec.day, rec.studentId)),
      { uid: rec.uid, student_id: rec.studentId, day: rec.day, ...add },
      { merge: true },
    );
    batch.set(this.db.collection("ai_usage_total").doc(rec.day), { day: rec.day, ...add }, { merge: true });
    await batch.commit();
  }

  async log(entry: LogEntry): Promise<void> {
    const now = Date.now();
    await this.db.collection("ai_logs").add({
      ...entry,
      created_at: Timestamp.fromMillis(now),
      // Firestore deletes the log after this time (TTL policy, firestore.indexes.json).
      expire_at: Timestamp.fromMillis(now + LOG_DAYS * 24 * 60 * 60 * 1000),
    });
  }

  async projectCost(day: string): Promise<number> {
    return (await this.db.collection("ai_usage_total").doc(day).get()).get("cost_usd") ?? 0;
  }

  async waitingAnswers(limit: number): Promise<QueuedAnswer[]> {
    const snap = await this.db.collection("ai_queue").where("status", "==", "waiting").limit(limit).get();
    return snap.docs.map((doc) => ({
      id: doc.id,
      uid: doc.get("uid"),
      student_id: doc.get("student_id"),
      lesson_id: doc.get("lesson_id"),
      step_id: doc.get("step_id"),
      lang: doc.get("lang"),
      answer: doc.get("answer"),
      created_at: (doc.get("created_at") as Timestamp | undefined)?.toDate() ?? new Date(0),
    }));
  }

  async markQueued(ids: string[], status: "in_batch" | "skipped", batchId?: string): Promise<void> {
    const batch = this.db.batch();
    for (const id of ids) {
      batch.update(this.db.collection("ai_queue").doc(id), { status, batch_id: batchId ?? null });
    }
    await batch.commit();
  }

  async answerQueued(id: string, result: QueueResult | null): Promise<void> {
    await this.db
      .collection("ai_queue")
      .doc(id)
      .update(
        result
          ? { status: "answered", level: result.level, reply: result.reply, answered_at: FieldValue.serverTimestamp() }
          : { status: "failed", answered_at: FieldValue.serverTimestamp() },
      );
  }

  async saveBatch(batch: BatchInfo): Promise<void> {
    await this.db
      .collection("ai_batches")
      .doc(batch.id)
      .set({ items: batch.items, status: "in_progress", created_at: FieldValue.serverTimestamp() });
  }

  async openBatches(): Promise<BatchInfo[]> {
    const snap = await this.db.collection("ai_batches").where("status", "==", "in_progress").get();
    return snap.docs.map((doc) => ({ id: doc.id, items: doc.get("items") }));
  }

  async closeBatch(id: string): Promise<void> {
    await this.db.collection("ai_batches").doc(id).update({ status: "ended", ended_at: FieldValue.serverTimestamp() });
  }

  async saveReport(uid: string, studentId: string, week: string, stats: unknown, note: unknown): Promise<void> {
    await this.student(uid, studentId)
      .collection("reports")
      .doc(week)
      .set({ week, stats, note, created_at: FieldValue.serverTimestamp() });
  }

  async allStudents(): Promise<StudentRef[]> {
    const snap = await this.db.collectionGroup("students").get();
    return snap.docs
      .filter((doc) => doc.ref.parent.parent?.parent.id === "accounts")
      .map((doc) => ({ uid: doc.ref.parent.parent!.id, studentId: doc.id, grade: doc.get("grade") ?? 0 }));
  }

  async studentActivity(uid: string, studentId: string) {
    const ref = this.student(uid, studentId);
    const [progress, skills] = await Promise.all([ref.collection("progress").get(), ref.collection("skills").get()]);
    return {
      progress: progress.docs.map((d) => d.data()),
      skills: skills.docs.map((d) => d.data()),
    };
  }

  async studentsOf(uid: string): Promise<string[]> {
    const refs = await this.db.collection("accounts").doc(uid).collection("students").listDocuments();
    return refs.map((ref) => ref.id);
  }

  async usageFor(days: string[], students: { uid: string; studentId: string }[] | "all"): Promise<UsageRow[]> {
    let docs: FirebaseFirestore.DocumentSnapshot[];
    if (students === "all") {
      docs = (await this.db.collection("ai_usage").where("day", "in", days).get()).docs;
    } else {
      const refs = students.flatMap((s) => days.map((day) => this.db.collection("ai_usage").doc(usageId(day, s.studentId))));
      docs = refs.length ? (await this.db.getAll(...refs)).filter((d) => d.exists) : [];
      // A student id is unique, but check the account too.
      const owners = new Set(students.map((s) => `${s.uid}/${s.studentId}`));
      docs = docs.filter((d) => owners.has(`${d.get("uid")}/${d.get("student_id")}`));
    }
    return docs.map((d) => ({
      day: d.get("day"),
      uid: d.get("uid"),
      student_id: d.get("student_id"),
      calls: d.get("calls") ?? 0,
      text: d.get("text") ?? 0,
      photo: d.get("photo") ?? 0,
      cost_usd: d.get("cost_usd") ?? 0,
    }));
  }
}
