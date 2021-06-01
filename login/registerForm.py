from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class RegisterForm(UserCreationForm):
    #name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
    #image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))