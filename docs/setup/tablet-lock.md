# Locking a donated tablet to AI Tutor

This guide is for whoever hands out a donated tablet (Shahid, a teacher or a volunteer). When you finish, the tablet:

- opens only AI Tutor;
- needs a PIN before a child can leave the app;
- belongs to one named child; and
- can be found, locked or wiped if it is lost.

It uses **app pinning**, which is built into Android (5.0 and newer), so there is nothing to buy or install. It takes about 15 minutes per tablet.

Android menus differ a little between brands. Where Samsung uses different names, they are shown in *italics*.

---

## Part 1. Before you start

You need:

- the tablet, charged, and Wi-Fi to connect it to;
- the child's first name and class;
- a parent or guardian with you (they must agree when the child is added); and
- the **tablet register** (the table at the end of this guide), printed or on paper.

---

## Part 2. Set up the tablet

1. Turn the tablet on and follow Android's own setup.
   - When it asks for a Google account, use **one Google account for the donation programme**, not the child's or the parent's. Write the account in the register.
   - Skip anything optional (backups of other apps, extra offers).
2. Connect to Wi-Fi.
3. **Set a screen lock PIN.** App pinning needs it.
   1. Open **Settings**, then **Security**. *(Samsung: **Lock screen** → **Screen lock type**.)*
   2. Tap **Screen lock**, then **PIN**.
   3. Choose a 6-digit PIN. **The child and the parent must not know it.** Write it in the register (keep the register safe).
4. Turn on **Find My Device**, so a lost tablet can be found or wiped.
   1. Open **Settings**, then **Google**, then **Find My Device**.
   2. Turn it **On**.
5. Install AI Tutor.
   - From Google Play once it is there. Until then, use the test version: open https://github.com/storekeeperpra-711/ai-tutor/releases/tag/test-app on the tablet and download **ai-tutor-test-arm64.apk** (most tablets); if it won't install, use **ai-tutor-test-older-phones.apk**.
6. Update Android if the tablet asks to. Then turn off automatic app updates on mobile data: **Play Store** → your picture → **Settings** → **Network preferences** → **App download preference** → **Over Wi-Fi only**.

---

## Part 3. Add the one child

1. Open AI Tutor.
2. Tap the **family button** (top right), then sign in or create an account **with the parent's email**, so their child's progress is saved and comes back on a new tablet.
3. Go back to the home screen and tap **Add learner**.
4. Type the child's **first name only** and choose their class.
5. Choose a 4-digit **PIN for the child** if they share a home with brothers or sisters. Write it down and give it to the parent, not in the register.
6. Show the parent the **Privacy note** (it has a **Listen** button), then let **the parent** tick the box and tap **Save**.
7. In **Settings**, check:
   - **Data saver** is on (videos download on Wi-Fi only).
   - **Mithu's AI help**: on or off, as the parent chooses.
8. Tap **Settings** → **Downloads** and download the child's lessons while you are on Wi-Fi.

Only add this one child. A tablet belongs to one named child.

---

## Part 4. Turn on app pinning

1. Open **Settings**, then **Security**, then **Advanced** (or **More security settings**), then **App pinning**. *(Samsung: **Security and privacy** → **More security settings** → **Pin windows**.)*
   - If you can't find it, type **pin** in the search box at the top of Settings.
2. Turn **App pinning** **On**.
3. Turn on **Ask for PIN before unpinning** (it may say **Lock device when unpinning**). This is the most important switch: without it, any child can leave the app.

## Part 5. Pin AI Tutor

1. Open AI Tutor.
2. Open the **recent apps** screen:
   - with the 3 buttons at the bottom, tap the **square** button;
   - with gestures, swipe up from the bottom edge and hold for a moment, then let go.
3. At the top of the AI Tutor card, tap the **app icon** (the round picture above the card).
4. Tap **Pin** (*Samsung: **Pin this app***). Tap **Got it** if Android explains how to unpin.

The child can now use AI Tutor, but can't open other apps, the Play Store or Settings.

**Check it works:** press the **Home** button. The tablet should stay in AI Tutor and show a short message about unpinning.

## Part 6. How an adult unpins (for charging, updates or problems)

- With the 3 buttons: **touch and hold Back and the square button together**.
- With gestures: **swipe up from the bottom and hold**.
- Then type the **tablet PIN** from Part 2.

After you're done, pin AI Tutor again (Part 5). If the tablet restarts, it starts unpinned: an adult must pin it again. Ask the parent to call you if that happens, or teach a trusted adult at home the tablet PIN.

---

## Part 7. If a tablet is lost or stolen

Do these on the same day.

1. **Find, lock or wipe the tablet.** On any phone or computer, open https://www.google.com/android/find and sign in with the programme's Google account.
   - **Play sound** if it may be nearby.
   - **Secure device** to lock it and show a message ("This tablet belongs to the AI Tutor programme, please call …").
   - **Factory reset device** (erase) if it won't come back. This removes everything on it.
2. **Protect the child's account.** Shahid (or whoever runs the Firebase project) does this:
   1. Open https://console.firebase.google.com and choose the project.
   2. Go to **Authentication**, then **Users**, and find the parent's email.
   3. Tap the **⋮** at the end of the row, then **Reset password**. The parent gets an email to choose a new password.
   4. Once the password changes, the lost tablet is signed out the next time it goes online, and it stops receiving or sending the child's progress.
3. **Nothing is lost for the child.** Their progress is saved in the parent's account. On the new tablet or phone, sign in with the parent's email (Part 3, step 2) and it comes back.
4. Write what happened in the register.

What the lost tablet still holds: the child's first name, class, picture and progress, saved on the tablet. It holds no surname, address, phone number or photo of the child, because the app never asks for them.

---

## Part 8. When the tablet goes to a different child

1. Unpin (Part 6).
2. In AI Tutor, tap the **family button**, then the **bin** next to the old child, to remove them and their progress. Their progress stays safe in their parent's account if they move to another device.
3. Sign out of the old parent's account, then follow Part 3 for the new child.
4. Pin again (Part 5) and update the register.

---

## Tablet register

Keep one row per tablet. Store this somewhere safe (it holds the tablet PINs).

| Tablet (brand, model, serial number) | Child's first name and class | Parent's name and phone | Programme Google account | Tablet PIN | Date given | Notes (lost, returned, changed child) |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
