import numpy as np
import sounddevice as sd
import scipy.fftpack
import os 
from contextlib import suppress
import copy
import time


"""
Guitar tuner using HPS(Harmonic Product Spectrum) method
Sources: https://www.chciken.com/digital/signal/processing/2020/05/13/guitar-tuner.html

"""

SAMPLE_FREQ = 44100 # sample frequency in Hz
WINDOW_SIZE = 44100 # window size of the DFT in samples
WINDOW_STEP = 21050 # step size of window
WINDOW_T_LEN = WINDOW_SIZE / SAMPLE_FREQ # length of the window in seconds
SAMPLE_T_LENGTH = 1 / SAMPLE_FREQ # length between two samples in seconds
#windowSamples = [0 for _ in range(WINDOW_SIZE)]
HPS = 5
POWER_THRESH = 1e-5
CONCERT_PITCH = 440
WHITE_NOISE_THRESH = 0.4

WINDOW_T_LEN = WINDOW_SIZE / SAMPLE_FREQ
DELTA_FREQ = SAMPLE_FREQ/WINDOW_SIZE
OCTAVE_BANDS = [50,100,200,400,800,1600,3200,6400,12800,25600]
STANDARD_PITCH = 440

NOTES = ["A","A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
HANN_WINDOW = np.hanning(WINDOW_SIZE)


#chooseClosestNote function picks the closest note to the frequency reading  -- takes a pitch as an  input and outputs closest_note , closest_pitch
def chooseClosestNote(pitch): 
    i = int(np.round(np.log2(pitch/STANDARD_PITCH)*12))
    closest_note = NOTES[i%12]+ str(4 + (i+9)//12)
    closest_pitch = STANDARD_PITCH*2**(i/12)
    return closest_note, closest_pitch


#displayTuner takes input stream of audio and outputs the frequency result -- this is what we will use to see if the note we want is in tune or not 
def displayTuner(indata, frames, time, status): 
    
    
    if not hasattr(displayTuner, "windowSamples"):
        displayTuner.windowSamples = [0 for _ in range(WINDOW_SIZE)]
    if not hasattr(displayTuner, "noteBuffer"):
        displayTuner.noteBuffer = ["1","2"]
        
    

    if status:
        print(status)
        return
    if any(indata):
        displayTuner.windowSamples = np.concatenate((displayTuner.windowSamples, indata[:,0]))
        displayTuner.windowSamples = displayTuner.windowSamples[len(indata[:,0]):]
        

        signal_power = (np.linalg.norm(displayTuner.windowSamples, ord=2)**2) / len(displayTuner.windowSamples)
        if signal_power < POWER_THRESH:
            os.system('cls' if os.name =='nt' else 'clear')
            print(f"Closest Note ... ")
            return 
        hann_samples = displayTuner.windowSamples * HANN_WINDOW
        magnitudeSpec = abs(scipy.fftpack.fft(hann_samples)[:len(hann_samples)//2])
        

        for i in range(int(62/DELTA_FREQ)):
            magnitudeSpec[i] = 0
        
        for j in range(len(OCTAVE_BANDS)-1):
            ind_start = int(OCTAVE_BANDS[j]/DELTA_FREQ)
            ind_end = int(OCTAVE_BANDS[j+1]/DELTA_FREQ)
            ind_end = ind_end if len(magnitudeSpec) > ind_end else len(magnitudeSpec)
            avg_energy_per_freq = (np.linalg.norm(magnitudeSpec[ind_start:ind_end], ord=2)**2)/(ind_end - ind_start) 
            avg_energy_per_freq = avg_energy_per_freq**0.5
            for i in range(ind_start, ind_end):
                magnitudeSpec[i] = magnitudeSpec[i] if magnitudeSpec[i] > WHITE_NOISE_THRESH*avg_energy_per_freq else 0

        mag_spec_ipol = np.interp(np.arange(0, len(magnitudeSpec), 1/HPS), np.arange(0,len(magnitudeSpec)), magnitudeSpec)

        mag_spec_ipol = mag_spec_ipol / np.linalg.norm(mag_spec_ipol, ord=2) #normalize

        hps_spec = copy.deepcopy(mag_spec_ipol)

        for i in range(HPS):
            tmp_hps_spec = np.multiply(hps_spec[:int(np.ceil(len(mag_spec_ipol)/(i+1)))], mag_spec_ipol[::(i+1)])
            if not any(tmp_hps_spec):
                break
            hps_spec = tmp_hps_spec

        maxInd = np.argmax(hps_spec)
        maxFreq = maxInd * (SAMPLE_FREQ/WINDOW_SIZE) / HPS
        closest_note, closest_pitch = chooseClosestNote(maxFreq)
        print("closest pitch is: {}".format(closest_pitch))
        maxFreq = round(maxFreq, 1)
        closest_pitch = round(closest_pitch, 1)

        displayTuner.noteBuffer.insert(0, closest_note)
        displayTuner.noteBuffer.pop()

        os.system('cls' if os.name=='nt' else 'clear')
        if displayTuner.noteBuffer.count(displayTuner.noteBuffer[0]) == len(displayTuner.noteBuffer):
            print(f"Closest note: {closest_note} {maxFreq}/{closest_pitch}")
        else:
            print(f"Closest note: ...")

    else:
        print('no input')     

with suppress(Exception):
    print("Starting HPS guitar tuner...")
    with sd.InputStream(channels=1, callback=displayTuner, blocksize=WINDOW_STEP, samplerate=SAMPLE_FREQ):
        while True:
            time.sleep(0.5)