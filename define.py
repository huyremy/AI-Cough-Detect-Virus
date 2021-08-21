import os
import wave
import pylab
import warnings
import matplotlib.pyplot as plt
import librosa
import numpy as np
import csv
import pathlib
warnings.simplefilter("ignore", DeprecationWarning)
warnings.filterwarnings('ignore')
SR = 44000
N_FFT = 2048
HOP_LENGTH = 512
N_MELS = 60
SILENCE = 0.0018
SAMPLE_LENGTH = 0.5 #s
SAMPLE_SIZE = int(np.ceil(SR*SAMPLE_LENGTH))
NOISE_RATIO = 0.25
def graph_spectrogram(wav_file):
    sound_info, frame_rate = librosa.load(wav_file, mono=True)
    pylab.specgram(sound_info, NFFT=2048, Fs=frame_rate, Fc=0, noverlap=128, cmap='inferno', sides='default', mode='default', scale='dB')
    pylab.axis('off')
    pylab.savefig('huyremy.png')
