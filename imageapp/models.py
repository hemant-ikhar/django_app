from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    age = models.IntegerField()


