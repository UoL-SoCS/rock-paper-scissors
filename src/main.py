import cv2

from game import COMPUTER_WIN, DRAW, MOVES, PLAYER_WIN
from game import choose_computer_move, decide_winner, reset_score, update_score
from hand_tracking import classify_gesture, create_hand_tracker, detect_first_hand
from hand_tracking import draw_hand_landmarks
from utils import CYAN, GREEN, RED, WHITE, YELLOW, draw_panel, draw_text


WINDOW_NAME = "Rock Paper Scissors"
CAMERA_INDEX = 0


def show_camera_message():
    print("Could not open the webcam.")
    print("Check that the camera is connected and that your OS allows camera access.")
    print("If another app is using the camera, close it and try again.")


def display_move(move):
    if not move:
        return "WAITING"

    return move.upper()


def result_color(result):
    if result == PLAYER_WIN:
        return GREEN
    if result == COMPUTER_WIN:
        return RED
    if result == DRAW:
        return YELLOW
    return WHITE


def draw_game_overlay(frame, player_move, finger_count, computer_move, result, score):
    height, width = frame.shape[:2]

    draw_panel(frame, 0, 0, width, 152)
    draw_text(frame, "Rock Paper Scissors", 28, 45, scale=1.2, color=YELLOW)
    draw_text(frame, "Show a gesture, then press SPACE to play", 30, 88, scale=0.75, color=WHITE)

    if finger_count is None:
        finger_text = "Fingers: -"
    else:
        finger_text = f"Fingers: {finger_count}"

    draw_text(frame, f"Player: {display_move(player_move)}", 30, 132, scale=0.82, color=CYAN)
    draw_text(frame, finger_text, 330, 132, scale=0.75, color=WHITE)

    draw_panel(frame, 0, height - 180, width, 180)
    draw_text(frame, f"Computer: {display_move(computer_move)}", 30, height - 132, scale=0.85)
    draw_text(frame, f"Result: {result}", 30, height - 90, scale=0.85, color=result_color(result))
    draw_text(
        frame,
        f"Score  You {score['player']} - {score['computer']} Computer",
        30,
        height - 50,
        scale=0.75,
        color=WHITE,
    )
    draw_text(frame, "SPACE play   R reset   Q quit", 30, height - 14, scale=0.65, color=WHITE)


def play_round(player_move, score):
    if player_move not in MOVES:
        return None, "Show rock, paper, or scissors first."

    computer_move = choose_computer_move()
    result = decide_winner(player_move, computer_move)
    update_score(score, result)
    return computer_move, result


def main():
    camera = cv2.VideoCapture(CAMERA_INDEX)

    if not camera.isOpened():
        show_camera_message()
        return

    score = reset_score()
    computer_move = None
    result = "Ready."

    with create_hand_tracker() as hand_tracker:
        while True:
            success, frame = camera.read()

            if not success:
                print("The webcam opened, but no frame was received.")
                break

            frame = cv2.flip(frame, 1)
            hand_landmarks, handedness = detect_first_hand(frame, hand_tracker)

            if hand_landmarks is None:
                player_move = None
                finger_count = None
            else:
                draw_hand_landmarks(frame, hand_landmarks)
                player_move, finger_count = classify_gesture(hand_landmarks, handedness)

            draw_game_overlay(frame, player_move, finger_count, computer_move, result, score)
            cv2.imshow(WINDOW_NAME, frame)

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

            if key == ord("r"):
                score = reset_score()
                computer_move = None
                result = "Score reset."

            if key == 32:
                computer_move, result = play_round(player_move, score)

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
