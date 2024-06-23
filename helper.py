import palette
import pixelator
import cv2
import os
from rich.progress import track
import numpy as np

# Read images
def read_images(file_paths):
    pixels = np.zeros((0, 3))
    for file_path in file_paths:
        if file_path:
            image = cv2.imread(file_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            pixels = np.concatenate((pixels, image.reshape(-1, 3)))
    return pixels

# Write palette to txt file
def write_palette(file_path):
    with open(file_path, 'w') as file:
        for color in palette.color_palette:
            file.write(f'{color[0]},{color[1]},{color[2]}\n')
    print('Palette saved to', file_path)

# Read palette from txt file
def read_palette(file_path):
    palette.clear_palette()
    with open(file_path, 'r') as file:
        for line in file:
            color = [int(x) for x in line.strip().split(',')]
            palette.add_color(color)
    print('Palette loaded from', file_path)

# Extract frames from video
def extract_frames(video_path, output_path, frame_rate=1):
    video = cv2.VideoCapture(video_path)
    count = 0
    frame_count = 0
    while True:
        success, image = video.read()
        if not success:
            break
        if count % frame_rate == 0:
            cv2.imwrite(f'{output_path}/{frame_count}.png', image)
            frame_count += 1
        count += 1
    video.release()
    print('Frames extracted to', output_path)

# Pixelate frames
def pixelate_frames(input_path, output_path, scale):
    for file_name in track(os.listdir(input_path)):
        if file_name.endswith('.png'):
            image = cv2.imread(f'{input_path}/{file_name}')
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            pixelated_image = pixelator.pixelate(image, scale)
            pixelated_image = cv2.cvtColor(pixelated_image, cv2.COLOR_RGB2BGR)
            cv2.imwrite(f'{output_path}/{file_name}', pixelated_image)
    print('Frames pixelated to', output_path)

# Pixelate frames, creating a new palette for each frame
def pixelate_frames_new_palette(input_path, output_path, scale, num_colors):
    for file_name in track(os.listdir(input_path)):
        if file_name.endswith('.png'):
            image = cv2.imread(f'{input_path}/{file_name}')
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            pixels = image.reshape(-1, 3)
            palette.clear_palette()
            palette.generate_palette(pixels, num_colors)
            pixelated_image = pixelator.pixelate(image, scale)
            pixelated_image = cv2.cvtColor(pixelated_image, cv2.COLOR_RGB2BGR)
            cv2.imwrite(f'{output_path}/{file_name}', pixelated_image)
    print('Frames pixelated to', output_path)