from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':"Votre nom d'Utilisateur"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':"Entrez votre mot de passe"}))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':"Votre nom d'Utilisateur"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':"Votre adresse mail"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':"Entrez votre mot de passe"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':"Confirmer votre mot de passe"}))