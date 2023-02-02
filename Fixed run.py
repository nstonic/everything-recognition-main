import cv2

from config import CASCADES


def is_user_wants_quit():
    return cv2.waitKey(1) & 0xFF == ord('q')


def show_frame(frame):
    cv2.imshow('Video', frame)


def draw_sqare(frame, color: tuple, rectangle: tuple):
    x, y, w, h = rectangle
    cv2.rectangle(
        img=frame,
        pt1=(x, y),
        pt2=(x + w, y + h),
        color=color,
        thickness=2
    )


def get_rectangle(frame, cascade) -> tuple:
    return cascade.detectMultiScale(
        frame,
        scaleFactor=1.1,
        minNeighbors=10,
        minSize=(30, 30)
    )


def render_video(video, cascades):
    while True:
        if is_user_wants_quit():
            break

        if not video.isOpened():
            print("Couldn't find your webcam... Sorry :c")

        _, webcam_frame = video.read()
        gray_frame = cv2.cvtColor(webcam_frame, cv2.COLOR_BGR2GRAY)

        captures = (
            (color, get_rectangle(frame=gray_frame, cascade=cascade))
            for color, cascade in cascades
        )

        for color, capture in captures:
            for rectangle in capture:
                draw_sqare(webcam_frame, color, rectangle)

        show_frame(webcam_frame)


def main():
    cascades = (
        (cascade['color'], cv2.CascadeClassifier(cascade['path']))
        for _, cascade in CASCADES.items()
        if cascade['draw']
    )
    video = cv2.VideoCapture(0)
    try:
        render_video(video, cascades)
    finally:
        video.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
