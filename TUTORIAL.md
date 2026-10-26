# 45-Minute Tutorial

This tutorial turns the mostly complete starter code into a webcam-powered Rock, Paper, Scissors game. 

The point is not to type heroic amounts of code. The point is to make a webcam do something fun, see each milestone working, and end with a game you can play with, all using state-of-the-art hand tracking.

By the end, the program will do three jobs:

1. Look for a hand in the camera image.
2. Count raised fingers using hand landmarks.
3. Play Rock, Paper, Scissors, AI! against the computer.

## Timing Plan

- 0-5 min: setup, run the app, and meet the files
- 5-10 min: activate the camera feed
- 10-15 min: draw hand landmarks
- 15-25 min: count fingers and classify gestures
- 25-35 min: add the computer move and winner logic
- 35-42 min: update the score and test the game
- 42-45 min: celebrate, tweak, or use `complete-solution` if you are stuck

## Files

- `src/main.py`: the main loop, webcam frames, controls, and on-screen display
- `src/hand_tracking.py`: MediaPipe hand detection and our gesture rules
- `src/game.py`: computer move, winner logic, and score
- `src/utils.py`: small OpenCV drawing helpers

The files are split by job so the project is easier to talk through. No mystery architecture, just a few tidy drawers.

## Before You Start

You will need to install the requirements and run the app. We are using `uv` which will do both of those steps for you!

```bash
uv run src/main.py
```

At the very start, the app prints a camera message because the first TODO has not been completed yet. That is intentional. The first job is to wake up the webcam.

What is happening: the project already has most of the display and game loop ready. You will fill in the important missing pieces one at a time, then rerun the app after each one.

## Step 1: Activate the Camera

Open `src/main.py` and find `TODO 1`.

Replace:

```python
return None
```

with:

```python
return cv2.VideoCapture(CAMERA_INDEX)
```

Run the app again. You should see the webcam feed and the game overlay.

What is happening: OpenCV asks the computer for camera `0`, which is usually the built-in or default webcam. After that, the main loop asks the camera for one frame after another, fast enough that it feels like video.

Checkpoint: you can point to the camera window and say, "This is OpenCV giving us live image frames."

## Step 2: Draw Hand Landmarks

Stay in `src/main.py` and find `TODO 2`.

Replace the TODO comment with:

```python
draw_hand_landmarks(frame, hand_landmarks)
```

Run the app again. When a hand is visible, MediaPipe should draw dots and lines over it.
analyses the image and returns landmark points for a hand. Each point has an `x` and `y` position. We draw those points so you can see just how robust the hand tracking. MediaPipe is an AI tool developed by Google and trained on a huge variety of hand images. It can track hands in all sorts of positions, lighting conditions, and backgrounds.

Checkpoint: wave a hand in front of the camera and watch the landmarks follow it.

## Step 3: Count the Fingers

Open `src/hand_tracking.py` and find `TODO 3`.

Add:

```python
for tip_id, bend_id in zip(FINGER_TIPS, FINGER_BENDS):
    if landmarks[tip_id].y < landmarks[bend_id].y:
        extended_fingers += 1
```

What is happening: for each finger, we compare the fingertip with the middle bend of that finger. On screen, a smaller `y` value means higher up. So if the fingertip is higher than the bend, we count that finger as raised.

We deliberately ignore the thumb. We can distinguish rock, paper, and scissors just by counting the other four fingers.

Checkpoint: try a fist, two fingers, and an open hand. The finger count should now be roughly `0`, `2`, and `4`.

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

What is happening: this is a simple rule-based system that chooses a label based on the number of extended fingers. If the count is `0` or `1`, we call it `rock`. If the count is `2`, we call it `scissors`. If the count is `4` or `5`, we call it `paper`. Any other counts are classified as `unknown`.

Checkpoint: the overlay should now show `ROCK`, `SCISSORS`, `PAPER`, or `UNKNOWN` depending on your hand gesture.

## Step 5: Choose the Computer Move

Open `src/game.py` and find `TODO 5`.

Replace the temporary return value with:

```python
return random.choice(MOVES)
```

What is happening: `MOVES` is just a tuple containing `"rock"`, `"paper"`, and `"scissors"`. `random.choice(...)` picks one item from that tuple. The computer has no grand strategy; it is confidently winging it.

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

What is happening: `WINNING_MOVE` stores the move each player move beats. For example, `"rock"` beats `"scissors"`. Instead of writing every possible matchup separately, the dictionary lets the code ask one clear question.

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

What is happening: `score` is a dictionary with two numbers in it. A player win increases `score["player"]`; a computer win increases `score["computer"]`; a draw leaves both alone.

Checkpoint: press `Space` to play rounds and `R` to reset the score.

## Final Test

Before you call it finished, check:

- `Q` quits the app
- `R` resets the score
- `Space` plays one round
- rock, paper, and scissors are detected
- the computer move is random
- the result and score update clearly

Here's what we did in one sentence:

> We used a webcam to find hand landmarks, counted raised fingers, turned that into a rock-paper-scissors move, and played against a random computer move.

## Fallback

If you get stuck, switch to the complete branch:

```bash
git switch complete-solution
uv run src/main.py
```

To return to the workshop branch:

```bash
git switch main
```

The complete branch keeps the same structure, so you can compare your files with the finished version and get back into the activity quickly.

## Extensions

Did you enjoy the tutorial and want to take it further? Here are some ideas:
- Add a countdown timer that gives the player a few seconds to get ready before each round.
- Use a more complex AI strategy for the computer move, like tracking the player's previous moves and trying to predict the next one.
- Add sound effects or animations for each move and outcome.
- Implement a two-player mode where two people can play against each other using the same webcam feed.
- Create a more polished user interface with better graphics and layout.

Send us your extensions or ideas in the GitHub discussions for this project!
