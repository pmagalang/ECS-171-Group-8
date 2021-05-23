import os 
from skimage import io, color
from skimage.transform import resize

def get_data(filepath):
    genres = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']

    # use to translate from integers to labels
    int_translator = {}
    for i, genre in enumerate(genres):
        int_translator[i] = genre

    # Load files
    image_list = []
    labels = []

    for label, genre in enumerate(genres):
        list_files = os.listdir(filepath + '/' + genre)
        for filename in list_files:
            image_list.append(io.imread(filepath + '/' + genre + '/' + filename))
            labels.append(label)

    return (int_translator, image_list, labels)

def image_processor(images):

    def process(image):
        #image = color.rgba2rgb(image)
        #image = color.rgb2gray(color.rgba2rgb(img))
        #image = resize(image, (235,500))
        image = image.reshape(-1)
        return image
    
    return [process(image) for image in images]

# flatten images
