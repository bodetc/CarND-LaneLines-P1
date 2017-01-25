from tools import *
from extrapolation import hough_with_interpolation


# Settings of the image and of the masked edges
class ImageSettings:
    width = 960
    height = 540
    center = 470
    mask_height = 330
    mask_top_width = 30

    def getVertices(self):
        top_left = self.center - self.mask_top_width
        top_righ = self.center + self.mask_top_width

        return np.array(
            [[(0, self.height), (top_left, self.mask_height), (top_righ, self.mask_height), (self.width, self.height)]],
            dtype=np.int32)


# Settings of the transformation
def default_settings():
    # Kernel size of Gaussian Smoothing
    kernel_size = 3
    # Low and high thresholds of Canny transform
    low_threshold = 30
    high_threshold = 120
    # Define the Hough transform parameters
    rho = 2  # distance resolution in pixels of the Hough grid
    theta = np.pi / 180  # angular resolution in radians of the Hough grid
    threshold = 15  # minimum number of votes (intersections in Hough grid cell)
    min_line_length = 30  # minimum number of pixels making up a line
    max_line_gap = 30  # maximum gap in pixels between connectable line segments
    return high_threshold, kernel_size, low_threshold, max_line_gap, min_line_length, rho, theta, threshold


def process_image(image, image_settings=ImageSettings(), extrapolation=False):
    # Get settings
    high_threshold, kernel_size, low_threshold, max_line_gap, min_line_length, rho, theta, threshold = default_settings()

    # Transform to Grayscale
    gray = grayscale(image)

    # Apply Gaussian blur
    blur_gray = gaussian_blur(gray, kernel_size)

    # Apply Canny transformation
    edges = canny(blur_gray, low_threshold, high_threshold)

    # Create a masked edges image
    vertices = image_settings.getVertices()
    masked_edges = region_of_interest(edges, vertices)

    if (extrapolation):
        # Run Hough on edge detected image and reduce to the left and right lanes
        hough = hough_with_interpolation(masked_edges, rho, theta, threshold, min_line_length, max_line_gap,
                                         image_settings)
    else:
        # Run Hough on edge detected image
        hough = hough_lines(masked_edges, rho, theta, threshold, min_line_length, max_line_gap)

    processed_image = weighted_img(hough, image)

    return processed_image
