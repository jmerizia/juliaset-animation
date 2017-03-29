Python program to output animations of julia sets

The program iterates over each pixel of a frame and changes the c variable via a predefined function. Current implementation is slow, as iterating over numpy arrays is incredibly slow in python. Possible C++ or cython implementations of the code would drastically improve performance. 

Make sure ffmpeg is installed before running the program, as it relies on running a bash script which runs ffmpeg to create the output gif.
