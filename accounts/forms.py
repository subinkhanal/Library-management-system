from django.contrib.auth.forms import UserCreationForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth.models import User
from django import forms
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


class Student(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'username', 'email', 'date']


class BookRequest(forms.ModelForm):
    class Meta:
        model = BookRequest
        fields = ['name', 'username', 'email', 'date']
