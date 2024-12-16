from django.db import models

# Create your models here.
class Item(models.Model):
    username = models.CharField(max_length=100)
    created_datetime = models.DateField()
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=500)
