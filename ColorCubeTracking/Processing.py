import cv2
import numpy as np


class ImageProcessor(object):
    SQUARE_SIMILARITY_ERROR = 30

    def detect_color_cube(self, mask_frame, frame):
        marked_frame = frame.copy()
        contours, _ = cv2.findContours(mask_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        max_area = 0
        candidate = None
        for contour in contours:
            rect = cv2.minAreaRect(contour)
            area = rect[1][0]*rect[1][1]
            if area > max_area and area > 30:       # cut off noise
                max_area = area
                candidate = rect

        if candidate:
            center = (int(candidate[0][0]), int(candidate[0][1]))
            box = np.int0(cv2.boxPoints(candidate))
            if self.is_square(box):
                cv2.drawContours(marked_frame, [box], 0, (0, 0, 255), 1)
                cv2.circle(marked_frame, center, 5, (255, 0, 0), 3)
                return center, marked_frame
        return None, frame

    def is_square(self, coords):
        """Checks whether a primitive found earlier looks like a square."""
        if abs(np.linalg.norm(coords[0]-coords[1]) -
               np.linalg.norm(coords[0] - coords[3])) < self.SQUARE_SIMILARITY_ERROR:
            return True
        return False
