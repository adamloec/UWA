from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import UWAppUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(error_messages={'required': 'Please enter your email address.', 'unique': 'An account with this email address already exists.'})
    username = forms.CharField(error_messages={'required': 'Please enter your username.', 'unique': 'An account with this username already exists.'})
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, error_messages={'required': 'Please enter your password.'})
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput, error_messages={'required': 'Please confirm your password.'})

    class Meta:
        model = UWAppUser
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True, error_messages={'required': 'Username is required.'})
    password = forms.CharField(widget=forms.PasswordInput, required=True, error_messages={'required': 'Password is required.'})

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise ValidationError('Invalid username or password.')