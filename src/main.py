import math
import time

import cv2

from game import DRAW, MOVES, PLAYER_1_WIN, PLAYER_2_WIN
from game import decide_multiplayer_winner, reset_multiplayer_score, update_multiplayer_score
from hand_tracking import classify_gesture, create_hand_tracker, detect_hands
from hand_tracking import draw_hand_landmarks
from utils import CYAN, GREEN, RED, WHITE, YELLOW, draw_panel, draw_text


WINDOW_NAME = "Rock, Paper, Scissors, AI!"
CAMERA_INDEX = 0
COUNTDOWN_SECONDS = 3
PLAYER_1 = "player_1"
PLAYER_2 = "player_2"


def show_camera_message():
    print("Could not open the webcam.")
    print("Check that the camera is connected and that your OS allows camera access.")
    print("If another app is using the camera, close it and try again.")


def window_was_closed():
    try:
        return cv2.getWindowProperty(WINDOW_NAME, cv2.WND_PROP_VISIBLE) < 1
    except cv2.error:
        return True


def display_move(move):
    if not move:
        return "WAITING"

    return move.upper()


def result_color(result):
    if result == PLAYER_1_WIN:
        return GREEN
    if result == PLAYER_2_WIN:
        return RED
    if result == DRAW:
        return YELLOW
    return WHITE


def empty_player_state():
    return {"landmarks": None, "move": None, "finger_count": None}


def hand_center_x(hand_landmarks):
    landmarks = hand_landmarks.landmark
    total_x = sum(landmark.x for landmark in landmarks)
    return total_x / len(landmarks)


def read_players(hand_landmarks_list):
    players = {
        PLAYER_1: empty_player_state(),
        PLAYER_2: empty_player_state(),
    }

    for hand_landmarks in hand_landmarks_list:
        player_key = PLAYER_1 if hand_center_x(hand_landmarks) < 0.5 else PLAYER_2
        player_move, finger_count = classify_gesture(hand_landmarks)
        players[player_key] = {
            "landmarks": hand_landmarks,
            "move": player_move,
            "finger_count": finger_count,
        }

    return players


def finger_text(finger_count):
    if finger_count is None:
        return "Fingers: -"

    return f"Fingers: {finger_count}"


def draw_countdown(frame, countdown_number):
    if countdown_number is None:
        return

    height, width = frame.shape[:2]
    text = str(countdown_number)
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 5.0
    thickness = 8
    text_size, _ = cv2.getTextSize(text, font, scale, thickness)
    text_x = (width - text_size[0]) // 2
    text_y = (height + text_size[1]) // 2

    draw_text(
        frame,
        text,
        text_x + 5,
        text_y + 5,
        scale=scale,
        color=(0, 0, 0),
        thickness=thickness + 2,
    )
    draw_text(
        frame,
        text,
        text_x,
        text_y,
        scale=scale,
        color=YELLOW,
        thickness=thickness,
    )


def draw_game_overlay(frame, players, result, score, countdown_number):
    height, width = frame.shape[:2]
    middle_x = width // 2
    player_1 = players[PLAYER_1]
    player_2 = players[PLAYER_2]

    draw_panel(frame, 0, 0, width, 166)
    draw_text(frame, "Rock, Paper, Scissors, AI!", 28, 45, scale=1.0, color=YELLOW)
    draw_text(frame, "Stand left and right. Press SPACE.", 30, 86, scale=0.72, color=WHITE)
    draw_text(frame, "Throw on 1.", 30, 120, scale=0.72, color=WHITE)
    draw_text(frame, "Player 1", 30, 154, scale=0.82, color=CYAN)
    draw_text(frame, "Player 2", middle_x + 30, 154, scale=0.82, color=GREEN)

    draw_panel(frame, 0, height - 200, width, 200)
    draw_text(frame, f"P1: {display_move(player_1['move'])}", 30, height - 154, scale=0.82, color=CYAN)
    draw_text(frame, finger_text(player_1["finger_count"]), 30, height - 118, scale=0.68, color=WHITE)
    draw_text(frame, f"P2: {display_move(player_2['move'])}", middle_x + 30, height - 154, scale=0.82, color=GREEN)
    draw_text(
        frame,
        finger_text(player_2["finger_count"]),
        middle_x + 30,
        height - 118,
        scale=0.68,
        color=WHITE,
    )
    draw_text(frame, f"Result: {result}", 30, height - 76, scale=0.68, color=result_color(result))
    draw_text(
        frame,
        f"Score  P1 {score['player_1']} - {score['player_2']} P2",
        30,
        height - 40,
        scale=0.68,
        color=WHITE,
    )
    draw_text(frame, "SPACE play   R reset   Q quit", 30, height - 14, scale=0.65, color=WHITE)
    cv2.line(frame, (middle_x, 0), (middle_x, height), YELLOW, 2)
    draw_countdown(frame, countdown_number)


def play_round(player_1_move, player_2_move, score):
    player_1_ready = player_1_move in MOVES
    player_2_ready = player_2_move in MOVES

    if not player_1_ready and not player_2_ready:
        return "Both players need rock, paper, or scissors."

    if not player_1_ready:
        return "Player 1, show rock, paper, or scissors."

    if not player_2_ready:
        return "Player 2, show rock, paper, or scissors."

    result = decide_multiplayer_winner(player_1_move, player_2_move)
    update_multiplayer_score(score, result)
    return result


def main():
    camera = cv2.VideoCapture(CAMERA_INDEX)

    if not camera.isOpened():
        show_camera_message()
        return

    score = reset_multiplayer_score()
    result = "Ready."
    countdown_started_at = None

    with create_hand_tracker(max_num_hands=2) as hand_tracker:
        while True:
            success, frame = camera.read()

            if not success:
                print("The webcam opened, but no frame was received.")
                break

            frame = cv2.flip(frame, 1)
            hand_landmarks_list = detect_hands(frame, hand_tracker)
            players = read_players(hand_landmarks_list)

            for hand_landmarks in hand_landmarks_list:
                draw_hand_landmarks(frame, hand_landmarks)

            countdown_number = None
            if countdown_started_at is not None:
                remaining = COUNTDOWN_SECONDS - (time.monotonic() - countdown_started_at)

                if remaining > 0:
                    countdown_number = math.ceil(remaining)
                    result = "Get ready..."
                else:
                    player_1_move = players[PLAYER_1]["move"]
                    player_2_move = players[PLAYER_2]["move"]
                    result = play_round(player_1_move, player_2_move, score)
                    countdown_started_at = None

            draw_game_overlay(frame, players, result, score, countdown_number)
            cv2.imshow(WINDOW_NAME, frame)

            key = cv2.waitKey(1) & 0xFF

            if window_was_closed():
                break

            if key == ord("q"):
                break

            if key == ord("r"):
                score = reset_multiplayer_score()
                result = "Score reset."
                countdown_started_at = None

            if key == 32 and countdown_started_at is None:
                countdown_started_at = time.monotonic()
                result = "Get ready..."

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
