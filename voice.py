import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import os

def transform(filename, id):
    os.chdir("./static/uploads/")
    print(os.getcwd())
    # print(os.listdir())
    # print(filename)
    pwd = id + '.png'
    signal, sr = librosa.load(filename)
    plt.figure()
    librosa.display.waveshow(signal, sr)
    plt.xlabel('Time(s)')
    plt.ylabel('Amplitude')
    plt.title("Waveform")
    plt.savefig(pwd)
    os.remove(filename)
    os.chdir("../../") #원래 디렉토리 위치로 이동
    return pwd

# os.chdir("./static/uploads/")
# print(os.getcwd())
# print(os.listdir())
# signal, sr = librosa.load('webmtest.webm')
# plt.figure()
# librosa.display.waveshow(signal, sr)
# plt.xlabel('Time(s)')
# plt.ylabel('Amplitude')
# plt.title("Waveform")
# plt.savefig('aaa.png')