import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from moviepy.editor import *

c_re = float(raw_input('Enter real part of complex parameter: '))
c_im = float(raw_input('Enter imaginary part of complex parameter: '))
c = complex(c_re, c_im)

img_width = int(raw_input('Enter width of image: '))
img_height = int(raw_input('Enter height of image: '))

re_min = float(raw_input('Enter minimum real value: '))
re_max = float(raw_input('Enter maximum real value: '))

im_min = float(raw_input('Enter minimum imaginary value: '))
im_max = float(raw_input('Enter maximum imaginary value: '))

#re_delta = float(raw_input('Enter real delta: '))
#im_delta = float(raw_input('Enter imaginary delta: '))
#num_frames = int(raw_input('Enter number of frames to draw: '))

re_range = np.linspace(re_min, re_max, num=img_width)
im_range = np.linspace(im_min, im_max, num=img_height)

max_iterations = 50

def juliaeval(img_width, img_height, re_range, im_range, c, frame):

	im = Image.new('L',(img_width,img_height))

	for i in xrange(img_width):
		for j in xrange(img_height):

			z = complex(re_range[i], im_range[j])
			num_iterations = 0

			while np.absolute(z) < 2 and num_iterations < max_iterations:

				z = np.square(z) + c
				num_iterations += 1

			shade = num_iterations * (360/max_iterations)

			im.putpixel((i,j), shade)
		
	frame = str(frame).rjust(4, '0')
 		
	im.save('./images/'+frame+'.png')
	 		

def cpath(x):

	y = np.square(x)
	return y

for n in xrange(num_frames):

	juliaeval(img_width, img_height, re_range, im_range, c, n)
	c = c + complex(re_delta, im_delta)	

