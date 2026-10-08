# One-week test on the Infinix Hot 10

This is a checklist for Shahid. For one week, use AI Tutor every day on a cheap phone, the way a family would. At the end, the numbers below show whether the app is light enough for the phones families really have.

The test phone is an **Infinix Hot 10** (Android 10 or 11, XOS, 3 or 4 GB memory). It is a newer phone type, so it uses the `arm64-v8a` app file.

Print this page, or copy the tables into a notebook.

---

## Day 0. Get ready (about 20 minutes)

1. **Charge the phone to 100%.**
2. **Install the test app.**
   1. On the phone, open this page in Chrome: https://github.com/storekeeperpra-711/ai-tutor/releases/tag/test-app
   2. Under **Assets**, tap **ai-tutor-test-arm64.apk** to download it. (It is always the newest test app.)
   3. When the download finishes, tap **Open** (or find it in **Files** → **Downloads**).
   4. On the phone, tap the file. If Android asks, allow **Install unknown apps** for that app, then tap **Install**.
3. **Stop XOS from closing the app.** Infinix phones close apps in the background to save battery, which can stop progress from saving.
   1. Open **Settings** → **Battery** (or **Power Marathon / Battery manager**). If you can't find it, type **battery** in the search box at the top of Settings.
   2. Find **App launch** or **Auto-start management**, find **AI Tutor**, and allow it.
   3. Don't use **Phone Master** to "clean" or "boost" during the test week.
4. **Reset Android's battery numbers**, so the week starts fresh: unplug the charger when it reaches 100%. Android's battery page counts from the last full charge.
5. **Set the phone up like a family would.**
   - Turn **mobile data on** and use it for at least part of every day (Wi-Fi for the rest is fine).
   - In AI Tutor, add one learner, a real child if one can use it, or a pretend one (any first name, any class).
   - Leave **Data saver** on and **Mithu's AI help** on.
6. **Write the starting numbers** in the "Day 0" row of the table below. To open the **Phone check** screen: open **Settings** in AI Tutor and **press and hold the word "Settings"** at the top.

---

## Every day (about 20 to 30 minutes)

Use the app as a child would, and try a bit of everything over the week:

- [ ] Do at least one lesson to the end.
- [ ] Watch a video step.
- [ ] Ask Mithu for help at least once (a hint, or "explain in your own words").
- [ ] One day: do a photo step (take a picture of working on paper).
- [ ] One day: turn mobile data and Wi-Fi **off**, do a lesson, then turn them back on. Progress should not be lost.
- [ ] One day: switch to another app (WhatsApp, the camera) in the middle of a video, then come back. The video should be paused at the same place.
- [ ] One day: turn the phone off and on, then open the app. It should open where you were.
- [ ] One day: let a child under 7 try it, with you next to them, if you can.

At the end of each day:

1. Open **Phone check** (Settings → press and hold **"Settings"**) **before you close the app**.
2. Write the numbers in today's row.
3. Write anything strange in **Notes**: slow screens, the phone getting hot, a crash, a wrong answer from Mithu, words that are hard to read.

| Day | Memory now | Most memory used | Saved videos | Mobile data, last 7 days | Wi-Fi data, last 7 days | Crashes, last 7 days | Battery % left at night | Notes |
|---|---|---|---|---|---|---|---|---|
| 0 | | | | | | | 100% | |
| 1 | | | | | | | | |
| 2 | | | | | | | | |
| 3 | | | | | | | | |
| 4 | | | | | | | | |
| 5 | | | | | | | | |
| 6 | | | | | | | | |
| 7 | | | | | | | | |

---

## Day 7. Read the results (about 15 minutes)

1. **Phone check:** write the Day 7 row.
2. **Android's battery page:** **Settings** → **Battery** → **Battery usage** (or **Power consumption ranking**). Find **AI Tutor** and write:
   - AI Tutor's share of the battery: ______ %
3. **Android's data page:** **Settings** → **Network & internet** (or **Mobile network**) → **Data usage** → **Mobile data usage**. Find **AI Tutor** and write:
   - Mobile data this month: ______ MB
4. **Storage:** **Settings** → **Apps** → **AI Tutor** → **Storage**. Write:
   - App size: ______ MB    Data: ______ MB    Cache: ______ MB

### What "good" looks like

| What | Good | Tell Claude if |
|---|---|---|
| Most memory used | under 250 MB | over 350 MB |
| Saved videos | under 300 MB (the app's own limit) | over 300 MB |
| Mobile data, last 7 days | under 50 MB | over 100 MB |
| Crashes, last 7 days | 0 | 1 or more |
| AI Tutor's share of the battery | under 10% | over 20% |
| App size + data | under 200 MB | over 400 MB |
| Screens | open in under 2 seconds | anything feels slow or freezes |

## Send the results

Take a photo of the filled-in tables and send it in this thread, with anything from **Notes**. Claude will check the numbers, look at any crash in Firebase (Crashlytics), and fix what needs fixing.
