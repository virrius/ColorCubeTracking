import cv2
from GUI import HSVtrackbarRange, HSVtrackbarDelta


def cube_recognizing_from_video_stream(camera, processor, serial):
    frame_processing = False
    cam = cv2.VideoCapture(camera)
    cv2.namedWindow("VideoStream", cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow("Mask", cv2.WINDOW_AUTOSIZE)
    trackbar = HSVtrackbarRange()
    # trackbar = HSVtrackbarDelta(60, 100, 100)
    while True:
        ret, frame = cam.read()

        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask_frame = cv2.inRange(hsv_frame, trackbar.get_low_range(), trackbar.get_high_range())
        key = cv2.waitKey(1)
        if key == 27:
            break
        elif key == ord('w'):
            frame_processing = not frame_processing

        if frame_processing:
            center, frame = processor.detect_color_cube(mask_frame, frame)
            if center is not None:
                serial.send_data((center, trackbar.get_color()))

        cv2.imshow("VideoStream", frame)
        cv2.imshow("Mask", mask_frame)
    cam.release()
    cv2.destroyAllWindows()

