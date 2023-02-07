from scipy.fftpack import fft
from scipy.io import wavfile # get the api
import os

import numpy as np

# Configuration
FPS = 30
FFT_WINDOW_SECONDS = 0.25 # how many seconds of audio make up an FFT window

# Note range to display
FREQ_MIN = 10
FREQ_MAX = 1000

# Names of the notes
NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# Output size. Generally use SCALE for higher res, unless you need a non-standard aspect ratio.
RESOLUTION = (1920, 1080)
SCALE = 2 # 0.5=QHD(960x540), 1=HD(1920x1080), 2=4K(3840x2160)


def extract_sample(audio, frame_number, FRAME_OFFSET, FFT_WINDOW_SIZE):
  end = frame_number * FRAME_OFFSET
  begin = int(end - FFT_WINDOW_SIZE)

  if end == 0:
    # We have no audio yet, return all zeros (very beginning)
    return np.zeros((np.abs(begin)),dtype=float)
  elif begin<0:
    # We have some audio, padd with zeros
    return np.concatenate([np.zeros((np.abs(begin)),dtype=float),audio[0:end]])
  else:
    # Usually this happens, return the next sample
    return audio[begin:end]

def find_top_notes(fft, xf):
  if np.max(fft.real)<0.001:
    return []

  lst = [x for x in enumerate(fft.real)]
  lst = sorted(lst, key=lambda x: x[1],reverse=True)

  idx = 0
  found_note = ""
  f = xf[lst[idx][0]]
  y = lst[idx][1]
  n = freq_to_number(f)
  n0 = int(round(n))
  name = note_name(n0)

  if name not in found_note:
    found_note = name
  idx += 1
    
  return found_note


# See https://newt.phys.unsw.edu.au/jw/notes.html
def freq_to_number(f): return 69 + 12*np.log2(f/440.0)
def number_to_freq(n): return 440 * 2.0**((n-69)/12.0)
def note_name(n): return NOTE_NAMES[n % 12] + str(int(n/12 - 1))

def transcribe(AUDIO_FILE):
  filepath = os.path.join('C:/Users/wmpsa/Documents/capstone/Capstone/flask/demo/Tabs', 'Tab.txt')
  if not os.path.exists('C:/Users/wmpsa/Documents/capstone/Capstone/flask/demo/Tabs'):
    os.makedirs('C:/Users/wmpsa/Documents/capstone/Capstone/flask/demo/Tabs')
  file = open(filepath, "+w")

  allowed_extention = {"wav"}
  if AUDIO_FILE == "" :
    return []
  if isinstance(AUDIO_FILE, str) == False:
    return "Input is not String! Enter file name as string"
  if AUDIO_FILE[-4:] != '.wav':
    return "Incorrect file type! This program accepts files of .wav format."
  try:
    fs, data = wavfile.read(AUDIO_FILE) # load the data
  except OSError:

    return "Error! Could not find File in dirctory"

  
  audio = data.T[0] # this is a two channel soundtrack, get the first track
  
  FRAME_STEP = (fs / FPS) # audio samples per video frame
  FFT_WINDOW_SIZE = int(fs * FFT_WINDOW_SECONDS)
  AUDIO_LENGTH = len(audio)/fs

  # Hanning window function
  window = 0.5 * (1 - np.cos(np.linspace(0, 2*np.pi, FFT_WINDOW_SIZE, False)))

  xf = np.fft.rfftfreq(FFT_WINDOW_SIZE, 1/fs)
  FRAME_COUNT = int(AUDIO_LENGTH*FPS)
  FRAME_OFFSET = int(len(audio)/FRAME_COUNT)

  notes = []
  prev_note = None
    
  # Pass 1, find out the maximum amplitude so we can scale.
  mx = 0
  for frame_number in range(FRAME_COUNT):
    sample = extract_sample(audio, frame_number, FRAME_OFFSET, FFT_WINDOW_SIZE)

    fft = np.fft.rfft(sample * window)
    fft = np.abs(fft).real 
    mx = max(np.max(fft),mx)

  # Pass 2, produce the animation
  #for frame_number in tqdm.tqdm(range(FRAME_COUNT)):
   # sample = extract_sample(audio, frame_number, FRAME_OFFSET, FFT_WINDOW_SIZE)

    #fft = np.fft.rfft(sample * window)
    #fft = np.abs(fft) / mx
       
    s = find_top_notes(fft, xf)

    # removes blank notes and duplicate readings of notes
    if s != []:
      if notes != []:
        if prev_note != s:
          notes.append(s)
      else:
        notes.append(s)

    prev_note = s
  Notes  = ", ".join(notes)
  file.write(Notes)
  return notes

# prints the list of notes
print(transcribe("test.wav"))

  
