import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import os

print("Ho đi nào, máy sẽ ghi âm tiếng ho trong vòng 5 giây")
freq = 44000
  
duration = 5
  
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

sd.wait()
  
write("recording0.wav", freq, recording)
  
wv.write("recording1.wav", recording, freq, sampwidth=2)
print("Ghi âm xong rồi đấy. Đợi tí kiểm tra luôn.")
print("Đợi tầm 1 phút đến 3 phút nữa là sẽ có kết quả. Máy chậm là nó sẽ hơi lâu.")
cmd = "python3 detect.py -w recording0.wav"
a=os.system(cmd)

print("Xong")
