import streamlit as st
import pandas as pd
import numpy as np
import sys
import os.path
from pydub import AudioSegment
from PIL import Image


# Paths
sys.path.insert(1, '../Generate Images')
#sys.path.insert(1, '../frontend')
import wave_generator 
import spec_generator
import mel_spectrogram_generator1
import wav_splitter

# imgs & audio path
img_path = os.path.dirname(__file__) + '/../Images/'
audio_path = os.path.dirname(__file__) + '/../Audio/'

st.write("""
# Music Genre Classification App
## ECS171 Group 8 Spring 2021
This app analyzes a song and classifies it into one of the 10 genres
""")

col1 = st.sidebar
col2, col3 = st.beta_columns((2,1))

col1.header('User Input Features')

# Collects user input 
uploaded_file = col1.file_uploader("Upload your wave file", type=["wav"])

choice = col1.selectbox('Chart',('Wave', 'Spectrogram', 'Mel Spectrogram'))

# if uploaded_file is not None:
    # if user uploads a file
    # pass
# else:
#     # if user doesn't upload a file 
#     def get_chart_type():
#         choice = col1.selectbox('Chart',('Wave', 'Spectrogram'))
#         return choice
#     user_selects = get_chart_type()


# Displays the user input features

audio = AudioSegment.from_wav(uploaded_file)

if uploaded_file is not None:
    if audio.duration_seconds > 30:
        #slice song to 30sec
        wav_splitter.wav_split(uploaded_file)
        splitted = audio_path + 'splitted.wav'
    else:
        #file is shorter than 30secs
        splitted = uploaded_file

    if choice == 'Wave':
        st.subheader('Wave Chart')
        wave_generator.visualize_wave(splitted)
        image = Image.open(img_path + 'wave_img.png')

    elif choice == 'Spectrogram':
        st.subheader('Spectrogram Chart')
        spec_generator.visualize_spec(splitted)
        image = Image.open(img_path + 'spec.png')
        
    elif choice == 'Mel Spectrogram':
        st.subheader('Mel Spectrogram Chart')
        mel_spectrogram_generator1.mel_spectrogram(splitted)
        image = Image.open(img_path + 'melspec.png')

    st.image(image, use_column_width=True)
    st.write("The audio segment we used to analyze")
    st.audio(splitted, format = 'audio/wav')
    st.write("The genre of this song is ____!")
            
else:
    st.write('Awaiting Wave file to be uploaded...') 
