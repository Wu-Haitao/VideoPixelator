import cv2
import palette
import helper
import tkinter as tk
from tkinter import filedialog
import os

def create_palette():
    num_colors = int(entry_color.get())
    file_paths = filedialog.askopenfilenames()
    pixels = helper.read_images(file_paths)
    palette.generate_palette(pixels, num_colors)
    helper.write_palette('palette.txt')

def load_palette():
    file_path = filedialog.askopenfilename()
    if file_path:
        helper.read_palette(file_path) 

def show_palette():
    palette.show_palette()

def extract_frames_from_video():
    video_path = filedialog.askopenfilename()
    output_path = os.path.join(os.getcwd(), 'frames')
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    num_frames = int(entry_frame.get())
    helper.extract_frames(video_path, output_path, num_frames)

def pixelate_frames():
    framse_path = os.path.join(os.getcwd(), 'frames')
    output_path = os.path.join(os.getcwd(), 'frames_pixelated')
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    scale = int(entry_scale.get())
    is_consistent =  (bool)(is_consistent_palette.get())
    if is_consistent:
        helper.pixelate_frames(framse_path, output_path, scale)
    else:
        num_colors = int(entry_color.get())
        helper.pixelate_frames_new_palette(framse_path, output_path, scale, num_colors)


window = tk.Tk()
window.title('Pixelator')

label = tk.Label(window, text='帧间隔:').grid(row=0, column=0, padx=(10, 0), pady=10)
entry_frame = tk.Entry(window, width=5)
entry_frame.insert(0, '1')
entry_frame.grid(row=0, column=1, padx=(0, 10), pady=10)
button = tk.Button(window, text='从视频中提取帧', command=extract_frames_from_video).grid(row=0, column=2, padx=10, pady=10)

line = tk.Label(window, text='-'*50).grid(row=1, column=0, columnspan=3, pady=0)

label = tk.Label(window, text='颜色数量:').grid(row=2, column=0, padx=(10, 0), pady=10)
entry_color = tk.Entry(window, width=5)
entry_color.insert(0, '10')
entry_color.grid(row=2, column=1, padx=(0, 10), pady=10)
button = tk.Button(window, text='生成调色盘', command=create_palette).grid(row=2, column=2, padx=10, pady=10)

button = tk.Button(window, text='加载调色盘', command=load_palette).grid(row=3, column=0, columnspan=2, padx=10, pady=10)
button = tk.Button(window, text='展示调色盘', command=show_palette).grid(row=3, column=2, padx=10, pady=10)

line = tk.Label(window, text='-'*50).grid(row=4, column=0, columnspan=3, pady=0)

label = tk.Label(window, text='尺寸比例:').grid(row=5, column=0, padx=(10, 0), pady=10)
entry_scale = tk.Entry(window, width=5)
entry_scale.insert(0, '50')
entry_scale.grid(row=5, column=1, padx=(0, 10), pady=10)

button = tk.Button(window, text='开始像素化', command=pixelate_frames).grid(row=5, column=2, padx=10, pady=10)
is_consistent_palette = tk.IntVar()
is_consistent_palette.set(1)
checkbox_consistent_palette = tk.Checkbutton(window, text='一致调色盘', variable=is_consistent_palette).grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Start the window
window.mainloop()
