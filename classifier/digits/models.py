from django.db import models
from PIL import Image
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from django.conf import settings
import os

class Digit(models.Model):
    image = models.ImageField(upload_to='images')
    result = models.CharField(max_length=2, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        img = Image.open(self.image)
        img_array = image.img_to_array(img)
        dim = (28, 28)
        new_img = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(new_img, dim, interpolation=cv2.INTER_AREA)

        ready = np.expand_dims(resized, axis=2)
        ready = np.expand_dims(ready, axis=0)

        try:
            file_model = os.path.join(settings.BASE_DIR, 'cnn_model/CNN_model.h5')
            model = load_model(file_model)
            pred = np.argmax(model.predict(ready))
            self.result = str(pred)

        except:
            print('Failed to classify')
            self.result = 'Failed to classify'

        return super().save(*args, **kwargs)