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
        fields = ['name', 'username', 'email', 'phone', 'date']


class UserPasswordResetForm(SetPasswordForm):
    """Change password form."""
    new_password1 = forms.CharField(label='Password',
                                    help_text="<ul class='errorlist text-muted'><li>Your password can 't be too "
                                              "similar to your other personal information.</li><li>Your password must "
                                              "contain at least 8 characters.</li><li>Your password can 't be a "
                                              "commonly used password.</li> <li>Your password can 't be entirely "
                                              "numeric.<li></ul>",
                                    max_length=100,
                                    required=True,
                                    widget=forms.PasswordInput(
                                        attrs={
                                            'class': 'form-control',
                                            'placeholder': 'password',
                                            'type': 'password',
                                            'id': 'user_password',
                                        }))

    new_password2 = forms.CharField(label='Confirm password',
                                    help_text=False,
                                    max_length=100,
                                    required=True,
                                    widget=forms.PasswordInput(
                                        attrs={
                                            'class': 'form-control',
                                            'placeholder': 'confirm password',
                                            'type': 'password',
                                            'id': 'user_password',
                                        }))


class UserForgotPasswordForm(PasswordResetForm):
    """User forgot password, check via email form."""
    email = forms.EmailField(label='Email address',
                             max_length=254,
                             required=True,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control',
                                        'placeholder': 'email address',
                                        'type': 'text',
                                        'id': 'email_address'
                                        }
                             ))
