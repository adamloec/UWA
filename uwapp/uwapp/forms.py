from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UWAppUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = UWAppUser
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']