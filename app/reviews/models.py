from django.db import models


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=50, default='empty')
    text = models.CharField(max_length=100)
