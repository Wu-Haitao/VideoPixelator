import cv2
import palette
import numpy as np

# Recolor an image
def recolor(image):
    pixels = image.reshape(-1, 3)
    new_image = np.zeros_like(pixels)
    for i, pixel in enumerate(pixels):
        new_image[i] = palette.get_closest_color(pixel)
    new_image = new_image.reshape(image.shape)
    return new_image

# Downscale an image
def downscale(image, scale):
    width = int(image.shape[1] * scale / 100)
    height = int(image.shape[0] * scale / 100)
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_NEAREST)

# Pixelate an image
def pixelate(image, scale):
    return recolor(downscale(image, scale))