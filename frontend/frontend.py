import streamlit as st
import pandas as pd
import numpy as np
import sys
import os.path
from PIL import Image


# Paths
sys.path.insert(1, '../Generate Images')
import wave_generator 
import spec_generator

# imgs path
img_path = os.path.dirname(__file__) + '/../Images/'
st.write("""
# Music Genre Classification App
This app analyzes a song and classifies it into one of the genres
""")

col1 = st.sidebar
col2, col3 = st.beta_columns((2,1))

col1.header('User Input Features')

# Collects user input 
uploaded_file = col1.file_uploader("Upload your wave file", type=["wav"])

choice = col1.selectbox('Chart',('Wave', 'Spectrogram'))

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


if uploaded_file is not None:
    if choice == 'Wave':
        st.subheader('Wave Chart')
        wave_generator.visualize_wave(uploaded_file)
        image = Image.open(img_path + 'wave_img.png')

    elif choice == 'Spectrogram':
        st.subheader('Spectrogram Chart')
        spec_generator.visualize_spec(uploaded_file)
        image = Image.open(img_path + 'spec.png')

    st.image(image, use_column_width=True)
            
else:
    st.write('Awaiting Wave file to be uploaded...') 
