import cv2


WHITE = (255, 255, 255)
YELLOW = (0, 255, 255)
CYAN = (255, 255, 0)
GREEN = (80, 220, 80)
RED = (80, 80, 255)
PANEL = (20, 20, 20)


def draw_panel(frame, x, y, width, height, color=PANEL, alpha=0.72):
    overlay = frame.copy()
    cv2.rectangle(overlay, (x, y), (x + width, y + height), color, -1)
    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)


def draw_text(frame, text, x, y, scale=1.0, color=WHITE, thickness=2):
    cv2.putText(
        frame,
        text,
        (x, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        scale,
        color,
        thickness,
        cv2.LINE_AA,
    )
