import librosa
import numpy as np
import csv
# Run the all sound file and clear data.
audio = "cough.wav"
y, sr = librosa.load(audio, mono=True, duration=1)
# features
chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
zcr = librosa.feature.zero_crossing_rate(y)
mfcc = librosa.feature.mfcc(y=y, sr=sr)
# Clear data and Export to csv
for feature in (chroma_stft, spec_cent, spec_bw, rolloff, zcr, mfcc):
      with open ('feature.csv', 'a') as csvfile:
            cler = np.mean(feature)
            fieldnames = ['Cough']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'Cough':cler})
