import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

def gen_melspectrogram(wav_file):
    y, sr = librosa.load(wav_file)
    mel_spect = librosa.feature.melspectrogram(y=y, sr=sr,  n_fft = 2048, hop_length = 1024)
    mel_spect = librosa.power_to_db(mel_spect, ref=np.max)
    librosa.display.specshow(mel_spect, fmax=8000)
    
    plt.axis('off')
    plt.savefig('output/images/melspec.png', bbox_inches="tight", pad_inches = 0, transparent = True)

def gen_Tonnetz(wav_file):
    y, sr = librosa.load(wav_file)
    y = librosa.effects.harmonic(y)
    tonnetz = librosa.feature.tonnetz(y=y, sr=sr)
    librosa.display.specshow(tonnetz)
    plt.axis('off')
    plt.savefig('output/images/tonnetz.png', bbox_inches="tight",pad_inches = 0,transparent=True)

def gen_Chroma(wav_file):
    y, sr = librosa.load(wav_file)
    y = librosa.effects.harmonic(y)
    librosa.display.specshow(librosa.feature.chroma_cqt(y, sr=sr), y_axis='chroma', x_axis='time')
    plt.axis('off')
    plt.savefig('output/images/chroma.png', bbox_inches="tight",pad_inches = 0,transparent=True)
