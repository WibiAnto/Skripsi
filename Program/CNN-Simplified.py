import urllib.request
import zipfile
import tensorflow as tf
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import RMSprop

class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if (logs.get('accuracy') > 0.95 and logs.get('val_accuracy') > 0.92):
            self.model.stop_training = True

TRAINING_DIR = 'data/horse-or-human'
train_datagen = ImageDataGenerator(rescale=1/255)

train_generator = train_datagen.flow_from_directory(directory=TRAINING_DIR,
                                                    batch_size=32,
                                                    class_mode="binary",
                                                    target_size=(150,150))
VALIDATION_DIR = 'data/validation-horse-or-human'
val_datagen = ImageDataGenerator(rescale=1/255)

# YOUR IMAGE SIZE SHOULD BE 150x150
val_generator = val_datagen.flow_from_directory(directory=VALIDATION_DIR,
                                                batch_size=32,
                                                class_mode="binary",
                                                target_size=(150,150))
model=tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
    ])
model.compile(optimizer=RMSprop(learning_rate=0.001),
              loss="binary_crossentropy",
              metrics=["accuracy"])
model.fit(train_generator,
          epochs=20,
          verbose=1,
          validation_data=val_generator,
          callbacks=[myCallback()])