import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
import subprocess

import functions as f
import setvar as s

if os.path.isdir('./images/') == False:

	os.mkdir('./images')

for frame in xrange(s.num_frames):

	c = complex(s.c_range[frame], f.cpath(s.c_range[frame]))
	f.juliaeval(s.img_width, s.img_height, s.re_range, s.im_range, c, s.max_iterations, frame)

os.chdir('./images/')

p = subprocess.call('bash makegif.sh', shell=True)

subprocess.call('rm *.png', shell=True)
subprocess.call('mv output.gif julia.gif', shell=True)


fig = plt.figure()
plt.plot(s.c_range, f.cpath(s.c_range), markevery=markers_on)
fig.suptitle('Plot of the path of c through the complex plane')
plt.xlabel('Real')
plt.ylabel('Imaginary')
fig.savefig('plot.png')

