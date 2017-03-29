import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
import subprocess
import sys

import functions as f
import setvar as s

if os.path.isdir('./images/') == False:

	os.mkdir('./images')

# initialize loading bar:
loading_bar_width = 37
sys.stdout.write("loading: [%s]" % (" " * loading_bar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (loading_bar_width + 1))
previous = -1

for frame in xrange(s.num_frames):

	c = complex(s.c_range[frame], f.cpath(s.c_range[frame]))
	f.juliaeval(s.img_width, s.img_height, s.re_range, s.im_range, c, s.max_iterations, frame)
  
	# log progress:
	new_load_amount = int(((1.0*frame) / s.num_frames)*loading_bar_width)
	if frame is not 0 and new_load_amount is not previous:

		previous = new_load_amount
		sys.stdout.write("#")
		sys.stdout.flush()

sys.stdout.write('\n')

os.chdir('./images/')

p = subprocess.call('bash makegif.sh', shell=True)

subprocess.call('rm *.png', shell=True)
subprocess.call('mv output.gif julia.gif', shell=True)

fig = plt.figure()
plt.plot(s.c_range, f.cpath(s.c_range))
fig.suptitle('Plot of the path of c through the complex plane')
plt.xlabel('Real')
plt.ylabel('Imaginary')
fig.savefig('plot.png')

