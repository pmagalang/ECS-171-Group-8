from pydub import AudioSegment
import math
import random

# class SplitWavAudioMubin():
#     def __init__(self, filename):
#         self.filename = filename
        
#         self.audio = AudioSegment.from_wav(self.filename)
    
    # def get_duration(self):
    #     return self.audio.duration_seconds

def wav_split(filename):
    audio = AudioSegment.from_wav(filename)
    total_ms = len(audio)
    total_mins = math.ceil(audio.duration_seconds / 60)
    start = random.randint(5000, total_ms - 35000) # first 5 seconds to last 5 seconds
    end = start + 30000 # take 30 seconds
    split_audio = audio[start:end]
    split_audio.export('output/audio/splitted.wav', format="wav")
    #return split_audio

    # def single_split(self, from_min=1, to_min=1.5, split_filename):
    #     t1 = from_min * 60 * 1000
    #     t2 = to_min * 60 * 1000
    #     split_audio = self.audio[t1:t2]
    #     return split_audio
    #     #split_audio.export(self.folder + '/' + split_filename, format="wav")
        
    # def multiple_split(self, min_per_split):
    #     total_mins = math.ceil(self.get_duration() / 60)
    #     for i in range(0, total_mins, min_per_split):
    #         split_fn = str(i) + '_' + self.filename
    #         self.single_split(i, i+min_per_split, split_fn)
    #         print(str(i) + ' Done')
    #         if i == total_mins - min_per_split:
    #             print('All splited successfully')

