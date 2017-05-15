#!/usr/env/python

import sys
import os
import glob

# disable TF debugging info
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from keras.models import load_model as load_keras_model

model_filename = 'model.h5'

def get_filenames():
    images = sys.argv[1:]
    if not images:
        for filename in glob.iglob('data/**/*.*', recursive=True):
            yield filename
    else:
        for filename in images:
            yield "data/{}".format(filename)


def load_model():
    if os.path.exists(model_filename):
        return load_keras_model(model_filename)
    else:
        print("File {} not found!".format(model_filename))
        exit()


def predict(name, model):
    import numpy as np
    from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

    img = load_img("{}".format(name))
    img_arr = img_to_array(img)
    X_test = np.asarray([img_arr])

    result = model.predict(X_test)
    print("{}   {}".format(name, result))


if __name__ == '__main__':
    try:
        filenames = get_filenames()
        keras_model = load_model()
        for filename in filenames:
            predict(filename, keras_model)
    except AttributeError:
        pass
