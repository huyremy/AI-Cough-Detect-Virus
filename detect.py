import os
import wave
import pylab
import warnings
import matplotlib.pyplot as plt
import librosa
import numpy as np
import csv
import pathlib
import argparse
from define import *
from check import*
def get_args():
    parser = argparse.ArgumentParser(prog="Phát hiện virus qua tiếng ho",description="Detect Virus via Cough Sound")
    parser.add_argument('-w', '--wav', type=str, default='cough.wav',help='Đường dẫn đến file wav chứa tiếng ho.')
    args = parser.parse_args()
    return args
cough = load_model('cough.hdf5')
if __name__ == '__main__':
    args = get_args()
    graph_spectrogram(args.wav)
print("Convert done. AI đang kiểm tra. Vui lòng đợi trong giây lát.")
output(cough,'huyremy.png',(224,224))
os.remove("huyremy.png") 
