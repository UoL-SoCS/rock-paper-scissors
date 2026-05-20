![Rock, Paper, Scissors, AI! banner](banner.png)

# Rock, Paper, Scissors, AI!

A classroom-friendly Python activity that turns a webcam into a game of Rock, Paper, Scissors, AI!

This repository has two useful branches:

- `main`: the guided workshop version, with a few small `TODO` sections to complete during the activity
- `complete-solution`: the finished fallback version, ready to run if you get stuck or want to compare your work
- `multiplayer`: a two-player version with a split screen, countdown, and player-vs-player scoring

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

## Guided Tutorial

On the `main` branch, follow `TUTORIAL.md` for the 45-minute step-by-step lesson.

1. Activate the webcam feed.
2. Draw hand landmarks.
3. Count extended fingers.
4. Classify rock, paper, and scissors.
5. Generate the computer move.
6. Decide the winner and update the score.

The `main` starting point runs before any TODOs are completed, but it will print a helpful camera message until you activate the webcam feed.

## Controls

- Show a rock, paper, or scissors gesture to the camera.
- Press `Space` to play a round. On the `multiplayer` branch, this starts a 3-second countdown.
- Press `R` to reset the score.
- Press `Q` to quit.

## Gesture Rules

- Rock: zero or one fingers extended
- Scissors: two fingers extended
- Paper: four fingers extended

Three fingers is treated as unknown so you get clear feedback when the gesture is not one of the game moves. The thumb is deliberately ignored because sideways thumb detection can be brittle in a quick classroom setup.

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
