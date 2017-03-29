'''
Creates variables from user input
Lots of variables to input so containing the code in
a separate file is ideal
'''

import numpy as np

img_width = int(raw_input('Enter image width: '))
img_height = int(raw_input('Enter image height: '))
re_min = float(raw_input('Enter minimum real value: '))
re_max = float(raw_input('Enter maximum real value: '))
im_min = float(raw_input('Enter minimum imaginary value: '))
im_max = float(raw_input('Enter maximum imaginary value: '))
max_iterations = int(raw_input('Enter maximum iterations per pixel: '))
num_frames = int(raw_input('Enter the number of frames to draw: '))
c_start = float(raw_input('Enter real value of starting c: '))
c_end = float(raw_input('Enter real value of ending c: '))

re_range = np.linspace(re_min, re_max, img_width)
im_range = np.linspace(im_min, im_max, img_height)

c_range = np.linspace(c_start, c_end, num_frames)