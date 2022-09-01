from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.forms.widgets import PasswordInput, TextInput

class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate input','placeholder': 'Email / Username'}), label='Email / Username')
    password = forms.CharField(widget=PasswordInput(attrs={'class':'input', 'placeholder':'Password'}))