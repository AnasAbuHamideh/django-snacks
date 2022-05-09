from pydoc import describe
from django.db import models

# Create your models here.

class Snack(models.Model):
    name = models.CharField(max_length=255)
    describition = models.TextField()

    def __str__(self):
        return self.name