# tools

Python and Node helpers. Install the Python ones once with `pip install -r tools/requirements.txt`.

| Tool | What it does |
|---|---|
| `validate_lessons.py` | Checks lesson files against the schema and the rules a schema can't express (also that simulation, video and Lottie files exist, and that simulations make no network requests). |
| `video/make_video.py` | Makes a short explainer video from a scene script in `video/scripts/`, in English and Urdu, with WebVTT captions. Needs ffmpeg. Example: `python tools/video/make_video.py tools/video/scripts/fractions_roti.json` writes `assets/videos/fractions_roti_{en,ur}.{mp4,vtt}`. |
| `lottie/make_lottie.py` | Writes the small Lottie animations in `assets/lottie/` from code. |
| `firestore-rules/` | Firestore security rules tests on the emulator (`npm test` there). |

Tests: `python -m unittest discover -s tools -p 'test_*.py'`.

## Adding a video

1. Copy a script in `video/scripts/` and change the scenes. Each scene has `seconds`, a `draw` (one of the drawers in `make_video.py`: `title`, `rotis`, `equations`), its `params`, and a `caption` in `en` and `ur`. Keep the whole video under 2 minutes.
2. Run `make_video.py` on it, then watch both files.
3. Add a `video` step to the lesson with the file names, the captions and a `summary` (shown if the video can't play).

A new kind of picture needs a new drawer function: it gets the frame (with `t` going from 0 to 1 through the scene) and the scene's params.
