// Checks firestore.rules: each account sees only its own children's data,
// and student profiles hold only the minimal fields.
import { readFileSync } from 'node:fs';
import { after, before, beforeEach, test } from 'node:test';
import {
  assertFails,
  assertSucceeds,
  initializeTestEnvironment,
} from '@firebase/rules-unit-testing';
import {
  deleteDoc,
  doc,
  getDoc,
  setDoc,
  Timestamp,
} from 'firebase/firestore';

let env;

before(async () => {
  env = await initializeTestEnvironment({
    projectId: 'demo-ai-tutor',
    firestore: { rules: readFileSync('../../firestore.rules', 'utf8') },
  });
});

after(() => env.cleanup());
beforeEach(() => env.clearFirestore());

const student = {
  first_name: 'Ayesha',
  grade: 6,
  avatar: 'star',
  pin_hash: null,
  created_at: Timestamp.now(),
  consent_at: Timestamp.now(),
};

const db = (uid) =>
  uid ? env.authenticatedContext(uid).firestore() : env.unauthenticatedContext().firestore();

test('an account can save and read its own learners and progress', async () => {
  const mine = db('phone1');
  await assertSucceeds(setDoc(doc(mine, 'accounts/phone1'), { role: 'device' }));
  await assertSucceeds(setDoc(doc(mine, 'accounts/phone1/students/s1'), student));
  await assertSucceeds(
    setDoc(doc(mine, 'accounts/phone1/students/s1/progress/lesson-a'), {
      next_step: 3,
      steps: { s1: { correct: true } },
    }),
  );
  await assertSucceeds(getDoc(doc(mine, 'accounts/phone1/students/s1/progress/lesson-a')));
  await assertSucceeds(
    setDoc(doc(mine, 'accounts/phone1/students/s1/skills/maths.fractions.divide_by_fraction'), {
      skill: 'maths.fractions.divide_by_fraction',
      needs_help: false,
    }),
  );
  await assertSucceeds(deleteDoc(doc(mine, 'accounts/phone1/students/s1')));
});

test("an account can't see or change another account's children", async () => {
  await env.withSecurityRulesDisabled(async (ctx) => {
    await setDoc(doc(ctx.firestore(), 'accounts/phone1/students/s1'), student);
  });
  const other = db('phone2');
  await assertFails(getDoc(doc(other, 'accounts/phone1/students/s1')));
  await assertFails(getDoc(doc(other, 'accounts/phone1/students/s1/progress/lesson-a')));
  await assertFails(getDoc(doc(other, 'accounts/phone1/students/s1/skills/maths.x.y')));
  await assertFails(setDoc(doc(other, 'accounts/phone1/students/s1/skills/maths.x.y'), { a: 1 }));
  await assertFails(setDoc(doc(other, 'accounts/phone1/students/s2'), student));
  await assertFails(deleteDoc(doc(other, 'accounts/phone1/students/s1')));
});

test('nothing is readable without signing in', async () => {
  const anon = db(null);
  await assertFails(getDoc(doc(anon, 'accounts/phone1')));
  await assertFails(getDoc(doc(anon, 'accounts/phone1/students/s1')));
});

test('student profiles hold only the minimal fields', async () => {
  const mine = db('phone1');
  const path = 'accounts/phone1/students/s1';
  await assertFails(setDoc(doc(mine, path), { ...student, surname: 'Khan' }));
  await assertFails(setDoc(doc(mine, path), { ...student, phone: '0300' }));
  await assertFails(setDoc(doc(mine, path), { ...student, first_name: '' }));
  await assertFails(setDoc(doc(mine, path), { ...student, first_name: 'x'.repeat(31) }));
  await assertFails(setDoc(doc(mine, path), { ...student, grade: 'six' }));
  const { consent_at, ...noConsent } = student;
  await assertFails(setDoc(doc(mine, path), noConsent));
});

test('the account role must be device, parent or teacher', async () => {
  const mine = db('phone1');
  await assertSucceeds(setDoc(doc(mine, 'accounts/phone1'), { role: 'parent' }));
  await assertFails(setDoc(doc(mine, 'accounts/phone1'), { role: 'admin' }));
});

test('other collections are closed', async () => {
  await assertFails(setDoc(doc(db('phone1'), 'lessons/x'), { a: 1 }));
  await assertFails(getDoc(doc(db('phone1'), 'lessons/x')));
});

// Phase 6: AI queue, reports, and server-only AI collections.

const queued = (uid, studentId = 's1') => ({
  uid,
  student_id: studentId,
  lesson_id: 'g6-maths-02-dividing-fractions',
  step_id: 's6_explain_why',
  lang: 'ur',
  answer: 'ہر روٹی کے دو آدھے',
  created_at: Timestamp.now(),
  status: 'waiting',
});
const QID = 'Ab3dEf6hIj9kLm2nOp5q';

async function withStudent(uid) {
  await env.withSecurityRulesDisabled((ctx) =>
    setDoc(doc(ctx.firestore(), `accounts/${uid}/students/s1`), student),
  );
}

test('a phone can queue an answer for its own student and read it back', async () => {
  await withStudent('phone1');
  const mine = db('phone1');
  await assertSucceeds(setDoc(doc(mine, `ai_queue/${QID}`), queued('phone1')));
  await assertSucceeds(setDoc(doc(mine, `ai_queue/${QID}`), queued('phone1')));
  await assertSucceeds(getDoc(doc(mine, `ai_queue/${QID}`)));
  await assertFails(getDoc(doc(db('phone2'), `ai_queue/${QID}`)));
});

test('queued answers are checked', async () => {
  await withStudent('phone1');
  const mine = db('phone1');
  await assertFails(setDoc(doc(mine, `ai_queue/${QID}`), queued('phone2')));
  await assertFails(setDoc(doc(mine, `ai_queue/${QID}`), queued('phone1', 'not-my-child')));
  await assertFails(setDoc(doc(mine, `ai_queue/${QID}`), { ...queued('phone1'), status: 'answered' }));
  await assertFails(setDoc(doc(mine, `ai_queue/${QID}`), { ...queued('phone1'), reply: 'Great!' }));
  await assertFails(setDoc(doc(mine, `ai_queue/${QID}`), { ...queued('phone1'), answer: 'x'.repeat(1501) }));
  await assertFails(setDoc(doc(mine, 'ai_queue/short'), queued('phone1')));
  await assertFails(setDoc(doc(db(null), `ai_queue/${QID}`), queued('phone1')));
});

test('a phone cannot change an answer after the server took it', async () => {
  await withStudent('phone1');
  await env.withSecurityRulesDisabled((ctx) =>
    setDoc(doc(ctx.firestore(), `ai_queue/${QID}`), { ...queued('phone1'), status: 'answered', reply: 'Well done' }),
  );
  await assertFails(setDoc(doc(db('phone1'), `ai_queue/${QID}`), queued('phone1')));
  await assertSucceeds(getDoc(doc(db('phone1'), `ai_queue/${QID}`)));
});

test('parents read weekly reports but only the server writes them', async () => {
  await withStudent('phone1');
  const path = 'accounts/phone1/students/s1/reports/2026-10-04';
  await env.withSecurityRulesDisabled((ctx) => setDoc(doc(ctx.firestore(), path), { note: { en: 'Good week' } }));
  await assertSucceeds(getDoc(doc(db('phone1'), path)));
  await assertFails(getDoc(doc(db('phone2'), path)));
  await assertFails(setDoc(doc(db('phone1'), path), { note: { en: 'Best week ever' } }));
});

test('AI usage, logs and batches are server only', async () => {
  const mine = db('phone1');
  for (const path of ['ai_usage/2026-10-04_s1', 'ai_usage_total/2026-10-04', 'ai_logs/x', 'ai_batches/b1']) {
    await assertFails(getDoc(doc(mine, path)));
    await assertFails(setDoc(doc(mine, path), { cost_usd: 0 }));
  }
});
