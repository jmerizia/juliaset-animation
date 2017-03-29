# Python file containing functions and ability to test

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Function that evaluates julia set shading values at each pixel of a given frame
def juliaeval(img_width, img_height, re_range, im_range, c, max_iterations, frame):

	im = Image.new('L', (img_width, img_height))

	for i in xrange(img_width):
		for j in xrange(img_height):

			# Starting complex parameter at each pixel
			z = complex(re_range[i], im_range[j])

			num_iterations = 0

			while np.absolute(z) < 2 and num_iterations < max_iterations:

				z = np.square(z) + c
				num_iterations += 1

			shade = num_iterations * (360/max_iterations)

			im.putpixel((i,j), shade)

	# Save each frame as a number 0000-9999. Makes for easier creation of gif later
	frame = str(frame).rjust(4, '0')

	im.save('./images/' + frame + '.png')

# Function that defines the path the complex variable will take through 2D space
def cpath(x):

	y = np.square(x)
	return y





# Local testing environment
if __name__ == '__main__':

	re = np.linspace(-2, 2, 400)
	plt.plot(re, cpath(re))
	plt.show()