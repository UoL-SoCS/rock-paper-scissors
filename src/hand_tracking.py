import cv2
import os
import tempfile


os.environ.setdefault("MPLCONFIGDIR", os.path.join(tempfile.gettempdir(), "rps-matplotlib-cache"))

import mediapipe as mp


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_styles = mp.solutions.drawing_styles

FINGER_TIPS = (8, 12, 16, 20)
FINGER_PIPS = (6, 10, 14, 18)
THUMB_TIP = 4
THUMB_IP = 3


def create_hand_tracker():
    return mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.5,
    )


def detect_first_hand(frame, hand_tracker):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hand_tracker.process(rgb_frame)

    if not results.multi_hand_landmarks:
        return None, None

    hand_landmarks = results.multi_hand_landmarks[0]
    handedness = "Right"

    if results.multi_handedness:
        handedness = results.multi_handedness[0].classification[0].label

    return hand_landmarks, handedness


def draw_hand_landmarks(frame, hand_landmarks):
    mp_drawing.draw_landmarks(
        frame,
        hand_landmarks,
        mp_hands.HAND_CONNECTIONS,
        mp_styles.get_default_hand_landmarks_style(),
        mp_styles.get_default_hand_connections_style(),
    )


def count_extended_fingers(hand_landmarks, handedness):
    landmarks = hand_landmarks.landmark
    extended_fingers = 0

    # TODO 2: Count the thumb if it points away from the hand.
    # Right hands point to the right of the image. Left hands point to the left.

    # TODO 3: Count each finger whose tip is above its middle joint.
    # Use FINGER_TIPS and FINGER_PIPS together with zip(...).

    return extended_fingers


def classify_gesture(hand_landmarks, handedness):
    finger_count = count_extended_fingers(hand_landmarks, handedness)

    # TODO 4: Turn the finger count into a game move.
    # 0 or 1 fingers = rock
    # 2 fingers = scissors
    # 4 or 5 fingers = paper

    return "unknown", finger_count
