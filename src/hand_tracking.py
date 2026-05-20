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

    for tip_id, bend_id in zip(FINGER_TIPS, FINGER_BENDS):
        if landmarks[tip_id].y < landmarks[bend_id].y:
            extended_fingers += 1

    return extended_fingers


def classify_gesture(hand_landmarks):
    finger_count = count_extended_fingers(hand_landmarks)

    if finger_count <= 1:
        return "rock", finger_count

    if finger_count == 2:
        return "scissors", finger_count

    if finger_count >= 4:
        return "paper", finger_count

    return "unknown", finger_count
