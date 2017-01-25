# Import everything needed to edit/save/watch video clips
from moviepy.editor import VideoFileClip

import os

os.listdir("test_images/")

from process_image import process_image
from process_image import ImageSettings

white_output = 'white.mp4'
clip1 = VideoFileClip("solidWhiteRight.mp4")
white_clip = clip1.fl_image(process_image)  # NOTE: this function expects color images!!
white_clip.write_videofile(white_output, audio=False)

yellow_output = 'yellow.mp4'
clip2 = VideoFileClip('solidYellowLeft.mp4')
yellow_clip = clip2.fl_image(process_image)
yellow_clip.write_videofile(yellow_output, audio=False)


def process_challenge(image):
    settings = ImageSettings()
    settings.width = 1280
    settings.height = 720
    settings.mask_height = 450
    settings.center = 780
    settings.mask_top_width = 50

    return process_image(image, image_settings=settings, extrapolation=False)


yellow_output = 'zuper.mp4'
clip2 = VideoFileClip('challenge.mp4')
yellow_clip = clip2.fl_image(process_challenge)
yellow_clip.write_videofile(yellow_output, audio=False)
