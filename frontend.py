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
    splitted = [0, 0, 0]
    image = [0, 0, 0]

    # generate images from user input
    for i in range(3):
        splitted[i] = audio_path + 'splitted{}.wav'.format(i)

        if choice == 'Chroma':
            generate_spectrograms.gen_Chroma(splitted[i], i)
            image[i] = Image.open(img_path + 'chroma{}.png'.format(i))

        elif choice == 'Tonnetz':
            generate_spectrograms.gen_Tonnetz(splitted[i], i)
            image[i] = Image.open(img_path + 'tonnetz{}.png'.format(i))
        
        elif choice == 'Mel Spectrogram':
            generate_spectrograms.gen_melspectrogram(splitted[i], i)
            image[i] = Image.open(img_path + 'melspec{}.png'.format(i))

    ### show spectrograms to user
    if choice == 'Chroma':
        st.subheader('Chroma Chart')

    elif choice == 'Tonnetz':
        st.subheader('Tonnetz Chart')
        
    elif choice == 'Mel Spectrogram':
            st.subheader('Mel Spectrogram Chart')

    for i in range(3):
        st.image(image[i], use_column_width=True)


    ### show audio clips
    st.subheader('Audio Clips')
    st.write("The audio segments we used to perform the classification:")
    for i in range(3):
        st.audio(splitted[i], format = 'audio/wav')


    # determine the song genre
    all_probs = []
    genres = ['blues','classical','country','disco','hiphop','jazz','metal','pop','reggae','rock']

    for i in range(3):
        all_probs.append(song_predict.predict_song_genre(img_path + 'melspec{}.png'.format(i)))

    genre_probabilities = pd.DataFrame(all_probs)
    avg_probs = genre_probabilities.sum() / 3

    genre_probabilities = pd.DataFrame({
        'genre': genres,
        'probability': avg_probs
    })
    
    best_genre = genre_probabilities['probability'].idxmax()
    st.write("The genre of this song is ...", best_genre, "!")

    # show probabilities
    c = alt.Chart(genre_probabilities).mark_bar().encode(x = 'genre', y = 'probability')
    st.altair_chart(c, use_container_width=True)

else:
    st.write('Awaiting Wave file to be uploaded...') 
