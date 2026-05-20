# AGENTS.md

## Project overview

This project is a short, classroom-friendly computer vision activity for a school event. The goal is to build a webcam-based rock-paper-scissors game in Python that is simple enough to follow live, visually engaging, and reliable on locally installed machines.

The code should prioritise:

- clarity over cleverness
- fast visual feedback
- minimal dependencies
- easy local setup in VS Code
- small, incremental changes that students can copy alongside a live demo

## Recommended stack

- Python 3.11
- OpenCV for webcam capture and display
- MediaPipe for hand landmark detection
- Random module from the Python standard library for the computer’s move

Avoid adding heavier frameworks unless they are strictly necessary.

## Repository structure

A sensible layout is:

```text
.
├── README.md
├── AGENTS.md
├── requirements.txt
├── start.bat
├── start.sh
├── src/
│   ├── main.py
│   ├── game.py
│   ├── hand_tracking.py
│   └── utils.py
└── assets/
    └── optional_images_or_icons/
```

Keep the first working version small. A single-file starter is acceptable if that makes the workshop easier to teach.

## Local development setup

Use a virtual environment and keep it ready before the session.

Typical setup:

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
python src/main.py
```

If the project is intended for multiple classroom machines, prepare a start script so students do not need to remember commands.

## Coding conventions

Use straightforward, readable Python.

- Prefer short functions with one job each.
- Use clear variable names such as `player_move`, `computer_move`, `hand_landmarks`, and `score`.
- Keep comments brief and instructional.
- Avoid classes unless they genuinely improve readability.
- Do not over-engineer the architecture.
- Keep the main loop easy to follow.

## Activity design rules

The session should be built around visible milestones.

Good milestones:

1. open webcam feed
2. draw hand landmarks
3. classify rock, paper, scissors
4. generate a computer move
5. decide winner and update score

Do not spend time on model training, dataset collection, or deep theory. The activity should feel like a working interactive demo very quickly.

## Gesture logic

A simple rule-based classifier is preferred. For example:

- rock = zero or one fingers extended
- scissors = two fingers extended
- paper = four or five fingers extended

The exact rule can be adjusted to match the chosen hand-tracking approach, but the logic should remain easy for students to understand.

## Classroom reliability

The code should be robust in a lab setting.

- Assume different webcams may behave slightly differently.
- Provide a fallback message if no camera is found.
- Include clear instructions if permissions fail.
- Keep frame processing light enough to run smoothly on modest hardware.
- Avoid requiring internet access during the session.

## Teaching-friendly output

The app should show clear feedback on screen:

- the student’s current gesture
- the computer’s move
- the result of the round
- the score

Use large readable text and simple visuals. A demo that can be understood from the back of a room is ideal.

## Testing checklist

Before the event, verify that:

- the webcam opens successfully
- the hand landmarks render correctly
- each gesture is recognised consistently
- the computer move is displayed clearly
- the game resets cleanly between rounds
- the app runs on every target machine

## Suggested workshop approach

The `main` branch should be the guided tutorial branch. Keep it mostly complete, runnable, and easy to teach in about 45 minutes, with a small number of clearly labelled `TODO` sections that students can fill in during the activity.

When editing the code for the workshop, make changes in small steps and keep each step runnable.

A good sequence is:

- run the camera feed and overlays
- draw hand landmarks
- count extended fingers
- classify gestures
- add random computer moves
- decide winners and update the score

## Complete solution fallback

Keep a separate `complete-solution` branch with the finished version of the project.

This branch is a safety net for the session. If a student or group gets stuck, their local copy breaks, or a classroom machine behaves differently, the complete branch should let them quickly switch to a known working version and stay involved in the activity.

Before the event, verify that the complete branch:

- runs from a fresh checkout
- includes any start scripts and setup instructions
- has the final webcam, gesture, game, score, and reset behaviour working
- stays close enough to the workshop code that students can compare the two

## What to avoid

- training a model live
- large notebooks
- heavy dependency chains
- obscure abstractions
- long code blocks that students must type without seeing a result
- anything that depends on cloud services or login flows

## Final goal

By the end of the activity, a student should be able to explain the project in plain language:

> We built a webcam game that reads hand gestures and plays rock-paper-scissors against the computer.
