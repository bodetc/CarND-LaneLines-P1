import interpolation
from tools import *

def process_image(image):
    # Kernel size of Gaussian Smoothing
    kernel_size = 5
    # Low and high thresholds of Canny transform
    low_threshold = 50
    high_threshold = 120
    # This time we are defining a four sided polygon to mask
    vertices = np.array([[(0, 540), (440, 330), (500, 330), (960,540)]], dtype=np.int32)
    # Define the Hough transform parameters
    rho = 2  # distance resolution in pixels of the Hough grid
    theta = np.pi / 180  # angular resolution in radians of the Hough grid
    threshold = 15  # minimum number of votes (intersections in Hough grid cell)
    min_line_length = 30  # minimum number of pixels making up a line
    max_line_gap = 20  # maximum gap in pixels between connectable line segments

    # Transform to Grayscale
    gray = grayscale(image)

    # Apply Gaussian blur
    blur_gray = gaussian_blur(gray, kernel_size)

    # Apply Canny transformation
    edges = canny(blur_gray, low_threshold, high_threshold)

    # Next we'll create a masked edges image using cv2.fillPoly()
    masked_edges = region_of_interest(edges, vertices)

    # Run Hough on edge detected image
    # hough = hough_lines(masked_edges, rho, theta, threshold, min_line_length, max_line_gap)
    hough = interpolation.hough_with_interpolation(masked_edges, rho, theta, threshold, min_line_length, max_line_gap)

    processed_image = weighted_img(hough, image)

    return processed_image
