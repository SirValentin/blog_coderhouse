import email
from turtle import title
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=200)
    creation_date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    description = models.CharField(max_length=100)

class Advertising(models.Model):
    company = models.CharField(max_length=20)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)