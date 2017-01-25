# importing some useful packages
import matplotlib.image as mpimg

from process_image import process_image

import os
os.listdir("test_images/")

# TODO: Build your pipeline that will draw lane lines on the test_images
# then save them to the test_images directory.

for imFile in os.listdir("test_images/"):
    print('Reading file:' + imFile)
    image=mpimg.imread("test_images/"+imFile)
    print('This image is:', type(image), 'with dimensions:', image.shape)
    processed_image = process_image(image)
    mpimg.imsave("test_images_processed/"+imFile, processed_image)
