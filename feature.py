import librosa
import numpy as np
import csv
# Run the sound file and Clear data.
audio = "cough.wav"
y, sr = librosa.load(audio, mono=True, duration=1)
# features
rmse = librosa.feature.rms(y=x)
chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
zcr = librosa.feature.zero_crossing_rate(y)
mfcc = librosa.feature.mfcc(y=y, sr=sr)
# Clear data and Export to csv
for feature in (rmse, chroma_stft, spec_cent, spec_bw, rolloff, zcr, mfcc):
      with open ('feature.csv', 'a') as csvfile:
            abc = np.mean(feature)
            print(abc)
            fieldnames = ['rmse', 'chroma_stft', 'spec_cent', 'spec_bw', 'rolloff', 'zcr', 'mfcc']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'rmse':np.mean(rmse),
                             'chroma_stft':np.mean(chroma_stft),
                             'spec_cent': np.mean(spec_cent),
                             'spec_bw': np.mean(spec_bw),
                             'rolloff': np.mean(rolloff),
                             'zcr': np.mean(zcr),
                             'mfcc': np.mean(mfcc)})
            break
