import math
import numpy as np
import scipy.io.wavfile
#import matplotlib.pyplot as plt

PATH = "sinesweep.wav"
Fs = 48000
bits = 16
Fstart = 10

reqTime = 60

y = np.array([math.sin(2 * math.pi * 2 * Fstart ** (((4 * n) / (reqTime * Fs)) + 1)) for n in range(1, reqTime * Fs + 1)])

#plt.stem(y)
#plt.show()

scaled = y / np.max(np.abs(y)) * (2 ** (bits - 1))
scaled = np.int16(scaled)

scipy.io.wavfile.write(PATH, Fs, scaled)