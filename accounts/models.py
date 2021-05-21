from django.contrib.auth.models import User
from django.db import models


# Books ADD Database Model


class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False)
    author = models.CharField(max_length=100, null=True, blank=False, default=False)
    quantity = models.CharField(max_length=100, null=True, blank=False)

    def __str__(self):
        return self.name, self.author


class Photo(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=False, blank=True)
    image = models.ImageField(null=False, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.description, self.category


class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    content = models.TextField(default=False)
