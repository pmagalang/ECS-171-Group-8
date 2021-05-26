import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import sys
import os.path
from pydub import AudioSegment
from PIL import Image


# Paths
sys.path.insert(1, './preprocessing')
sys.path.insert(1, './model')
import wav_splitter
import generate_spectrograms
import song_predict

# imgs & audio path
img_path = os.path.dirname(__file__) + '/output/images/'
audio_path = os.path.dirname(__file__) + '/output/audio/'

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

choice = col1.selectbox('Chart',('Mel Spectrogram', 'Chroma', 'Tonnetz'))

if uploaded_file is not None:

    wav_splitter.wav_split(uploaded_file)
    splitted = audio_path + 'splitted.wav'

    if choice == 'Chroma':
        st.subheader('Chroma Chart')
        generate_spectrograms.gen_Chroma(splitted)
        image = Image.open(img_path + 'chroma.png')

    elif choice == 'Tonnetz':
        st.subheader('Tonnetz Chart')
        generate_spectrograms.gen_Tonnetz(splitted)
        image = Image.open(img_path + 'tonnetz.png')
        
    elif choice == 'Mel Spectrogram':
        st.subheader('Mel Spectrogram Chart')
        generate_spectrograms.gen_melspectrogram(splitted)
        image = Image.open(img_path + 'melspec.png')

    # show spectrogram to user
    st.image(image, use_column_width=True)

    # show audio clip
    st.write("The audio segment we used to analyze")
    st.audio(splitted, format = 'audio/wav')

    # determine song genre
    genre_probabilities = song_predict.predict_song_genre(img_path + 'melspec.png')

    best_genre = max(genre_probabilities, key = genre_probabilities.get)
    st.write("The genre of this song is ...", best_genre, "!")

    # show probabilities
    probs_df = pd.DataFrame(genre_probabilities.items(), columns = ['genre', 'probability'])
    c = alt.Chart(probs_df).mark_bar().encode(x = 'genre', y = 'probability')
    st.altair_chart(c, use_container_width=True)

else:
    st.write('Awaiting Wave file to be uploaded...') 
