from django.db import models
from django.core.validators import FileExtensionValidator


class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/Slider',
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', ])])

    def __str__(self):
        return self.title
