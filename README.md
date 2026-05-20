# Webcam Rock Paper Scissors

A classroom-friendly Python activity that turns a webcam into a rock-paper-scissors game.

The workshop branch starts with a small runnable webcam demo. A finished version is kept on the `complete-solution` branch so the class has a fallback if a machine or group gets stuck.

## Setup

Use Python 3.11.

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

## Workshop Flow

1. Open the webcam feed.
2. Draw hand landmarks.
3. Classify rock, paper, and scissors.
4. Generate a computer move.
5. Decide the winner and update the score.

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
