import cv2


WINDOW_NAME = "Rock Paper Scissors"


def draw_text(frame, text, x, y, scale=1.0, color=(255, 255, 255)):
    cv2.putText(
        frame,
        text,
        (x, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        scale,
        color,
        2,
        cv2.LINE_AA,
    )


def show_camera_message():
    print("Could not open the webcam.")
    print("Check that the camera is connected and that your OS allows camera access.")
    print("If another app is using the camera, close it and try again.")


def main():
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        show_camera_message()
        return

    while True:
        success, frame = camera.read()

        if not success:
            print("The webcam opened, but no frame was received.")
            break

        frame = cv2.flip(frame, 1)

        draw_text(frame, "Rock Paper Scissors", 30, 50, scale=1.2)
        draw_text(frame, "Milestone 1: webcam feed", 30, 95, scale=0.8, color=(0, 255, 255))
        draw_text(frame, "Press Q to quit", 30, frame.shape[0] - 30, scale=0.8)

        cv2.imshow(WINDOW_NAME, frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
