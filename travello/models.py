from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Destination(models.Model):

    name = models.CharField(max_length = 255)
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()
    price = models.IntegerField(default=100)
    offer = models.BooleanField(default=False)