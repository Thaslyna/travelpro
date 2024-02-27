from django.db import models


# Create your models here.

class Destination(models.Model):
    img = models.ImageField(upload_to='pics')
    header = models.CharField(max_length=200)
    desc = models.TextField()

    def __str__(self):
        return self.header
