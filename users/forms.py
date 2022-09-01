from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.forms.widgets import PasswordInput, TextInput
from phonenumber_field.formfields import PhoneNumberField
from betterforms.multiform import MultiModelForm
from users.models import Profile


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'validate input','placeholder': 'Email / Username'}), label='Email / Username')
    password = forms.CharField(widget=PasswordInput(attrs={'class':'input', 'placeholder':'Password'}))

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']


class ProfileForm(forms.ModelForm):
    phone_number = PhoneNumberField()

    class Meta:
        model = Profile
        fields = ['phone_number','gender', 'address', 'occupation', 'course', 'branch', 'year_of_passing',]


class UserCreationMultiForm(MultiModelForm):
    form_classes = {
        'user': UserRegisterForm,
        'profile': ProfileForm,
    }