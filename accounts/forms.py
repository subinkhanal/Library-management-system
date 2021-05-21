from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm

from .models import *
from django.contrib.auth import get_user_model

user = get_user_model()


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'date_joined', 'is_staff', 'password1', 'password2']


class BookForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'author', 'quantity']


class Photo(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['category', 'image', 'description']


class Post(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'



