from django.db import models
from PIL import Image
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image

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
        return super().save(*args, **kwargs)