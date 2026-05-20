import cv2
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

    if handedness == "Right":
        thumb_extended = landmarks[THUMB_TIP].x > landmarks[THUMB_IP].x
    else:
        thumb_extended = landmarks[THUMB_TIP].x < landmarks[THUMB_IP].x

    if thumb_extended:
        extended_fingers += 1

    for tip_id, pip_id in zip(FINGER_TIPS, FINGER_PIPS):
        if landmarks[tip_id].y < landmarks[pip_id].y:
            extended_fingers += 1

    return extended_fingers


def classify_gesture(hand_landmarks, handedness):
    finger_count = count_extended_fingers(hand_landmarks, handedness)

    if finger_count <= 1:
        return "rock", finger_count

    if finger_count == 2:
        return "scissors", finger_count

    if finger_count >= 4:
        return "paper", finger_count

    return "unknown", finger_count
