"""
Created by Neel Gokhale at 2020-07-20
File real_world_conv.py from project week4_coursera
Built using PyCharm

"""

# NOTE: this neural network model is run by running the validate.py file. Do not run this file unless required.

import os
from get_data import train_horse_dir, train_human_dir
import tensorflow as tf
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Img directory info

train_horse_names = os.listdir(train_horse_dir)
# print(train_horse_names[:10])

train_human_names = os.listdir(train_human_dir)
# print(train_human_names[:10])

len_train_horses = len(train_horse_names)
len_train_humans = len(train_human_names)

# Model

model = tf.keras.models.Sequential([

    # First convolution layer
    tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(300, 300, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    # Second convolution layer
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    # Third convolution layer
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    # Fourth convolution layer
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    # Fifth convolution layer
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    # Dense layers
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')])

model.summary()

# Compile model for training

model.compile(loss='binary_crossentropy',
              optimizer=RMSprop(lr=0.001),
              metrics=['accuracy'])

# Data preprocessing and image generators

train_datagen = ImageDataGenerator(rescale=1./255)
# Training in batches of batch_size = 128 using datagenerator
train_batch_size = 128
train_generator = train_datagen.flow_from_directory(

    # Source dir for images
    '/Users/Owner/PycharmProjects/week4_coursera/img/horse-or-human',
    target_size=(300, 300),
    batch_size=train_batch_size,
    class_mode='binary')

# Training

history = model.fit_generator(
    generator=train_generator,
    steps_per_epoch=len_train_horses/train_batch_size,
    epochs=15,
    verbose=1)