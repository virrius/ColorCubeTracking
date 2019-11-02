import cv2
import numpy as np


class HSVtrackbarRange(object):
    _lowH = 0
    _highH = 179

    _lowS = 0
    _highS = 255

    _lowV = 0
    _highV = 255

    def __init__(self):
        cv2.namedWindow("Low_HSVcolor_range", cv2.WINDOW_AUTOSIZE)
        cv2.namedWindow("High_HSVcolor_range", cv2.WINDOW_AUTOSIZE)
        cv2.createTrackbar('lowH', "Low_HSVcolor_range", 0, 179, self._on_change_lowH)
        cv2.createTrackbar('highH', "High_HSVcolor_range", 179, 179, self._on_change_highH)
        cv2.createTrackbar('lowS', "Low_HSVcolor_range", 0, 255, self._on_change_lowS)
        cv2.createTrackbar('highS', "High_HSVcolor_range", 255, 255, self._on_change_highS)
        cv2.createTrackbar('lowV', "Low_HSVcolor_range", 0, 255, self._on_change_lowV)
        cv2.createTrackbar('highV', "High_HSVcolor_range", 255, 255, self._on_change_highV)
        self.low_visualization_matrix = np.zeros((100, 550, 3), np.uint8)
        self.high_visualization_matrix = np.zeros((100, 550, 3), np.uint8)
        self._update_low_color()
        self._update_high_color()

    def _on_change_lowH(self, val):
        self._lowH = val
        self._update_low_color()

    def _on_change_lowS(self, val):
        self._lowS = val
        self._update_low_color()

    def _on_change_lowV(self, val):
        self._lowV = val
        self._update_low_color()

    def _on_change_highH(self, val):
        self._highH = val
        self._update_high_color()

    def _on_change_highS(self, val):
        self._highS = val
        self._update_high_color()

    def _on_change_highV(self, val):
        self._highV = val
        self._update_high_color()

    def _update_high_color(self):
        self.high_visualization_matrix[:, :] = self.get_low_range()
        cv2.imshow('High_HSVcolor_range', cv2.cvtColor(self.high_visualization_matrix, cv2.COLOR_HSV2BGR))

    def _update_low_color(self):
        self.low_visualization_matrix[:, :] = self.get_low_range()
        cv2.imshow('Low_HSVcolor_range', cv2.cvtColor(self.low_visualization_matrix, cv2.COLOR_HSV2BGR))

    def get_low_range(self):
        return np.array((self._lowH, self._lowS, self._lowV), np.uint8)

    def get_high_range(self):
        return np.array((self._highH, self._highS, self._highV), np.uint8)

    def get_color(self):
        return (self.get_high_range() + self.get_low_range())/2


class HSVtrackbarDelta(object):
    _H = 0
    _S = 0
    _V = 0
    deltaH = 0
    deltaS = 0
    deltaV = 0

    def __init__(self, deltaH, deltaS, deltaV):
        self.deltaH = deltaH
        self.deltaS = deltaS
        self.deltaV = deltaV
        cv2.namedWindow("HSVcolor", cv2.WINDOW_AUTOSIZE)
        cv2.createTrackbar('H', "HSVcolor", 0, 179, self._on_change_H)
        cv2.createTrackbar('S', "HSVcolor", 0, 255, self._on_change_S)
        cv2.createTrackbar('V', "HSVcolor", 0, 255, self._on_change_V)
        self.visualization_matrix = np.zeros((100, 550, 3), np.uint8)
        self._update_color()

    def _on_change_H(self, val):
        self._H = val
        self._update_color()

    def _on_change_S(self, val):
        self._S = val
        self._update_color()

    def _on_change_V(self, val):
        self._V = val
        self._update_color()

    def _update_color(self):
        self.visualization_matrix[:, :] = self.get_color()
        cv2.imshow('HSVcolor', cv2.cvtColor(self.visualization_matrix, cv2.COLOR_HSV2BGR))

    def get_low_range(self):
        return np.array((self._H - self.deltaH, max(0, self._S - self.deltaS), max(0, self._V - self.deltaV)), np.uint8)

    def get_high_range(self):
        return np.array((self._H + self.deltaH, min(255, self._S + self.deltaS), min(255, self._V + self.deltaV)),
                        np.uint8)

    def get_color(self):
        return np.array((self._H, self._S, self._V), np.uint8)
