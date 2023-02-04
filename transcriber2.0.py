# imports
import numpy as np

import seaborn
import matplotlib.pyplot as plt
import IPython.display as ipd
from ipywidgets import interactive_output 
from ipywidgets import IntSlider, FloatSlider, fixed, Checkbox
from ipywidgets import VBox, Label

import librosa, librosa.display
from music21.tempo import MetronomeMark
from music21.note import Note, Rest
from music21.stream import Stream
from music21 import metadata
from music21 import instrument
from music21 import midi
from music21.key import Key

# config
path = './music/'

# parameters
fs = 44100                          # sampling frequency
nfft = 2048                         # length of FFT window
overlap = 0.5                       # Hop overlap percentage
hop_length = int(nfft*(1-overlap))  # # of samples between frames
n_bins = 72                         # # of frequency bins
mag_exp = 4                         # magnitude exponent
pre_post_max = 6                    # pre and post samples for peak picking
cqt_threshold = -61                 # Threshold for CQT dB levels

# Loading audio
filename = "%stest.wav"%path
x, fs = librosa.load(filename, sr=None, mono=True, duration=12)

print("x Shape=", x.shape)
print("Sample rat fs=", fs)
print("Audio length in seconds=%d [s]" % (x.shape[0]/fs))

ipd.Audio(x, rate=fs)
