from django.contrib import admin
from .models import Category, Photo, Student

# Register your models here.

admin.site.register(Student)
admin.site.register(Category)
admin.site.register(Photo)
