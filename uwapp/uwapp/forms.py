from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UWAppUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = UWAppUser
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)