import os
from skimage import io
from tensorflow.keras.preprocessing.image import ImageDataGenerator
def data_augmen(img,target_dir):
  datagen = ImageDataGenerator(rotation_range=45,     #Random rotation between 0 and 45
        width_shift_range=0.2,   #% shift
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')
  i = 0
  for batch in datagen.flow(img,
                            batch_size=16,
                            save_to_dir=target_dir,
                            save_prefix='aug',
                            save_format='png'):
    i += 1
    if i > 13:
        break