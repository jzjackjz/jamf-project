from django.db import models

# Create your models here.
class Animal(models.Model):
    genus = models.TextField()
    sound = models.TextField()
    habitat = models.TextField()
    food = models.TextField()
