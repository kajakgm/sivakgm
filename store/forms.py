from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':"Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':"Password"}))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':"Enter Username"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':"Enter email"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':"Enter password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':"Confirm Password"}))


