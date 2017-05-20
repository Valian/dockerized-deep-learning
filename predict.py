#!/usr/env/python
import sys
import os
import glob
import numpy as np

from keras.models import load_model as load_keras_model
from keras.preprocessing.image import img_to_array, load_img

# disable TF debugging info
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

model_filename = 'model.h5'
class_to_name = [
    "Airplane",
    "Automobile",
    "Bird",
    "Cat",
    "Deer",
    "Dog",
    "Frog",
    "Horse",
    "Ship",
    "Truck"
]


def get_filenames():
    glob_patterns = sys.argv[1:]
    if not glob_patterns:
        for filename in glob.iglob('data/**/*.*', recursive=True):
            yield filename
    else:
        for pattern in glob_patterns:
            for filename in glob.iglob('data/' + pattern, recursive=True):
                yield filename


def load_model():
    if os.path.exists(model_filename):
        return load_keras_model(model_filename)
    else:
        print("File {} not found!".format(model_filename))
        exit()


def load_image(filename):
    img_arr = img_to_array(load_img(filename))
    return np.asarray([img_arr])


def predict(image, model):
    result = np.argmax(model.predict(image))
    return class_to_name[result]


if __name__ == '__main__':
    try:
        filenames = get_filenames()
        keras_model = load_model()
        for filename in filenames:
            image = load_image(filename)
            image_class = predict(image, keras_model)
            print("{:30}   {}".format(filename, image_class))
    except AttributeError:
        pass
