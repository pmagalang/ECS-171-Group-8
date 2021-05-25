import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import model_from_json
import numpy as np
import cv2

def predict_song_genre(melspec_path, model_json="model/model.json",model_weights="model/model_final_weights.h5" ):
    # load json and create model
    json_file = open(model_json, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights(model_weights)
    print("Loaded model from disk")

    loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

    # image size refitted to 350,230
    image_size = (350,230)
    img = keras.preprocessing.image.load_img(
        melspec_path, target_size=image_size
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create batch axis

    predictions = loaded_model.predict(img_array)
    def get_genre_probabilities(pred_vals):
        info_dict = {}
        genres = ["blues", "country", "hiphop","metal", "reggae",
    "classical", "disco", "jazz","pop","rock"]
        for i in range(len(genres)):
            percent = pred_vals[i] * 100
            info_dict[genres[i]] = percent
        return info_dict

    return get_genre_probabilities(predictions[0])
