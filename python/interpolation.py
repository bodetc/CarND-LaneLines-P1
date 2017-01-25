import cv2
from sklearn import linear_model
import numpy as np

def draw_regression_line(img, image_settings, x, y, color=[255, 0, 0], thickness=2):
    regression = linear_model.LinearRegression()
    regression.fit(y, x)

    y_max = image_settings.height
    x_max = regression.predict(y_max)

    y_min = image_settings.mask_height
    x_min = regression.predict(y_min)

    cv2.line(img, (x_min, y_min), (x_max, y_max), color, thickness)


def draw_long_lines(img, image_settings, lines, color=[255, 0, 0], thickness=2):
    left_x = []
    left_y = []
    right_x = []
    right_y = []

    center = image_settings.center

    for line in lines:
        for x1, y1, x2, y2 in line:
            if x1 < center and x2 < center:
                left_x.append(x1)
                left_y.append([y1])
                left_x.append(x2)
                left_y.append([y2])

            if x1 > center and x2 > center:
                right_x.append(x1)
                right_y.append([y1])
                right_x.append(x2)
                right_y.append([y2])

    if len(left_x)>0:
        draw_regression_line(img, image_settings, left_x, left_y, color, thickness)

    if len(right_x) > 0:
        draw_regression_line(img, image_settings, right_x, right_y, color, thickness)

    return img


def hough_with_interpolation(img, rho, theta, threshold, min_line_len, max_line_gap, image_settings):
    """
    `img` should be the output of a Canny transform.

    Returns an image with hough lines drawn.
    """
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len,
                            maxLineGap=max_line_gap)

    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    draw_long_lines(line_img, image_settings, lines, thickness=4)
    return line_img
