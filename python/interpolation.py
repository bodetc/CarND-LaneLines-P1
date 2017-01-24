import cv2
from sklearn import linear_model
import numpy as np


def draw_regression_line(img, X, y, color=[255, 0, 0], thickness=2):
    regression = linear_model.LinearRegression()
    regression.fit(X, y)

    x_max = np.amax(X)
    y_max = regression.predict(x_max)

    x_min = np.amin(X)
    y_min = regression.predict(x_min)

    cv2.line(img, (x_min, y_min), (x_max, y_max), color, thickness)


def draw_long_lines(img, lines, color=[255, 0, 0], thickness=2):
    left_X = []
    left_y = []
    right_X = []
    right_y = []

    for line in lines:
        for x1, y1, x2, y2 in line:
            if x1 < 470 and x2 < 470:
                left_X.append([x1])
                left_y.append(y1)
                left_X.append([x2])
                left_y.append(y2)

            if x1 > 470 and x2 > 470:
                right_X.append([x1])
                right_y.append(y1)
                right_X.append([x2])
                right_y.append(y2)

    draw_regression_line(img, left_X, left_y, color, thickness)
    draw_regression_line(img, right_X, right_y, color, thickness)

    return img


def hough_with_interpolation(img, rho, theta, threshold, min_line_len, max_line_gap):
    """
    `img` should be the output of a Canny transform.

    Returns an image with hough lines drawn.
    """
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len,
                            maxLineGap=max_line_gap)

    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    draw_long_lines(line_img, lines, thickness=4)
    return line_img
