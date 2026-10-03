/**
 * A small Firestore client over the REST API, for the Cloudflare Worker
 * (which can't run firebase-admin). It signs in as the Firebase service
 * account, so like firebase-admin it is not bound by the security rules.
 *
 * Docs: https://firebase.google.com/docs/firestore/reference/rest
 */
import { SignJWT, importPKCS8 } from "jose";

export interface ServiceAccount {
  project_id: string;
  client_email: string;
  private_key: string;
}

/** Parses the FIREBASE_SERVICE_ACCOUNT secret (the JSON key file's text). */
export function parseServiceAccount(json: string): ServiceAccount {
  let data: Partial<ServiceAccount>;
  try {
    data = JSON.parse(json) as Partial<ServiceAccount>;
  } catch {
    throw new Error("FIREBASE_SERVICE_ACCOUNT is not valid JSON");
  }
  if (!data.project_id || !data.client_email || !data.private_key) {
    throw new Error("FIREBASE_SERVICE_ACCOUNT is missing project_id, client_email or private_key");
  }
  return data as ServiceAccount;
}

// ---- Values ---------------------------------------------------------------

/** A Firestore value as the REST API writes it. */
export type Value =
  | { nullValue: null }
  | { booleanValue: boolean }
  | { integerValue: string }
  | { doubleValue: number }
  | { timestampValue: string }
  | { stringValue: string }
  | { arrayValue: { values?: Value[] } }
  | { mapValue: { fields?: Record<string, Value> } };

export type Fields = Record<string, Value>;

/** Plain JavaScript to a Firestore value. Dates become timestamps. */
export function toValue(value: unknown): Value {
  if (value === null || value === undefined) return { nullValue: null };
  if (typeof value === "boolean") return { booleanValue: value };
  if (typeof value === "number") {
    return Number.isInteger(value) ? { integerValue: String(value) } : { doubleValue: value };
  }
  if (typeof value === "string") return { stringValue: value };
  if (value instanceof Date) return { timestampValue: value.toISOString() };
  if (Array.isArray(value)) return { arrayValue: { values: value.map(toValue) } };
  if (typeof value === "object") return { mapValue: { fields: toFields(value as Record<string, unknown>) } };
  throw new Error(`can't store ${typeof value}`);
}

export function toFields(data: Record<string, unknown>): Fields {
  const fields: Fields = {};
  for (const [key, v] of Object.entries(data)) if (v !== undefined) fields[key] = toValue(v);
  return fields;
}

/** A Firestore value to plain JavaScript. Timestamps become Dates. */
export function fromValue(value: Value): unknown {
  if ("nullValue" in value) return null;
  if ("booleanValue" in value) return value.booleanValue;
  if ("integerValue" in value) return Number(value.integerValue);
  if ("doubleValue" in value) return value.doubleValue;
  if ("timestampValue" in value) return new Date(value.timestampValue);
  if ("stringValue" in value) return value.stringValue;
  if ("arrayValue" in value) return (value.arrayValue.values ?? []).map(fromValue);
  if ("mapValue" in value) return fromFields(value.mapValue.fields ?? {});
  return null; // bytes, references, geo points: not used here.
}

export function fromFields(fields: Fields): Record<string, unknown> {
  const data: Record<string, unknown> = {};
  for (const [key, v] of Object.entries(fields)) data[key] = fromValue(v);
  return data;
}

/** A field path segment, quoted when it isn't a plain name (e.g. "g9-x/s1"). */
export function fieldPath(...segments: string[]): string {
  return segments
    .map((s) => (/^[A-Za-z_][A-Za-z_0-9]*$/.test(s) ? s : "`" + s.replace(/[\\`]/g, (c) => "\\" + c) + "`"))
    .join(".");
}

// ---- Documents and writes -------------------------------------------------

export interface Doc {
  /** Full resource name: projects/p/databases/(default)/documents/a/b. */
  name: string;
  /** The path after .../documents/, e.g. "ai_usage/2026-10-03_s1". */
  path: string;
  id: string;
  data: Record<string, unknown>;
}

/** One write in a commit. */
export type Write =
  | {
      /** Sets the listed fields (all of [data] when [merge] is false) and applies increments. */
      kind: "set";
      path: string;
      data: Record<string, unknown>;
      merge?: boolean;
      /** Field path -> amount to add. */
      increments?: Record<string, number>;
      /** Field paths set to the server's time. */
      serverTimes?: string[];
      /** Only if the document exists (an update) or doesn't (a create). */
      exists?: boolean;
    }
  | { kind: "delete"; path: string };

export type Filter =
  | { field: string; op: "EQUAL" | "LESS_THAN" | "IN"; value: unknown };

export interface Query {
  /** Parent path ("" for the root, or e.g. "accounts/u1"). */
  parent?: string;
  collection: string;
  /** All collections with this id, anywhere (a collection group). */
  allDescendants?: boolean;
  where?: Filter[];
  limit?: number;
}

type Fetch = (input: string, init?: RequestInit) => Promise<Response>;

export class FirestoreError extends Error {
  constructor(
    message: string,
    readonly status: number,
  ) {
    super(message);
  }
}

export class Firestore {
  private token: { value: string; expires: number } | null = null;
  private readonly root: string;

  constructor(
    private readonly account: ServiceAccount,
    private readonly fetchFn: Fetch = (input, init) => fetch(input, init),
    private readonly now: () => number = Date.now,
  ) {
    this.root = `projects/${account.project_id}/databases/(default)/documents`;
  }

  private url(rest: string) {
    return `https://firestore.googleapis.com/v1/${rest}`;
  }

  /** An OAuth token for the service account, reused until shortly before it expires. */
  private async accessToken(): Promise<string> {
    const now = this.now();
    if (this.token && this.token.expires > now + 60_000) return this.token.value;
    const key = await importPKCS8(this.account.private_key, "RS256");
    const assertion = await new SignJWT({ scope: "https://www.googleapis.com/auth/datastore" })
      .setProtectedHeader({ alg: "RS256", typ: "JWT" })
      .setIssuer(this.account.client_email)
      .setSubject(this.account.client_email)
      .setAudience("https://oauth2.googleapis.com/token")
      .setIssuedAt(Math.floor(now / 1000))
      .setExpirationTime(Math.floor(now / 1000) + 3600)
      .sign(key);
    const response = await this.fetchFn("https://oauth2.googleapis.com/token", {
      method: "POST",
      headers: { "content-type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams({ grant_type: "urn:ietf:params:oauth:grant-type:jwt-bearer", assertion }).toString(),
    });
    if (!response.ok) throw new FirestoreError(`service account sign-in failed (${response.status})`, response.status);
    const body = (await response.json()) as { access_token: string; expires_in: number };
    this.token = { value: body.access_token, expires: now + body.expires_in * 1000 };
    return body.access_token;
  }

  private async call<T>(method: string, rest: string, body?: unknown): Promise<T> {
    const response = await this.fetchFn(this.url(rest), {
      method,
      headers: { authorization: `Bearer ${await this.accessToken()}`, "content-type": "application/json" },
      body: body === undefined ? undefined : JSON.stringify(body),
    });
    if (!response.ok) {
      const text = await response.text();
      throw new FirestoreError(`Firestore ${method} ${rest.split("?")[0]}: ${response.status} ${text.slice(0, 300)}`, response.status);
    }
    return (await response.json()) as T;
  }

  private doc(raw: { name: string; fields?: Fields }): Doc {
    const path = raw.name.slice(this.root.length + 1);
    return { name: raw.name, path, id: path.split("/").pop()!, data: fromFields(raw.fields ?? {}) };
  }

  /** One document, or null when it doesn't exist. */
  async get(path: string, transaction?: string): Promise<Doc | null> {
    const docs = await this.getAll([path], transaction);
    return docs[0];
  }

  /** Several documents in one request, in the same order (null if missing). */
  async getAll(paths: string[], transaction?: string): Promise<(Doc | null)[]> {
    if (!paths.length) return [];
    const results = await this.call<{ found?: { name: string; fields?: Fields }; missing?: string }[]>(
      "POST",
      `${this.root}:batchGet`,
      { documents: paths.map((p) => `${this.root}/${p}`), ...(transaction ? { transaction } : {}) },
    );
    const byName = new Map<string, Doc>();
    for (const r of results) if (r.found) byName.set(r.found.name, this.doc(r.found));
    return paths.map((p) => byName.get(`${this.root}/${p}`) ?? null);
  }

  async query(q: Query): Promise<Doc[]> {
    const where = (q.where ?? []).map((f) => ({
      fieldFilter: { field: { fieldPath: f.field }, op: f.op, value: toValue(f.value) },
    }));
    const structuredQuery: Record<string, unknown> = {
      from: [{ collectionId: q.collection, allDescendants: q.allDescendants ?? false }],
    };
    if (where.length === 1) structuredQuery.where = where[0];
    if (where.length > 1) structuredQuery.where = { compositeFilter: { op: "AND", filters: where } };
    if (q.limit) structuredQuery.limit = q.limit;
    const parent = q.parent ? `${this.root}/${q.parent}` : this.root;
    const rows = await this.call<{ document?: { name: string; fields?: Fields } }[]>("POST", `${parent}:runQuery`, {
      structuredQuery,
    });
    return rows.filter((r) => r.document).map((r) => this.doc(r.document!));
  }

  /** The ids of a collection's documents (including ones with only subcollections). */
  async listIds(collectionPath: string): Promise<string[]> {
    const ids: string[] = [];
    let pageToken = "";
    do {
      const params = new URLSearchParams({ pageSize: "300", showMissing: "true", "mask.fieldPaths": "__name__" });
      if (pageToken) params.set("pageToken", pageToken);
      const page = await this.call<{ documents?: { name: string }[]; nextPageToken?: string }>(
        "GET",
        `${this.root}/${collectionPath}?${params}`,
      );
      for (const d of page.documents ?? []) ids.push(d.name.split("/").pop()!);
      pageToken = page.nextPageToken ?? "";
    } while (pageToken);
    return ids;
  }

  async beginTransaction(): Promise<string> {
    return (await this.call<{ transaction: string }>("POST", `${this.root}:beginTransaction`, {})).transaction;
  }

  async rollback(transaction: string): Promise<void> {
    await this.call("POST", `${this.root}:rollback`, { transaction });
  }

  /** Applies [writes] atomically (at most 500), optionally ending [transaction]. */
  async commit(writes: Write[], transaction?: string): Promise<void> {
    if (!writes.length && !transaction) return;
    await this.call("POST", `${this.root}:commit`, {
      writes: writes.map((w) => this.write(w)),
      ...(transaction ? { transaction } : {}),
    });
  }

  /** A new document id, like Firestore's own (20 letters and digits). */
  static newId(): string {
    const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    const bytes = crypto.getRandomValues(new Uint8Array(20));
    return Array.from(bytes, (b) => chars[b % chars.length]).join("");
  }

  private write(w: Write): Record<string, unknown> {
    const name = `${this.root}/${w.path}`;
    if (w.kind === "delete") return { delete: name };
    const out: Record<string, unknown> = { update: { name, fields: toFields(w.data) } };
    if (w.merge) out.updateMask = { fieldPaths: Object.keys(w.data).map((k) => fieldPath(k)) };
    const transforms = [
      ...Object.entries(w.increments ?? {}).map(([path, n]) => ({ fieldPath: path, increment: toValue(n) })),
      ...(w.serverTimes ?? []).map((path) => ({ fieldPath: path, setToServerValue: "REQUEST_TIME" })),
    ];
    if (transforms.length) out.updateTransforms = transforms;
    if (w.exists !== undefined) out.currentDocument = { exists: w.exists };
    return out;
  }
}
