"""
Created by Neel Gokhale at 2020-07-20
File validate.py from project week4_coursera
Built using PyCharm

"""

# NOTE: this is the main file to be executed. All other py files are dependencies or do not require explicit execution.

import os
import numpy as np
from tensorflow.keras.preprocessing import image
from real_world_conv import model


def predict_image_obj():
    """
    Used to predict the neural network model using the `model.predict()` function. Takes a user-selected test image from
    the val-img directory and runs a prediction.
    """

    print("___Validation_Test___")
    print("> Use this program to validate the neural net with actual images...")
    print("> The test images are retrieved from pixabay. Refer to the file names for the image contents")
    print("> The list of available test images are ->")

    for i in range(len(os.listdir('/Users/Owner/PycharmProjects/week4_coursera/img/val_img'))):
        print('  ', i + 1, ":", os.listdir('/Users/Owner/PycharmProjects/week4_coursera/img/val_img')[i])

    img_num = int(input("> Enter the number of the image of choice: "))

    path = '/Users/Owner/PycharmProjects/week4_coursera/img/val_img/' + os.listdir('/Users/Owner/PycharmProjects/week4_coursera/img/val_img')[img_num - 1]
    img = image.load_img(path=path, target_size=(300, 300))
    img_arr = image.img_to_array(img)
    img_arr = np.expand_dims(img_arr, axis=0)
    images = np.vstack([img_arr])

    classes = model.predict(images, batch_size=10)

    print("> Prediction %: " + str(classes[0]))
    if classes[0] > 0.5:
        print("The object in the file is a human")
    else:
        print("The object in the file is a horse")

    return 0


if __name__ == '__main__':
    predict_image_obj()