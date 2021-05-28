from pydub import AudioSegment
import random

def wav_split(filename):
    audio = AudioSegment.from_wav(filename)
    if audio.duration_seconds < 35:
        split_audio = audio
        split_audio.export('output/audio/splitted.wav', format="wav")
    else:
        total_ms = len(audio)

        for i in range(3):
            start = random.randint(5000, total_ms - 35000) # exclude first 5 seconds and last 5 seconds
            end = start + 30000 # take 30 seconds
            split_audio = audio[start:end]
            split_audio.export('output/audio/splitted{}.wav'.format(i), format="wav")
        


