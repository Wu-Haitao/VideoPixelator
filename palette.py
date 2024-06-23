import kmeans
import numpy as np
import matplotlib.pyplot as plt

color_palette = []

def add_color(color):
    global color_palette
    color_palette.append(color)

def clear_palette():
    global color_palette
    color_palette = []

def sort_colors(colors):
    brightness = np.linalg.norm(colors, axis=1)
    sorted_indices = np.argsort(brightness)
    sorted_colors = colors[sorted_indices]
    return sorted_colors

def generate_palette(pixels, n_colors):
    global color_palette
    unique_pixels, counts = np.unique(pixels, axis=0, return_counts=True)
    palette, _ = kmeans.kmeans(unique_pixels, n_colors, counts)
    color_palette = sort_colors(palette.round(0).astype(int))

def show_palette():
    global color_palette
    plt.figure(figsize=(8, 2))
    plt.imshow([color_palette], aspect='auto')
    plt.title('Color Palette')
    plt.axis('off')
    plt.show()

def get_closest_color(color):
    global color_palette
    distances = np.linalg.norm(color_palette - color, axis=1)
    closest_color = color_palette[np.argmin(distances)]
    return closest_color