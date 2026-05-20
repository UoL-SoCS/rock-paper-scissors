import cv2
import os
import tempfile


os.environ.setdefault("MPLCONFIGDIR", os.path.join(tempfile.gettempdir(), "rps-matplotlib-cache"))

import mediapipe as mp


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_styles = mp.solutions.drawing_styles

FINGER_TIPS = (8, 12, 16, 20)
FINGER_BENDS = (6, 10, 14, 18)


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
        return None

    return results.multi_hand_landmarks[0]


def draw_hand_landmarks(frame, hand_landmarks):
    mp_drawing.draw_landmarks(
        frame,
        hand_landmarks,
        mp_hands.HAND_CONNECTIONS,
        mp_styles.get_default_hand_landmarks_style(),
        mp_styles.get_default_hand_connections_style(),
    )


def count_extended_fingers(hand_landmarks):
    landmarks = hand_landmarks.landmark
    extended_fingers = 0

    # TODO 3: Count each finger whose tip is above its middle bend.
    # Use FINGER_TIPS and FINGER_BENDS together with zip(...).

    return extended_fingers


def classify_gesture(hand_landmarks):
    finger_count = count_extended_fingers(hand_landmarks)

    # TODO 4: Turn the finger count into a game move.
    # 0 or 1 fingers = rock
    # 2 fingers = scissors
    # 4 fingers = paper

    return "unknown", finger_count
