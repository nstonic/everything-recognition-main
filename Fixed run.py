from typing import NamedTuple

import cv2

from config import CASCADES


class Cascade(NamedTuple):
    color: tuple
    classifier: cv2.CascadeClassifier


def is_user_wants_quit() -> bool:
    return cv2.waitKey(1) & 0xFF == ord('q')


def draw_square(frame, color: tuple, rectangle: tuple):
    x, y, w, h = rectangle
    cv2.rectangle(
        img=frame,
        pt1=(x, y),
        pt2=(x + w, y + h),
        color=color,
        thickness=2
    )


def get_rectangle(frame, cascade: cv2.CascadeClassifier) -> tuple:
    return cascade.detectMultiScale(
        frame,
        scaleFactor=1.1,
        minNeighbors=10,
        minSize=(30, 30)
    )


def render_video(video: cv2.VideoCapture, cascades: list[Cascade]):
    while True:
        if is_user_wants_quit():
            break

        if not video.isOpened():
            raise IOError("Couldn't find your webcam... Sorry :c")

        _, webcam_frame = video.read()
        gray_frame = cv2.cvtColor(webcam_frame, cv2.COLOR_BGR2GRAY)

        captures = (
            (cascade.color, get_rectangle(frame=gray_frame, cascade=cascade.classifier))
            for cascade in cascades
        )

        for color, rectangles in captures:
            for rectangle in rectangles:
                draw_square(webcam_frame, color, rectangle)

        cv2.imshow('Video', webcam_frame)


def main():
    cascades = [
        Cascade(
            color=cascade['color'],
            classifier=cv2.CascadeClassifier(cascade['path'])
        )
        for cascade in CASCADES.values()
        if cascade['draw']
    ]
    video = cv2.VideoCapture(0)
    print('Press "q" for close video')
    try:
        render_video(video, cascades)
    finally:
        video.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
