# importing some useful packages
import matplotlib.image as mpimg

from process_image import process_image

import os

os.listdir("test_images/")

for imFile in os.listdir("test_images/"):
    print('Reading file:' + imFile)
    image = mpimg.imread("test_images/" + imFile)
    print('This image is:', type(image), 'with dimensions:', image.shape)
    line_image = process_image(image, extrapolation=False)
    mpimg.imsave("test_images/processed_" + imFile, line_image)
    processed_image = process_image(image)
    mpimg.imsave("test_images/processed_" + imFile, processed_image)
