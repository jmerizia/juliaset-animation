'''
Creates variables from user input
Lots of variables to input so containing the code in
a separate file is ideal
'''

import numpy as np

# defaults values:
img_width = 100
img_height = 100
re_min = -2.0
re_max = -2.0
im_min = -2.0
im_max = -2.0
max_iterations = 50
num_frames = 105
c_start = -1.0
c_end = 1.0

use_defaults = raw_input('Use defaults? [y]es or [n]o: ')

if use_defaults not in ['y', 'Y', 'Yes', 'yes', '1']:
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

print 'This may take a while...'

re_range = np.linspace(re_min, re_max, img_width)
im_range = np.linspace(im_min, im_max, img_height)

c_range = np.linspace(c_start, c_end, num_frames)
