from django import forms
from django.contrib.auth.models import User

class Register(forms.ModelForm):

    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first name'}))
    last_name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last name'}))
    email = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'email address'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']