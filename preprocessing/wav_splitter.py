from pydub import AudioSegment
import random

def wav_split(filename):
    audio = AudioSegment.from_wav(filename)
    total_ms = len(audio)
    start = random.randint(5000, total_ms - 35000) # first 5 seconds to last 5 seconds
    end = start + 30000 # take 30 seconds
    split_audio = audio[start:end]
    split_audio.export('output/audio/splitted.wav', format="wav")

