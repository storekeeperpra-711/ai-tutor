/**
 * Removes personal details from what a child typed, before it is sent to
 * Claude or saved in the logs (Phase 10). Maths answers are full of
 * numbers, so only number patterns that look like a phone number or an
 * ID card number are removed, never ordinary answers like "x = 12".
 */

export const REMOVED = {
  phone: "[phone number removed]",
  email: "[email removed]",
  address: "[address removed]",
  id: "[ID number removed]",
  link: "[link removed]",
} as const;

/** Urdu-script digits (۰-۹ and ٠-٩) as Latin digits, for matching only. */
function latinDigits(text: string): string {
  return text.replace(/[۰-۹]/g, (d) => String(d.charCodeAt(0) - 0x06f0)).replace(/[٠-٩]/g, (d) => String(d.charCodeAt(0) - 0x0660));
}

const DIGIT = "[0-9۰-۹٠-٩]";

const EMAIL = /[A-Za-z0-9._%+-]+\s*(?:@|\(at\)|\[at\])\s*[A-Za-z0-9.-]+\s*(?:\.|\(dot\)|\[dot\])\s*[A-Za-z]{2,}/gi;

/** Emails spelled out to get past filters: "ali at gmail dot com". */
const SPELLED_EMAIL = /\b[A-Za-z0-9._-]+\s+at\s+[A-Za-z0-9-]+\s+dot\s+(?:com|pk|net|org)\b/gi;

const LINK = /\b(?:https?:\/\/|www\.)\S+/gi;

/** Pakistani ID card (CNIC): 12345-1234567-1, or 13 digits in a row. */
const CNIC = new RegExp(`(?<!${DIGIT})${DIGIT}{5}[-\\s]?${DIGIT}{7}[-\\s]?${DIGIT}(?!${DIGIT})`, "g");

/**
 * Groups of 2 or more digits joined by single spaces or dashes, as phone
 * numbers are written ("0300 1234567", "+92-300-1234567", "(042) 3576-1234").
 * Whether it is a phone number is decided in [looksLikePhone].
 */
const NUMBER_RUN = new RegExp(`(?:\\+|00)?\\(?${DIGIT}{2,}\\)?(?:[\\s-]\\(?${DIGIT}{2,}\\)?){0,5}`, "g");

function looksLikePhone(run: string): boolean {
  const latin = latinDigits(run);
  const digits = latin.replace(/[^0-9]/g, "");
  // The first group of digits: "0300" in "0300 1234567", "92" in "+92 300 ...".
  const firstGroup = latin.match(/[0-9]+/)![0];
  // International: +92 ..., 0092 ..., or any number written with +.
  if (latin.startsWith("+")) return digits.length >= 9 && digits.length <= 15;
  if (latin.startsWith("00") && digits.length >= 11 && digits.length <= 15) return true;
  // Pakistani mobiles (0300 1234567) and landlines (042 35761234).
  if (digits.startsWith("0") && firstGroup.length >= 3 && digits.length >= 10 && digits.length <= 12) return true;
  // A mobile without its 0 (300 1234567) or with 92 in front (92 300 1234567).
  if (digits.startsWith("3") && firstGroup.length >= 3 && digits.length === 10) return true;
  if (digits.startsWith("923") && digits.length === 12 && firstGroup.length >= 2) return true;
  // A long unbroken run is a contact number, not a school answer.
  return /^[0-9]{10,}$/.test(latin);
}

const NUMBER_MARK = `(?:no\\.?|number|num|nmbr|#)`;
const HOUSE_NUMBER = `#?\\s*[A-Za-z]?-?${DIGIT}+(?:[-/][A-Za-z0-9]+)?[A-Za-z]?\\b`;

/**
 * Address words followed by a number or a name: "house no 12",
 * "street 5", "gali number 3", "plot no 7", "mohalla Ali Pur",
 * "مکان نمبر ۱۲", "گلی نمبر 3", "محلہ ...". Words that also appear in
 * lessons (plot, block, sector, road) count only with "no"/"number"/"#".
 */
const ADDRESS = new RegExp(
  [
    `\\b(?:house|makan|makaan|flat|street|gali|galli|chak)\\s*${NUMBER_MARK}?\\s*${HOUSE_NUMBER}`,
    `\\b(?:ghar|home|plot|block|sector|road|lane|ward|apartment)\\s*${NUMBER_MARK}\\s*${HOUSE_NUMBER}`,
    `\\b(?:mohallah?|muhallah?|mohalah?|basti)\\s+[A-Za-z]+(?:\\s+[A-Za-z]+)?`,
    `\\b[A-Za-z]+\\s+(?:mohallah?|basti)\\b`,
    `(?:مکان|گھر|گلی|سٹریٹ|اسٹریٹ|پلاٹ|فلیٹ|بلاک|سیکٹر|چک|وارڈ)\\s*(?:نمبر|#)?\\s*${DIGIT}+(?:[-/]${DIGIT}+)?`,
    `(?:محلہ|محلے|کالونی|ٹاؤن|بستی|سوسائٹی)\\s+\\S+`,
    `\\S+\\s+(?:کالونی|ٹاؤن|بستی|سوسائٹی)`,
  ].join("|"),
  "gi",
);

export interface Redacted {
  text: string;
  /** The kinds of detail that were removed (empty if nothing was). */
  removed: (keyof typeof REMOVED)[];
}

/** Removes phone numbers, emails, ID numbers, links and addresses. */
export function redactPersonal(input: string): Redacted {
  const removed = new Set<keyof typeof REMOVED>();
  let text = input
    .replace(EMAIL, () => (removed.add("email"), REMOVED.email))
    .replace(SPELLED_EMAIL, () => (removed.add("email"), REMOVED.email))
    .replace(LINK, () => (removed.add("link"), REMOVED.link))
    .replace(CNIC, (m) => (looksLikeCnic(m) ? (removed.add("id"), REMOVED.id) : m));
  text = text.replace(NUMBER_RUN, (m) => {
    if (!looksLikePhone(m)) return m;
    removed.add("phone");
    return REMOVED.phone;
  });
  text = text.replace(ADDRESS, () => (removed.add("address"), REMOVED.address));
  return { text, removed: [...removed] };
}

function looksLikeCnic(match: string): boolean {
  // With dashes it's clearly an ID card; 13 digits in a row is too long for an answer.
  return /-/.test(match) || /^[0-9۰-۹٠-٩]{13}$/.test(match);
}
