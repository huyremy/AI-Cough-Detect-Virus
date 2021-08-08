import os
import wave
import pylab
import warnings
import librosa
import numpy as np
import csv
warnings.simplefilter("ignore", DeprecationWarning)
def graph_spectrogram(wav_file):
    sound_info, frame_rate = get_wav_info(wav_file)
    pylab.figure(num=None, figsize=(10, 5))
    pylab.subplot(111)
    pylab.title('spectrogram of %r' % wav_file)
    pylab.specgram(sound_info, Fs=frame_rate)
    pylab.savefig('spec.png')
def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate
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
            filename = f"{dir_path}/{res}/{files}"
            x, sr = librosa.load(filename, mono=True)
            rmse = librosa.feature.rms(y=x)
            chroma_stft = librosa.feature.chroma_stft(y=x, sr=sr)
            spec_cent = librosa.feature.spectral_centroid(y=x, sr=sr)
            spec_bw = librosa.feature.spectral_bandwidth(y=x, sr=sr)
            rolloff = librosa.feature.spectral_rolloff(y=x, sr=sr)
            zcr = librosa.feature.zero_crossing_rate(x)
            mfcc = librosa.feature.mfcc(y=x, sr=sr)
            to_append = f'{filename} {patient_id} {np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'    
            for k in mfcc:
                to_append += f' {np.mean(k)}'
            to_append += f' {res}'
            file = open(filename, 'a', newline='')
            with file:
                writer = csv.writer(file)
                writer.writerow(to_append.split())
graph_spectrogram('cough.wav')
get_wav_info('cough.wav')
