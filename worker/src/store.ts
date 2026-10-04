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
 * ai_logs/{auto}           every call, for review; deleted after 90 days by the batch job
 * daily_totals/{day}       learning totals for the whole project (no child's data)
 * ai_queue/{id}            answers that waited offline (the app creates and reads them)
 * ai_batches/{batchId}     batches sent to the Batch API
 * ```
 */
import { LOG_DAYS } from "./config";
import type { DailyTotals, ProgressDoc } from "./learning";
import { Firestore, fieldPath, type Doc, type Write } from "./firestore";
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
  /** Deletes logs past their `expire_at`; returns how many. */
  deleteOldLogs(now: Date): Promise<number>;
  /** Sends any writes the store held back (scheduled jobs write in one go). */
  flush(): Promise<void>;
  usageFor(days: string[], students: { uid: string; studentId: string }[] | "all"): Promise<UsageRow[]>;

  /** Whether [day]'s learning totals were already counted. */
  hasDailyTotals(day: string): Promise<boolean>;
  /** Every child's lesson progress (for the daily totals). */
  allProgress(): Promise<ProgressDoc[]>;
  /** The whole project's AI calls and cost on [day]. */
  projectUsage(day: string): Promise<{ calls: number; cost_usd: number }>;
  saveDailyTotals(totals: DailyTotals): Promise<void>;
  dailyTotals(days: string[]): Promise<DailyTotals[]>;
}

const usageId = (day: string, studentId: string) => `${day}_${studentId}`;
const num = (v: unknown) => (typeof v === "number" ? v : 0);

/**
 * The Store on Firestore's REST API. With `deferWrites` (the scheduled
 * jobs), writes are held and sent together by [flush], in as few requests as
 * possible: a free Cloudflare Worker may make only 50 requests per run.
 */
export class FirestoreStore implements Store {
  private pending: Write[] = [];
  /** Usage increments per document, merged before [flush]. */
  private pendingUsage = new Map<string, { data: Record<string, unknown>; increments: Record<string, number> }>();
  private activity: Map<string, { progress: Record<string, unknown>[]; skills: Record<string, unknown>[] }> | null = null;

  constructor(
    private readonly db: Firestore,
    private readonly options: { deferWrites?: boolean } = {},
  ) {}

  private studentPath(uid: string, studentId: string) {
    return `accounts/${uid}/students/${studentId}`;
  }

  private async write(...writes: Write[]): Promise<void> {
    if (this.options.deferWrites) this.pending.push(...writes);
    else await this.db.commit(writes);
  }

  async flush(): Promise<void> {
    const writes = [...this.pending];
    for (const [path, u] of this.pendingUsage) {
      writes.push({ kind: "set", path, data: u.data, merge: true, increments: u.increments });
    }
    this.pending = [];
    this.pendingUsage.clear();
    for (let i = 0; i < writes.length; i += 400) await this.db.commit(writes.slice(i, i + 400));
  }

  async studentExists(uid: string, studentId: string): Promise<boolean> {
    return (await this.db.get(this.studentPath(uid, studentId))) !== null;
  }

  async reserve(r: Reservation): Promise<ReserveResult> {
    const usagePath = `ai_usage/${usageId(r.day, r.studentId)}`;
    const totalPath = `ai_usage_total/${r.day}`;
    // Firestore retries nothing here: a clash (two calls at the same
    // moment) fails the commit, and the second call gets a fallback.
    const tx = await this.db.beginTransaction();
    let result: ReserveResult = "ok";
    try {
      const [usage, total] = await this.db.getAll([usagePath, totalPath], tx);
      const u = usage?.data ?? {};
      const steps = (u.steps ?? {}) as Record<string, unknown>;
      if (num(total?.data.cost_usd) >= r.globalDailyUsd) result = "budget";
      else if (num(u[r.kind]) >= r.kindLimit) result = "student_limit";
      else if (num(steps[r.stepKey]) >= r.stepLimit) result = "step_limit";
    } catch (error) {
      await this.db.rollback(tx).catch(() => {});
      throw error;
    }
    if (result !== "ok") {
      await this.db.rollback(tx);
      return result;
    }
    await this.db.commit(
      [
        {
          kind: "set",
          path: usagePath,
          data: { uid: r.uid, student_id: r.studentId, day: r.day },
          merge: true,
          increments: { [r.kind]: 1, [fieldPath("steps", r.stepKey)]: 1 },
        },
      ],
      tx,
    );
    return "ok";
  }

  async release(r: Reservation): Promise<void> {
    await this.db.commit([
      {
        kind: "set",
        path: `ai_usage/${usageId(r.day, r.studentId)}`,
        data: {},
        merge: true,
        increments: { [r.kind]: -1, [fieldPath("steps", r.stepKey)]: -1 },
      },
    ]);
  }

  async recordUsage(rec: UsageRecord): Promise<void> {
    const add: Record<string, number> = {
      calls: rec.calls,
      input_tokens: rec.usage.input_tokens,
      output_tokens: rec.usage.output_tokens,
      cache_read_tokens: rec.usage.cache_read_input_tokens ?? 0,
      cost_usd: rec.costUsd,
    };
    const docs: [string, Record<string, unknown>][] = [
      [`ai_usage/${usageId(rec.day, rec.studentId)}`, { uid: rec.uid, student_id: rec.studentId, day: rec.day }],
      [`ai_usage_total/${rec.day}`, { day: rec.day }],
    ];
    if (this.options.deferWrites) {
      for (const [path, data] of docs) {
        const u = this.pendingUsage.get(path) ?? { data, increments: {} };
        for (const [k, v] of Object.entries(add)) u.increments[k] = (u.increments[k] ?? 0) + v;
        this.pendingUsage.set(path, u);
      }
      return;
    }
    await this.db.commit(docs.map(([path, data]) => ({ kind: "set", path, data, merge: true, increments: add })));
  }

  async log(entry: LogEntry): Promise<void> {
    const now = Date.now();
    await this.write({
      kind: "set",
      path: `ai_logs/${Firestore.newId()}`,
      data: {
        ...entry,
        // The model's reply exactly as it came, as text.
        output: JSON.stringify(entry.output ?? null),
        created_at: new Date(now),
        expire_at: new Date(now + LOG_DAYS * 86_400_000),
      },
    });
  }

  async deleteOldLogs(now: Date): Promise<number> {
    const old = await this.db.query({
      collection: "ai_logs",
      where: [{ field: "expire_at", op: "LESS_THAN", value: now }],
      limit: 300,
    });
    await this.write(...old.map((d): Write => ({ kind: "delete", path: d.path })));
    return old.length;
  }

  async projectCost(day: string): Promise<number> {
    return num((await this.db.get(`ai_usage_total/${day}`))?.data.cost_usd);
  }

  async waitingAnswers(limit: number): Promise<QueuedAnswer[]> {
    const docs = await this.db.query({ collection: "ai_queue", where: [{ field: "status", op: "EQUAL", value: "waiting" }], limit });
    return docs.map((doc) => ({
      id: doc.id,
      uid: doc.data.uid as string,
      student_id: doc.data.student_id as string,
      lesson_id: doc.data.lesson_id as string,
      step_id: doc.data.step_id as string,
      lang: doc.data.lang as string,
      answer: doc.data.answer as string,
      created_at: doc.data.created_at instanceof Date ? doc.data.created_at : new Date(0),
    }));
  }

  async markQueued(ids: string[], status: "in_batch" | "skipped", batchId?: string): Promise<void> {
    await this.write(
      ...ids.map(
        // The typed answer isn't kept once it has been sent or skipped.
        (id): Write => ({
          kind: "set", path: `ai_queue/${id}`, data: { status, batch_id: batchId ?? null, answer: "" }, merge: true, exists: true,
        }),
      ),
    );
  }

  async answerQueued(id: string, result: QueueResult | null): Promise<void> {
    await this.write({
      kind: "set",
      path: `ai_queue/${id}`,
      data: result ? { status: "answered", level: result.level, reply: result.reply } : { status: "failed" },
      merge: true,
      exists: true,
      serverTimes: ["answered_at"],
    });
  }

  async saveBatch(batch: BatchInfo): Promise<void> {
    await this.write({
      kind: "set",
      path: `ai_batches/${batch.id}`,
      data: { items: JSON.stringify(batch.items), status: "in_progress" },
      serverTimes: ["created_at"],
    });
  }

  async openBatches(): Promise<BatchInfo[]> {
    const docs = await this.db.query({ collection: "ai_batches", where: [{ field: "status", op: "EQUAL", value: "in_progress" }] });
    return docs.map((doc) => ({ id: doc.id, items: JSON.parse(String(doc.data.items ?? "{}")) }));
  }

  async closeBatch(id: string): Promise<void> {
    await this.write({ kind: "set", path: `ai_batches/${id}`, data: { status: "ended" }, merge: true, serverTimes: ["ended_at"] });
  }

  async saveReport(uid: string, studentId: string, week: string, stats: unknown, note: unknown): Promise<void> {
    await this.write({
      kind: "set",
      path: `${this.studentPath(uid, studentId)}/reports/${week}`,
      data: { week, stats, note },
      serverTimes: ["created_at"],
    });
  }

  /**
   * Every student, with everyone's progress and skills read in the same
   * go (three queries in all, instead of two per student).
   */
  async allStudents(): Promise<StudentRef[]> {
    const [students, progress, skills] = await Promise.all(
      ["students", "progress", "skills"].map((collection) => this.db.query({ collection, allDescendants: true })),
    );
    // accounts/{uid}/students/{sid}[/progress|skills/{id}]
    const owner = (doc: Doc) => doc.path.split("/").slice(0, 4).join("/");
    this.activity = new Map();
    const activityOf = (key: string) => {
      if (!this.activity!.has(key)) this.activity!.set(key, { progress: [], skills: [] });
      return this.activity!.get(key)!;
    };
    for (const doc of progress) activityOf(owner(doc)).progress.push(doc.data);
    for (const doc of skills) activityOf(owner(doc)).skills.push(doc.data);
    return students
      .filter((doc) => doc.path.split("/").length === 4 && doc.path.startsWith("accounts/"))
      .map((doc) => {
        const [, uid, , studentId] = doc.path.split("/");
        return { uid, studentId, grade: num(doc.data.grade) };
      });
  }

  async studentActivity(uid: string, studentId: string) {
    const key = this.studentPath(uid, studentId);
    const cached = this.activity?.get(key);
    if (cached || this.activity) return cached ?? { progress: [], skills: [] };
    const [progress, skills] = await Promise.all(
      ["progress", "skills"].map((collection) => this.db.query({ parent: key, collection })),
    );
    return { progress: progress.map((d) => d.data), skills: skills.map((d) => d.data) };
  }

  async studentsOf(uid: string): Promise<string[]> {
    return this.db.listIds(`accounts/${uid}/students`);
  }

  async usageFor(days: string[], students: { uid: string; studentId: string }[] | "all"): Promise<UsageRow[]> {
    let docs: Doc[];
    if (students === "all") {
      docs = await this.db.query({ collection: "ai_usage", where: [{ field: "day", op: "IN", value: days }] });
    } else {
      const paths = students.flatMap((s) => days.map((day) => `ai_usage/${usageId(day, s.studentId)}`));
      docs = (await this.db.getAll(paths)).filter((d): d is Doc => d !== null);
      // A student id is unique, but check the account too.
      const owners = new Set(students.map((s) => `${s.uid}/${s.studentId}`));
      docs = docs.filter((d) => owners.has(`${d.data.uid}/${d.data.student_id}`));
    }
    return docs.map((d) => ({
      day: d.data.day as string,
      uid: d.data.uid as string,
      student_id: d.data.student_id as string,
      calls: num(d.data.calls),
      text: num(d.data.text),
      photo: num(d.data.photo),
      cost_usd: num(d.data.cost_usd),
    }));
  }

  async hasDailyTotals(day: string): Promise<boolean> {
    return (await this.db.get(`daily_totals/${day}`)) !== null;
  }

  async allProgress(): Promise<ProgressDoc[]> {
    const docs = await this.db.query({ collection: "progress", allDescendants: true });
    // accounts/{uid}/students/{sid}/progress/{lessonId}
    return docs
      .filter((d) => d.path.startsWith("accounts/") && d.path.split("/").length === 6)
      .map((d) => ({ owner: d.path.split("/").slice(0, 4).join("/"), data: d.data }));
  }

  async projectUsage(day: string): Promise<{ calls: number; cost_usd: number }> {
    const doc = await this.db.get(`ai_usage_total/${day}`);
    return { calls: num(doc?.data.calls), cost_usd: num(doc?.data.cost_usd) };
  }

  async saveDailyTotals(totals: DailyTotals): Promise<void> {
    await this.write({ kind: "set", path: `daily_totals/${totals.day}`, data: { ...totals }, serverTimes: ["counted_at"] });
  }

  async dailyTotals(days: string[]): Promise<DailyTotals[]> {
    const docs = await this.db.getAll(days.map((day) => `daily_totals/${day}`));
    return docs.filter((d): d is Doc => d !== null).map((d) => d.data as unknown as DailyTotals);
  }
}
