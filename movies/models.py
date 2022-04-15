from tkinter import CASCADE
from django.conf import settings
from django.db import models
# Create your models here.
class Movie(models.Model):
    title           = models.CharField(max_length=20)
    description     = models.TextField()
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content        = models.CharField(max_length=100)
    movie          = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user           = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)


    