/** In-memory fakes for the store, Claude and the Batch API. */
import type { DailyTotals, ProgressDoc } from "../learning";
import type { BatchApi } from "../batch";
import type { ClaudeCaller, JsonReply, JsonRequest } from "../claude";
import { LessonLibrary } from "../lessons";
import type { TokenUsage } from "../pricing";
import type {
  BatchInfo,
  LogEntry,
  QueueResult,
  QueuedAnswer,
  Reservation,
  ReserveResult,
  Store,
  StudentRef,
  UsageRecord,
  UsageRow,
} from "../store";

export const USAGE: TokenUsage = { input_tokens: 900, output_tokens: 120 };

export function lessons(): LessonLibrary {
  return LessonLibrary.bundled();
}

interface Usage {
  uid: string;
  text: number;
  photo: number;
  steps: Record<string, number>;
  calls: number;
  cost: number;
}

export class MemoryStore implements Store {
  students = new Set<string>(); // "uid/sid"
  grades = new Map<string, number>();
  usage = new Map<string, Usage>(); // "day_sid"
  totals = new Map<string, number>(); // day -> cost
  logs: LogEntry[] = [];
  queue = new Map<string, QueuedAnswer & { status: string; batch_id?: string; result?: QueueResult | null }>();
  batches = new Map<string, BatchInfo & { status: string }>();
  reports: { uid: string; studentId: string; week: string; stats: unknown; note: unknown }[] = [];
  activity = new Map<string, { progress: Record<string, unknown>[]; skills: Record<string, unknown>[] }>();

  addStudent(uid: string, sid: string, grade = 6) {
    this.students.add(`${uid}/${sid}`);
    this.grades.set(`${uid}/${sid}`, grade);
  }

  private row(day: string, sid: string, uid: string): Usage {
    const key = `${day}_${sid}`;
    if (!this.usage.has(key)) this.usage.set(key, { uid, text: 0, photo: 0, steps: {}, calls: 0, cost: 0 });
    return this.usage.get(key)!;
  }

  async studentExists(uid: string, sid: string) {
    return this.students.has(`${uid}/${sid}`);
  }

  async reserve(r: Reservation): Promise<ReserveResult> {
    if ((this.totals.get(r.day) ?? 0) >= r.globalDailyUsd) return "budget";
    const row = this.row(r.day, r.studentId, r.uid);
    if (row[r.kind] >= r.kindLimit) return "student_limit";
    if ((row.steps[r.stepKey] ?? 0) >= r.stepLimit) return "step_limit";
    row[r.kind]++;
    row.steps[r.stepKey] = (row.steps[r.stepKey] ?? 0) + 1;
    return "ok";
  }

  async release(r: Reservation) {
    const row = this.row(r.day, r.studentId, r.uid);
    row[r.kind]--;
    row.steps[r.stepKey]--;
  }

  async recordUsage(rec: UsageRecord) {
    const row = this.row(rec.day, rec.studentId, rec.uid);
    row.calls += rec.calls;
    row.cost += rec.costUsd;
    this.totals.set(rec.day, (this.totals.get(rec.day) ?? 0) + rec.costUsd);
  }

  async log(entry: LogEntry) {
    this.logs.push(entry);
  }

  async projectCost(day: string) {
    return this.totals.get(day) ?? 0;
  }

  /** Daily learning totals by day, and every child's progress documents. */
  daily = new Map<string, DailyTotals>();
  progressDocs: ProgressDoc[] = [];
  aiCalls = new Map<string, number>(); // day -> calls

  async hasDailyTotals(day: string) {
    return this.daily.has(day);
  }

  async allProgress() {
    return this.progressDocs;
  }

  async projectUsage(day: string) {
    return { calls: this.aiCalls.get(day) ?? 0, cost_usd: this.totals.get(day) ?? 0 };
  }

  async saveDailyTotals(totals: DailyTotals) {
    this.daily.set(totals.day, totals);
  }

  async dailyTotals(days: string[]) {
    return days.flatMap((d) => (this.daily.has(d) ? [this.daily.get(d)!] : []));
  }

  async waitingAnswers(limit: number) {
    return [...this.queue.values()].filter((q) => q.status === "waiting").slice(0, limit);
  }

  async markQueued(ids: string[], status: "in_batch" | "skipped", batchId?: string) {
    for (const id of ids) Object.assign(this.queue.get(id)!, { status, batch_id: batchId, answer: "" });
  }

  async answerQueued(id: string, result: QueueResult | null) {
    Object.assign(this.queue.get(id)!, { status: result ? "answered" : "failed", result });
  }

  async saveBatch(batch: BatchInfo) {
    this.batches.set(batch.id, { ...batch, status: "in_progress" });
  }

  async openBatches() {
    return [...this.batches.values()].filter((b) => b.status === "in_progress");
  }

  async closeBatch(id: string) {
    this.batches.get(id)!.status = "ended";
  }

  async saveReport(uid: string, studentId: string, week: string, stats: unknown, note: unknown) {
    this.reports.push({ uid, studentId, week, stats, note });
  }

  async allStudents(): Promise<StudentRef[]> {
    return [...this.students].map((key) => {
      const [uid, studentId] = key.split("/");
      return { uid, studentId, grade: this.grades.get(key) ?? 0 };
    });
  }

  async studentActivity(uid: string, studentId: string) {
    return this.activity.get(`${uid}/${studentId}`) ?? { progress: [], skills: [] };
  }

  async studentsOf(uid: string) {
    return [...this.students].filter((k) => k.startsWith(`${uid}/`)).map((k) => k.split("/")[1]);
  }

  flushed = 0;
  async flush() {
    this.flushed++;
  }

  async deleteOldLogs() {
    return 0;
  }

  async usageFor(days: string[], students: { uid: string; studentId: string }[] | "all"): Promise<UsageRow[]> {
    const rows: UsageRow[] = [];
    for (const [key, u] of this.usage) {
      const [day, sid] = key.split("_");
      if (!days.includes(day)) continue;
      if (students !== "all" && !students.some((s) => s.studentId === sid && s.uid === u.uid)) continue;
      rows.push({ day, uid: u.uid, student_id: sid, calls: u.calls, text: u.text, photo: u.photo, cost_usd: u.cost });
    }
    return rows;
  }
}

/** Returns the queued replies in order; an Error in the queue is thrown. */
export class FakeClaude implements ClaudeCaller {
  requests: JsonRequest[] = [];
  constructor(public replies: (unknown | Error)[] = []) {}

  async json<T>(request: JsonRequest): Promise<JsonReply<T>> {
    this.requests.push(request);
    const next = this.replies.shift();
    if (next instanceof Error) throw next;
    return { data: next as T, model: request.model, usage: USAGE };
  }
}

type Message = { stop_reason: string; content: { type: string; text: string }[]; model: string; usage: TokenUsage };

export function message(data: unknown, model = "claude-haiku-4-5-20251001"): Message {
  return { stop_reason: "end_turn", content: [{ type: "text", text: JSON.stringify(data) }], model, usage: USAGE };
}

export class FakeBatches implements BatchApi {
  created: { id: string; requests: { custom_id: string; params: unknown }[] }[] = [];
  ended = new Set<string>();
  /** custom_id -> message (null = errored). */
  answers = new Map<string, Message | null>();

  async create(requests: { custom_id: string; params: unknown }[]) {
    const id = `batch_${this.created.length + 1}`;
    this.created.push({ id, requests });
    return { id };
  }

  async isEnded(id: string) {
    return this.ended.has(id);
  }

  async *results(id: string) {
    const batch = this.created.find((b) => b.id === id)!;
    for (const r of batch.requests) {
      if (this.answers.has(r.custom_id)) yield { custom_id: r.custom_id, message: this.answers.get(r.custom_id)! };
    }
  }
}
