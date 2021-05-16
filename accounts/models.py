from django.db import models
from django.utils import timezone


# Books ADD Database Model


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    author = models.CharField(max_length=100, null=False, blank=False)
    quantity = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name, self.author


class Photo(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=False, blank=True)
    image = models.ImageField(null=False, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.description, self.category


class Student(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    username = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, unique=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def __int__(self):
        return self.date


class BookRequest(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    username = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, unique=True)
    date = models.DateTimeField(default=timezone.now)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.cleaned_data = None

    def __str__(self):
        return self.name

    def is_valid(self):
        pass
