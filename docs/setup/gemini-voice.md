# Mithu's voice: setting up Google Gemini

Mithu's lines are spoken with Google's Gemini voice. The audio is made **once**, in GitHub, and saved; children's phones only play the saved files. It uses Gemini's free tier, so there is no bill and no bank card.

You do this once. It takes about 5 minutes.

## 1. Make a Gemini key

1. On a computer (or the phone's Chrome), open https://aistudio.google.com/apikey
2. Sign in with your Google account. Accept the terms if asked.
3. Tap **Create API key**. If it asks for a project, choose **Create API key in new project**.
4. A long key appears (it starts with `AIza`). Tap **Copy**.

**Don't send the key to anyone, not even in this chat.** It only goes into GitHub, in the next step.

## 2. Put the key in GitHub

1. Open https://github.com/storekeeperpra-711/ai-tutor/settings/secrets/actions
2. Tap **New repository secret**.
3. **Name:** `GEMINI_API_KEY`
4. **Secret:** paste the key.
5. Tap **Add secret**.

## 3. Listen to the samples

1. Open https://github.com/storekeeperpra-711/ai-tutor/actions/workflows/voice-sample.yml
2. Tap **Run workflow**, then the green **Run workflow** button.
3. Wait about 5 minutes, until the run has a green ✓. Tap the run.
4. At the bottom, under **Artifacts**, tap **mithu-voice-samples**. A zip downloads.
5. Unzip it and play the files. Each name says the voice, the line and the language: `Sulafat_1_ur.m4a` is the voice Sulafat saying line 1 in Urdu.
6. Say in the thread which voice sounds best for Urdu and for English (they can be different).

## If something goes wrong

- **"GEMINI_API_KEY is missing"**: step 2 wasn't saved. Check the name is exactly `GEMINI_API_KEY`.
- **A run that stops early** with "free daily limit": Gemini's free tier makes about **10 recordings a day**. The files made so far are in the zip. The next day, run it again and type only the voices still missing in the **voices** box.
- **"Gemini said 400" or "403"**: the key was copied wrongly. Make a new key (step 1) and replace the secret (step 2: tap the secret, then **Update**).
