# 45-Minute Tutorial

This tutorial turns the mostly complete starter on `main` into the finished webcam rock-paper-scissors game.

The goal is not to type a lot of code. The goal is for students to see how the camera, hand landmarks, simple rules, and game logic fit together.

## Timing Plan

- 0-5 min: setup, run the app, explain the files
- 5-10 min: draw hand landmarks
- 10-25 min: count fingers and classify gestures
- 25-35 min: add the computer move and winner logic
- 35-42 min: update the score and test the game
- 42-45 min: stretch ideas or switch stuck groups to `complete-solution`

## Files

- `src/main.py`: camera loop, controls, and on-screen display
- `src/hand_tracking.py`: MediaPipe hand detection and gesture rules
- `src/game.py`: random computer move, winner logic, and score
- `src/utils.py`: small OpenCV drawing helpers

## Before You Start

Install the requirements and run the app.

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

You should see the webcam feed and the game overlay. At the start, the app is not finished: it should show `UNKNOWN` for the player move and the score will not change yet.

## Step 1: Draw Hand Landmarks

Open `src/main.py` and find `TODO 1`.

Replace the TODO comment with:

```python
draw_hand_landmarks(frame, hand_landmarks)
```

Run the app again. When a hand is visible, MediaPipe should draw dots and lines over it.

Checkpoint: students can explain that MediaPipe finds landmark points on the hand, and OpenCV draws them on the webcam frame.

## Step 2: Count the Thumb

Open `src/hand_tracking.py` and find `TODO 2` inside `count_extended_fingers`.

Add:

```python
if handedness == "Right":
    thumb_extended = landmarks[THUMB_TIP].x > landmarks[THUMB_IP].x
else:
    thumb_extended = landmarks[THUMB_TIP].x < landmarks[THUMB_IP].x

if thumb_extended:
    extended_fingers += 1
```

The thumb is sideways, so we compare `x` positions. This is different from the other fingers.

Checkpoint: make a thumbs-up shape and watch the finger count change.

## Step 3: Count the Other Fingers

Stay in `src/hand_tracking.py` and find `TODO 3`.

Add:

```python
for tip_id, pip_id in zip(FINGER_TIPS, FINGER_PIPS):
    if landmarks[tip_id].y < landmarks[pip_id].y:
        extended_fingers += 1
```

For the index, middle, ring, and little finger, a finger is extended when its tip is higher on the screen than its middle joint.

Checkpoint: try a fist, two fingers, and an open hand. The finger count should now be roughly 0, 2, and 5.

## Step 4: Classify the Gesture

In `src/hand_tracking.py`, find `TODO 4` inside `classify_gesture`.

Add:

```python
if finger_count <= 1:
    return "rock", finger_count

if finger_count == 2:
    return "scissors", finger_count

if finger_count >= 4:
    return "paper", finger_count
```

Leave the existing final line:

```python
return "unknown", finger_count
```

Checkpoint: the overlay should now show `ROCK`, `SCISSORS`, or `PAPER`.

## Step 5: Choose the Computer Move

Open `src/game.py` and find `TODO 5`.

Replace the temporary return value with:

```python
return random.choice(MOVES)
```

Checkpoint: press `Space` a few times. The computer move should change randomly.

## Step 6: Decide the Winner

In `src/game.py`, find `TODO 6` and `TODO 7` inside `decide_winner`.

Add:

```python
if player_move == computer_move:
    return DRAW

if WINNING_MOVE[player_move] == computer_move:
    return PLAYER_WIN

return COMPUTER_WIN
```

Remove the temporary `return "Round played."` line.

Checkpoint: play each gesture against the computer and check that the result makes sense.

## Step 7: Update the Score

In `src/game.py`, find `TODO 8` inside `update_score`.

Replace the temporary `return` with:

```python
if result == PLAYER_WIN:
    score["player"] += 1
elif result == COMPUTER_WIN:
    score["computer"] += 1
```

Checkpoint: press `Space` to play rounds and `R` to reset the score.

## Final Test

Before the class calls it finished, check:

- `Q` quits the app
- `R` resets the score
- `Space` plays one round
- rock, paper, and scissors are detected
- the computer move is random
- the result and score update clearly

## Fallback

If a student or group gets stuck, switch to the complete branch:

```bash
git switch complete-solution
python src/main.py
```

To return to the workshop branch:

```bash
git switch main
```

The complete branch keeps the same structure, so students can compare their files with the finished version.
