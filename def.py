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
    pylab.savefig('file.png')
def spec_wav():
    results = ['positive', 'negative']
    for res in results: 
        pathlib.Path(f"spectrograms/{res}").mkdir(parents=True, exist_ok=True)
        for files in os.listdir(f"data/{res}"):
            filename = f"data/{res}/{files}"
            print(filename)
            x, sr = librosa.load(filename, mono=True)
            plt.specgram(x, NFFT=2048, Fs=2, Fc=0, noverlap=128, cmap='inferno', sides='default', mode='default', scale='dB');
            plt.axis('off');
            plt.savefig(f"spectrograms/{res}/{files[:-4]}.png")
            plt.clf()
def write_to_csv(filename='dataset.csv', dir_path='data'):
    #Create the header for the CSV File 
    header = 'filename ID chroma_stft rmse spectral_centroid spectral_bandwidth rolloff zero_crossing_rate'
    for x in range(1, 21):
        header += f" mfcc{x}"
    header += ' label'
    header = header.split()
    #create and write to file
    file = open(filename, 'w', newline="")
    with file: 
        writer = csv.writer(file)
        writer.writerow(header)
    results = ['positive', 'negative']
    for res in results: 
        for files in os.listdir(f"{dir_path}/{res}"):
            patient_id = files.split("_")[0]
            filenames = f"{dir_path}/{res}/{files}"
            print(filenames)
            x, sr = librosa.load(filenames, mono=True)
            rmse = librosa.feature.rms(y=x)
            chroma_stft = librosa.feature.chroma_stft(y=x, sr=sr)
            spec_cent = librosa.feature.spectral_centroid(y=x, sr=sr)
            spec_bw = librosa.feature.spectral_bandwidth(y=x, sr=sr)
            rolloff = librosa.feature.spectral_rolloff(y=x, sr=sr)
            zcr = librosa.feature.zero_crossing_rate(x)
            mfcc = librosa.feature.mfcc(y=x, sr=sr)
            to_append = f'{filenames} {patient_id} {np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'    
            for k in mfcc:
                to_append += f' {np.mean(k)}'
            to_append += f' {res}'
            file = open(filename, 'a', newline='')
            with file:
                writer = csv.writer(file)
                writer.writerow(to_append.split())
graph_spectrogram('cough.wav')
#write_to_csv()
#spec_wav()
