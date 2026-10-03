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
  addDoc,
  collection,
  getDoc,
  getDocs,
  serverTimestamp,
  setDoc,
  updateDoc,
  writeBatch,
  query,
  where,
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

test('signed-in phones read published lessons but only the upload tool writes them', async () => {
  await env.withSecurityRulesDisabled(async (ctx) => {
    await setDoc(doc(ctx.firestore(), 'lesson_catalog/current'), { lessons: {} });
    await setDoc(doc(ctx.firestore(), 'published_lessons/g9-maths-05-x'), { version: 1, content: '{}' });
  });
  for (const path of ['lesson_catalog/current', 'published_lessons/g9-maths-05-x']) {
    await assertSucceeds(getDoc(doc(db('phone1'), path)));
    await assertFails(getDoc(doc(db(null), path)));
    await assertFails(setDoc(doc(db('phone1'), path), { version: 99 }));
  }
  await assertFails(getDoc(doc(db('phone1'), 'lesson_reviews/g9-maths-05-x')));
});

describeReviews();
describeClasses();

function describeReviews() {
  const reviewer = (email, verified = true) =>
    env.authenticatedContext(`uid-${email}`, { email, email_verified: verified }).firestore();
  const HASH = 'aaaaaaaaaaaaaaaa';

  async function seed() {
    await env.withSecurityRulesDisabled(async (ctx) => {
      await setDoc(doc(ctx.firestore(), 'config/reviewers'), { emails: ['teacher@school.pk'] });
      await setDoc(doc(ctx.firestore(), 'lesson_reviews/g9-maths-05-x'), {
        hash: HASH,
        version: 1,
        status: 'in_review',
      });
    });
  }

  const decision = (status, approvedHash = HASH) => ({
    status,
    approved_hash: approvedHash,
    reviewer: 'teacher@school.pk',
    decided_at: serverTimestamp(),
  });

  const note = (overrides = {}) => ({
    step_id: 's1',
    text: 'Use the Urdu word for equation here.',
    author: 'teacher@school.pk',
    hash: HASH,
    created_at: serverTimestamp(),
    ...overrides,
  });

  test('a listed teacher with a verified email reviews lessons', async () => {
    await seed();
    const teacher = reviewer('Teacher@School.pk');
    await assertSucceeds(getDoc(doc(teacher, 'config/reviewers')));
    await assertSucceeds(getDocs(collection(teacher, 'lesson_reviews')));
    await assertSucceeds(addDoc(collection(teacher, 'lesson_reviews/g9-maths-05-x/notes'), note()));
    await assertSucceeds(getDocs(collection(teacher, 'lesson_reviews/g9-maths-05-x/notes')));
    await assertSucceeds(updateDoc(doc(teacher, 'lesson_reviews/g9-maths-05-x'), decision('approved')));
  });

  test('nobody else can review, even with the same email unverified', async () => {
    await seed();
    for (const someone of [reviewer('teacher@school.pk', false), reviewer('other@school.pk'), db('phone1')]) {
      await assertFails(getDoc(doc(someone, 'config/reviewers')));
      await assertFails(getDoc(doc(someone, 'lesson_reviews/g9-maths-05-x')));
      await assertFails(updateDoc(doc(someone, 'lesson_reviews/g9-maths-05-x'), decision('approved')));
      await assertFails(addDoc(collection(someone, 'lesson_reviews/g9-maths-05-x/notes'), note()));
    }
  });

  test('a reviewer approves only the version they saw, and only decides', async () => {
    await seed();
    const teacher = reviewer('teacher@school.pk');
    const review = doc(teacher, 'lesson_reviews/g9-maths-05-x');
    await assertFails(updateDoc(review, decision('approved', 'bbbbbbbbbbbbbbbb')));
    await assertFails(updateDoc(review, { ...decision('approved'), hash: 'bbbbbbbbbbbbbbbb' }));
    await assertFails(updateDoc(review, { ...decision('approved'), reviewer: 'shahid@x.pk' }));
    await assertFails(updateDoc(review, { ...decision('published') }));
    await assertFails(setDoc(doc(teacher, 'lesson_reviews/new-lesson'), decision('approved')));
    await assertFails(setDoc(doc(teacher, 'config/reviewers'), { emails: ['me@x.pk'] }));
    await assertSucceeds(updateDoc(review, decision('changes_requested')));
  });

  test('notes are checked', async () => {
    await seed();
    const notes = collection(reviewer('teacher@school.pk'), 'lesson_reviews/g9-maths-05-x/notes');
    await assertFails(addDoc(notes, note({ text: '' })));
    await assertFails(addDoc(notes, note({ text: 'x'.repeat(2001) })));
    await assertFails(addDoc(notes, note({ author: 'someone@else.pk' })));
    await assertFails(addDoc(notes, note({ hash: 'bbbbbbbbbbbbbbbb' })));
    await assertFails(addDoc(notes, note({ extra: true })));
  });
}

// Phase 9: classes, class codes, children's summaries and assigned lessons.
function describeClasses() {
  const CODE = 'ABC234';

  async function teacherAccount(uid = 'teacher1') {
    await env.withSecurityRulesDisabled((ctx) =>
      setDoc(doc(ctx.firestore(), `accounts/${uid}`), { role: 'teacher' }),
    );
  }

  function createClass(firestore, { uid = 'teacher1', id = 'class1', code = CODE, name = '9 A' } = {}) {
    const batch = writeBatch(firestore);
    batch.set(doc(firestore, `classes/${id}`), {
      teacher_uid: uid,
      name,
      code,
      created_at: serverTimestamp(),
    });
    batch.set(doc(firestore, `class_codes/${code}`), { class_id: id, name });
    return batch.commit();
  }

  async function seedClass() {
    await teacherAccount();
    await createClass(db('teacher1'));
  }

  const member = (uid, studentId = 's1', overrides = {}) => ({
    uid,
    student_id: studentId,
    first_name: 'Ayesha',
    grade: 9,
    joined_at: Timestamp.now(),
    updated_at: serverTimestamp(),
    skills: [{ skill: 'maths.unit5.x', level: 'learning', needs_help: false }],
    misconceptions: [],
    lessons: [],
    ...overrides,
  });

  function join(firestore, uid, studentId = 's1', overrides = {}) {
    const batch = writeBatch(firestore);
    batch.set(doc(firestore, `classes/class1/families/${uid}`), { joined_at: serverTimestamp() });
    batch.set(doc(firestore, `classes/class1/members/${uid}_${studentId}`), member(uid, studentId, overrides));
    return batch.commit();
  }

  test('a teacher creates a class with its code and lists their classes', async () => {
    await teacherAccount();
    const teacher = db('teacher1');
    await assertSucceeds(createClass(teacher));
    await assertSucceeds(getDoc(doc(teacher, 'classes/class1')));
    await assertSucceeds(getDocs(query(collection(teacher, 'classes'), where('teacher_uid', '==', 'teacher1'))));
  });

  test('only a teacher account creates classes, and a code is used once', async () => {
    await assertFails(createClass(db('phone1'), { uid: 'phone1' }));
    await teacherAccount();
    await teacherAccount('teacher2');
    await assertSucceeds(createClass(db('teacher1')));
    // The same code for another class is refused.
    await assertFails(createClass(db('teacher2'), { uid: 'teacher2', id: 'class2' }));
    // A class can't be made without its code, or for another teacher.
    await assertFails(
      setDoc(doc(db('teacher2'), 'classes/class3'), {
        teacher_uid: 'teacher2',
        name: 'x',
        code: 'QQQQQQ',
        created_at: serverTimestamp(),
      }),
    );
    await assertFails(createClass(db('teacher2'), { uid: 'teacher1', id: 'class4', code: 'WWWWWW' }));
    await assertFails(createClass(db('teacher2'), { uid: 'teacher2', id: 'class5', code: 'abc234' }));
    await assertFails(createClass(db('teacher2'), { uid: 'teacher2', id: 'class6', code: 'ZZZZZZ', name: '' }));
  });

  test('anyone signed in looks up one code, but nobody lists codes or reads other classes', async () => {
    await seedClass();
    await assertSucceeds(getDoc(doc(db('phone1'), `class_codes/${CODE}`)));
    await assertFails(getDoc(doc(db(null), `class_codes/${CODE}`)));
    await assertFails(getDocs(collection(db('phone1'), 'class_codes')));
    await assertFails(getDoc(doc(db('phone1'), 'classes/class1')));
    await assertFails(getDocs(query(collection(db('phone1'), 'classes'), where('teacher_uid', '==', 'teacher1'))));
    await assertFails(getDocs(collection(db('teacher2'), 'classes/class1/members')));
  });

  test('a family joins a child, and the teacher sees the summary', async () => {
    await seedClass();
    const family = db('phone1');
    await assertSucceeds(join(family, 'phone1'));
    await assertSucceeds(getDoc(doc(family, 'classes/class1')));
    await assertSucceeds(getDoc(doc(family, 'classes/class1/members/phone1_s1')));
    await assertSucceeds(setDoc(doc(family, 'classes/class1/members/phone1_s1'), member('phone1')));
    const teacher = db('teacher1');
    await assertSucceeds(getDocs(collection(teacher, 'classes/class1/members')));
    await assertSucceeds(getDocs(collection(teacher, 'classes/class1/families')));
    // Another family can't read it.
    await assertFails(getDoc(doc(db('phone2'), 'classes/class1/members/phone1_s1')));
  });

  test("summaries are checked and can't be written for another family", async () => {
    await seedClass();
    const family = db('phone1');
    await assertFails(join(family, 'phone2'));
    await assertFails(join(family, 'phone1', 's1', { first_name: '' }));
    await assertFails(join(family, 'phone1', 's1', { first_name: 'x'.repeat(31) }));
    await assertFails(join(family, 'phone1', 's1', { pin_hash: 'abc' }));
    await assertFails(join(family, 'phone1', 's1', { surname: 'Khan' }));
    await assertFails(join(family, 'phone1', 's1', { grade: 'nine' }));
    // Without joining the class first.
    await assertFails(setDoc(doc(family, 'classes/class1/members/phone1_s1'), member('phone1')));
    // The id must match the family and child.
    await assertSucceeds(join(family, 'phone1'));
    await assertFails(setDoc(doc(family, 'classes/class1/members/phone1_s2'), member('phone1', 's1')));
    // Not into a class that doesn't exist.
    const batch = writeBatch(family);
    batch.set(doc(family, 'classes/nope/families/phone1'), { joined_at: serverTimestamp() });
    await assertFails(batch.commit());
  });

  test('a family leaves, and the teacher can remove a child', async () => {
    await seedClass();
    await join(db('phone1'), 'phone1');
    await join(db('phone2'), 'phone2', 's9');
    await assertFails(deleteDoc(doc(db('phone2'), 'classes/class1/members/phone1_s1')));
    await assertSucceeds(deleteDoc(doc(db('phone1'), 'classes/class1/members/phone1_s1')));
    await assertSucceeds(deleteDoc(doc(db('phone1'), 'classes/class1/families/phone1')));
    await assertSucceeds(deleteDoc(doc(db('teacher1'), 'classes/class1/members/phone2_s9')));
  });

  test('the teacher assigns lessons, families in the class read them', async () => {
    await seedClass();
    await join(db('phone1'), 'phone1');
    const teacher = db('teacher1');
    const lesson = {
      lesson_id: 'g9-maths-05-feasible-region',
      due: Timestamp.now(),
      created_at: serverTimestamp(),
    };
    await assertSucceeds(setDoc(doc(teacher, 'classes/class1/assignments/a1'), lesson));
    await assertSucceeds(setDoc(doc(teacher, 'classes/class1/assignments/a2'), { ...lesson, due: null }));
    await assertFails(setDoc(doc(teacher, 'classes/class1/assignments/a3'), { ...lesson, extra: 1 }));
    await assertFails(setDoc(doc(teacher, 'classes/class1/assignments/a4'), { ...lesson, lesson_id: '' }));
    await assertSucceeds(getDocs(collection(db('phone1'), 'classes/class1/assignments')));
    await assertFails(getDocs(collection(db('phone2'), 'classes/class1/assignments')));
    await assertFails(setDoc(doc(db('phone1'), 'classes/class1/assignments/a5'), lesson));
    await assertFails(deleteDoc(doc(db('phone1'), 'classes/class1/assignments/a1')));
    await assertSucceeds(deleteDoc(doc(teacher, 'classes/class1/assignments/a1')));
  });

  test('the teacher deletes the class with its code; then the family can no longer write', async () => {
    await seedClass();
    await join(db('phone1'), 'phone1');
    await assertFails(deleteDoc(doc(db('phone1'), 'classes/class1')));
    await assertFails(deleteDoc(doc(db('teacher1'), `class_codes/${CODE}`)));
    const teacher = db('teacher1');
    const batch = writeBatch(teacher);
    batch.delete(doc(teacher, 'classes/class1/members/phone1_s1'));
    batch.delete(doc(teacher, 'classes/class1/families/phone1'));
    batch.delete(doc(teacher, `class_codes/${CODE}`));
    batch.delete(doc(teacher, 'classes/class1'));
    await assertSucceeds(batch.commit());
    await assertFails(setDoc(doc(db('phone1'), 'classes/class1/members/phone1_s1'), member('phone1')));
  });
}
