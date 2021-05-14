import librosa
import librosa.display
import matplotlib.pyplot as plt
def mel_spectrogram(wav_file):
    scale, sr = librosa.load(wav_file)
    mel_spec = librosa.feature.melspectrogram(scale, sr=sr,  n_fft = 2048, hop_length = 512, n_mels =10)
    plt.figure(figsize = (25, 10))
    librosa.display.specshow(librosa.power_to_db(mel_spec),
                        x_axis = 'time',
                        y_axis = 'mel')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel spectrogram')
    plt.show()
