# Mithu's voice with Google Gemini

Status: Shahid chose Google's Gemini voice (2026-10-04). Step 1 (voice samples) in progress.

## Why

The phone's own voice sounds robotic, and many phones have no Urdu voice. Gemini's voices sound like a real person, and can be told how to speak ("a warm, kind teacher"). The free tier needs no bank card.

## How it will work

1. **Voice samples** (`tools/voice/make_voice.py sample`, workflow "Mithu voice samples"): two real Mithu lines, in Urdu and English, in 4 voices (Sulafat, Vindemiatrix, Achird, Sadaltager). Shahid listens and picks a voice. This also checks Urdu: Gemini's newest voice model doesn't list Urdu, though it finds the language by itself, so we listen before building the rest.
2. **Make every line once** (after the voice is chosen): a workflow makes each Mithu line in each language (46 lines today, about 5,800 characters; 25 in Grade 9) and stores the files in Cloudflare KV through the AI server. Lines that haven't changed are skipped, so it costs nothing to run again after a lesson fix.
3. **The app downloads them**: when a lesson opens, the app fetches its Mithu recordings (about 4 KB a second of speech, so a lesson is about 100 KB), keeps them on the phone, and plays them with Mithu's beak following the voice. Data saver applies. With no recording, the phone's voice is used, as today.

No lesson format change: the app already looks for `<lesson>__<step>_<language>.m4a` recordings (Phase 7).

## Not included

- Only Mithu's lines are spoken, as today. Reading every question aloud would be a separate step.
- Mithu's live AI replies stay with the phone's voice: making them with Gemini on each reply would cost money per child.
