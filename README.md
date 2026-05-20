![Rock Paper Scissors AI banner](banner.png)

# Webcam Rock Paper Scissors

A classroom-friendly Python activity that turns a webcam into a rock-paper-scissors game.

This branch is the guided workshop version. The app is mostly complete, but a few small `TODO` sections are left for students to finish during the activity.

Follow [TUTORIAL.md](TUTORIAL.md) for the 45-minute step-by-step lesson. A finished fallback version is kept on the `complete-solution` branch so the class has a safety net if a machine or group gets stuck.

## Setup

Use Python 3.11 or 3.12.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/main.py
```

On Windows:

```bat
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python src\main.py
```

You can also run `./start.sh` on macOS/Linux or `start.bat` on Windows after installing the requirements.

If you previously installed the dependencies and see `AttributeError: module 'mediapipe' has no attribute 'solutions'`, run `pip install -r requirements.txt` again. The requirements file pins MediaPipe to a classroom-compatible version that still supports the simple `mp.solutions` API.

## Workshop Flow

1. Activate the webcam feed.
2. Draw hand landmarks.
3. Count extended fingers.
4. Classify rock, paper, and scissors.
5. Generate the computer move.
6. Decide the winner and update the score.

The starting point runs before any TODOs are completed, but it will print a helpful camera message until students activate the webcam feed.

## Complete Solution Fallback

To switch to the finished version:

```bash
git checkout complete-solution
python src/main.py
```

To return to the workshop starter:

```bash
git checkout main
```
