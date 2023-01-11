import numpy as np
import sounddevice as sd
import scipy.fftpack
import os 

SAMPLE_FREQ = 44100 # sample frequency in Hz
WINDOW_SIZE = 44100 # window size of the DFT in samples
WINDOW_STEP = 21050 # step size of window
WINDOW_T_LEN = WINDOW_SIZE / SAMPLE_FREQ # length of the window in seconds
SAMPLE_T_LENGTH = 1 / SAMPLE_FREQ # length between two samples in seconds
windowSamples = [0 for _ in range(WINDOW_SIZE)]

STANDARD_PITCH = 440

NOTES = ["A","A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

def chooseClosestNote(pitch):
    i = int(np.round(np.log2(pitch/STANDARD_PITCH)*12))
    closest_note = NOTES[i%12]+ str(4 + (i+9)//12)
    closest_pitch = STANDARD_PITCH*2**(i/12)
    return closest_note, closest_pitch


def callback(indata, frames, time, status):
    global windowSamples
    if status:
        print(status)
    if any(indata):
        windowSamples = np.concatenate((windowSamples, indata[:,0]))
        windowSamples = windowSamples[len(indata[:,0]):]
        magnitudeSpec = abs(scipy.fftpack.fft(windowSamples)[:len(windowSamples)//2] )

        for i in range(int(62/SAMPLE_FREQ/WINDOW_SIZE)):
            magnitudeSpec[i] = 0
        maxInd = np.argmax(magnitudeSpec)
        maxFreq = maxInd * (SAMPLE_FREQ/WINDOW_SIZE)

        closest_note, closest_pitch = chooseClosestNote(maxFreq)

        os.system('cls' if os.name =='nt' else 'clear')
        print(f"Closest Note: {closest_note} {maxFreq:.1f}/{closest_pitch:.1f}")
    else:
        print("no input")

try:
    with sd.InputStream(channels=1, callback=callback, blocksize=WINDOW_STEP, samplerate=SAMPLE_FREQ):
        while True:
            pass
except Exception as e:
    print(str(e))