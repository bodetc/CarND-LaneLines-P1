# importing some useful packages
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from process_image import process_image

# %matplotlib inline

# reading in an image
image = mpimg.imread('test_images/solidWhiteRight.jpg')
# printing out some stats and plotting
print('This image is:', type(image), 'with dimesions:', image.shape)
# if you wanted to show a single color channel image called 'gray', for example, call as plt.imshow(gray, cmap='gray')
plt.imshow(image)

import os
os.listdir("test_images/")

# TODO: Build your pipeline that will draw lane lines on the test_images
# then save them to the test_images directory.

for imFile in os.listdir("test_images/"):
    print(imFile)
    image=mpimg.imread("test_images/"+imFile)
    processed_image = process_image(image)
    mpimg.imsave("test_images_processed/"+imFile, processed_image)
