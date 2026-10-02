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
  await assertSucceeds(deleteDoc(doc(mine, 'accounts/phone1/students/s1')));
});

test("an account can't see or change another account's children", async () => {
  await env.withSecurityRulesDisabled(async (ctx) => {
    await setDoc(doc(ctx.firestore(), 'accounts/phone1/students/s1'), student);
  });
  const other = db('phone2');
  await assertFails(getDoc(doc(other, 'accounts/phone1/students/s1')));
  await assertFails(getDoc(doc(other, 'accounts/phone1/students/s1/progress/lesson-a')));
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
