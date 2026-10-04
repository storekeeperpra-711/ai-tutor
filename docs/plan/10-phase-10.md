# Phase 10 plan: hardening

Status: approved 2026-10-04 (Crashlytics yes, Data saver on by default). Step 1 built.
Spec: [master-prompt.md](../master-prompt.md), Part F, Phase 10.

**Goal:** reliable, light and safe on real devices.
**Done when:** a full week of use on the cheap phone shows no crashes, acceptable battery and data use, and costs within budget.

## What exists now

- Only one simulation (WebView) or video is open at a time, and it is closed when the step ends.
- Linked videos are downloaded once and kept (media cache), but there is no size limit, no Wi-Fi-only choice, and no screen showing what is stored.
- New lessons download automatically whenever the phone is online.
- Parents agree before a child is added and before a child joins a class. A child can be deleted with all their data.
- The AI server (Cloudflare Worker) has daily limits per child, short replies, fallbacks, a cost dashboard, and logs every AI call for 90 days for review.
- Nothing reports crashes, and nothing measures battery or data use.

## How it will work

### 1. Light on the cheap phone

- Put a size limit on stored videos (default 300 MB). When the limit is passed, the oldest videos are removed first.
- Play videos at the smallest size the lesson offers, and stop and free a video or simulation as soon as the app goes into the background.
- Build the Android app as one small file per phone type (split APKs), so each phone downloads less.
- Add a hidden **Phone check** screen (for Shahid and testers). It shows app memory, storage used, data used this week, and crashes this week.

### 2. Data saver and downloads

- A **Data saver** switch in Settings, on by default. While it is on, videos and new lessons download only on Wi-Fi, or when the parent taps Download.
- A **Downloads** screen lists each unit with its size. A parent can download a unit before going somewhere without signal, or remove it to free space.
- The app counts the data it uses itself, so the Phone check screen and the parent can see it.

### 3. Privacy and safety review

- Write a plain privacy note in English and Urdu (with Listen): what is stored, where, who can see it, and how long it is kept. Show it when a parent first sets up the app and in Settings.
- Check every consent step again (adding a child, joining a class, AI features) and fix any gaps.
- Review every AI prompt in the Worker. Add a fixed set of test messages (worrying messages, off-topic questions, attempts to share a phone number or address, rude words). Run them once against the dev Worker and save the results for Shahid to read. This costs a few cents of AI use.
- Before anything is sent to Claude, the Worker removes phone numbers, emails and addresses from what the child typed.

### 4. Crash reporting and privacy-safe numbers

- **Firebase Crashlytics** reports app crashes. It is free on the Spark plan. It gets no names and no account emails, only the phone model and where the app crashed.
- No Google Analytics, because it tracks devices and is not right for children.
- Learning numbers come from data we already have: once a day, the Worker counts lessons started and finished, questions answered, hints used and AI calls. It stores only totals, never per-child data, and the admin page shows them.

### 5. Kiosk guide for donated tablets

- A click-by-click guide with pictures for locking a tablet to the app with Android's built-in **app pinning**. It also covers registering a tablet to one named child and what to do if it is lost.

### 6. The one-week test

- A test checklist for Shahid: install on the cheap phone, use it every day for a week, and read the Phone check screen and Android's battery page at the end.

## Questions for Shahid

1. Use Firebase Crashlytics for crash reports? (Recommended: yes. It's free and gets no personal data.)
2. Keep Data saver on by default? (Recommended: yes. Most families use mobile data.)
3. Which cheap phone will you test on? (Brand and model, if you know it.)

## Cost and risk

- Crashlytics and the daily totals stay within the free plans.
- The AI safety test is a one-off run of about 40 short messages, costing a few cents.
- Risk: Google Play's rules for apps used by children. Crashlytics with no advertising ID and no Analytics is allowed, but I'll note it in the privacy note.

## Step 1 as built

- `lib/media/media_cache.dart`: saved media lives in its own cache (`lessonMedia`) with a 300 MB limit. After each download, the files used longest ago are removed until it fits; the lesson open now is never removed.
- `lib/app/memory_limits.dart`: pictures in memory are capped at 40 MB (Flutter's default is 100 MB) and cleared when Android reports low memory. Firestore's offline copy is capped at 40 MB.
- `video_step_view.dart`: when the app goes into the background, the video player is closed to free memory. When the app comes back, the video loads again at the same place, paused.
- Simulations need no change: they animate only while a ball is falling, and Android stops WebView animation while the app is hidden.
- The lesson format has one video file per language, so "play the smallest size" needs a second, smaller file per video. That is a change to the lesson schema, so I'll ask before doing it. For now, videos should be made small (360p) when they are created.
- CI's APK job (on main, or run by hand) also builds small release APKs, one for older phones (armeabi-v7a) and one for newer phones (arm64-v8a), and lists their sizes.
- Phone check screen: long-press the word "Settings" at the top of the Settings screen. It shows memory now and at most, pictures in memory, saved videos (with a button to remove them) and downloaded lessons. Data used (step 2) and crashes (step 4) will be added there.
