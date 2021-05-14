import os
import matplotlib.pyplot as plt

#for loading and visualizing audio files
import sys
import librosa
import librosa.display

#to play audio
import IPython.display as ipd

def visualize(path: str):


    # audio_fpath = "./"
    # audio_clips = os.listdir(audio_fpath)
    # print("No. of .wav files in audio folder = ", len(audio_clips))


    x, sr = librosa.load(path, sr=44100)

    # x, sr = librosa.load(audio_fpath+audio_clips[2], sr=44100)

    print(type(x), type(sr))
    print(x.shape, sr)

    plt.figure(figsize=(14, 5))
    librosa.display.waveplot(x, sr=sr)

    X = librosa.stft(x)
    Xdb = librosa.amplitude_to_db(abs(X))

    # before log transformation 

    # plt.figure(figsize=(14, 5))
    # librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
    # plt.colorbar()
    # plt.savefig('spec_time_hz.png')


    plt.figure(figsize=(14, 5))
    librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
    plt.colorbar()

    plt.savefig('spec_time_log.png')

    plt.show()


if __name__ == "__main__":
    path = sys.argv[1]
    visualize(path)