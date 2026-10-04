/** The cost dashboard: AI calls and estimated cost per student per day. */
import { dayOf } from "./config";
import type { DailyTotals } from "./learning";
import type { Store, UsageRow } from "./store";

export interface CostReport {
  /** True when the caller sees the whole project (an admin email). */
  all: boolean;
  days: string[];
  rows: UsageRow[];
  total_usd: number;
  /** Learning totals for the whole project, newest first (admins only). */
  learning?: DailyTotals[];
}

/** The last [count] days in Pakistan time, newest first. */
export function lastDays(now: Date, count: number): string[] {
  return Array.from({ length: count }, (_, i) => dayOf(new Date(now.getTime() - i * 86_400_000)));
}

/** Admins see every student; everyone else their own account's students. */
export async function costReport(
  store: Store,
  caller: { uid: string; email?: string; emailVerified?: boolean },
  adminEmails: string[],
  now: Date,
): Promise<CostReport> {
  const days = lastDays(now, 7);
  const email = caller.email?.toLowerCase();
  const all = !!email && caller.emailVerified === true && adminEmails.includes(email);
  const rows = all
    ? await store.usageFor(days, "all")
    : await store.usageFor(
        days,
        (await store.studentsOf(caller.uid)).map((studentId) => ({ uid: caller.uid, studentId })),
      );
  rows.sort((a, b) => b.day.localeCompare(a.day) || b.cost_usd - a.cost_usd);
  const total = rows.reduce((sum, r) => sum + r.cost_usd, 0);
  const report: CostReport = { all, days, rows, total_usd: Math.round(total * 1e6) / 1e6 };
  if (all) {
    report.learning = (await store.dailyTotals(days)).sort((a, b) => b.day.localeCompare(a.day));
  }
  return report;
}

/** Parses the ADMIN_EMAILS setting: comma-separated, any case. */
export function parseAdminEmails(value: string): string[] {
  return value
    .split(",")
    .map((e) => e.trim().toLowerCase())
    .filter((e) => e.includes("@"));
}
