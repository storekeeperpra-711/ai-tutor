# Mithu's voice with Google Gemini

Status: Shahid chose Google's Gemini voice (2026-10-04). Step 1 done: samples in 4 voices (2026-10-05); Shahid asked for the voice closest to a human one, and **Sulafat** (Google: "warm") was picked. Step 2 (below) built: the workflow "Make Mithu's voice" runs every day at 14:00 Pakistan time.

**Free limit:** Gemini's free tier allows 10 recordings a day for `gemini-3.8-flash-tts`. Grade 9 has 25 Mithu lines (50 recordings in two languages), so making them all takes about 5 days. Step 2 runs once a day by itself and carries on where it stopped.

## Why

The phone's own voice sounds robotic, and many phones have no Urdu voice. Gemini's voices sound like a real person, and can be told how to speak ("a warm, kind teacher"). The free tier needs no bank card.

## How it will work

1. **Voice samples** (`tools/voice/make_voice.py sample`, workflow "Mithu voice samples"): two real Mithu lines, in Urdu and English, in 4 voices (Sulafat, Vindemiatrix, Achird, Sadaltager). Shahid listens and picks a voice. This also checks Urdu: Gemini's newest voice model doesn't list Urdu, though it finds the language by itself, so we listen before building the rest.
2. **Make every line once** (`tools/voice/make_voice.py make`, workflow "Make Mithu's voice", daily): makes each Mithu line in each language in Sulafat's voice (88 recordings today, Grade 9 first) and stores each one at once in Cloudflare KV (storage `ai-tutor-voice`, made by `tools/voice/kv.py` the first time), with an index of which recordings exist. Lines already made and unchanged are skipped, so it carries on the next day after the free limit and costs nothing once all are made; a changed line is made again. The AI server hands them out at `GET /v1/voice/index` and `GET /v1/voice/<file>` (`worker/src/voice.ts`), with no sign-in, since they are lesson content.
3. **The app downloads them**: when a lesson opens, the app fetches its Mithu recordings (about 4 KB a second of speech, so a lesson is about 100 KB), keeps them on the phone, and plays them with Mithu's beak following the voice. Data saver applies. With no recording, the phone's voice is used, as today.

No lesson format change: the app already looks for `<lesson>__<step>_<language>.m4a` recordings (Phase 7).

## Not included

- Only Mithu's lines are spoken, as today. Reading every question aloud would be a separate step.
- Mithu's live AI replies stay with the phone's voice: making them with Gemini on each reply would cost money per child.
