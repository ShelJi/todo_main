from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"class": "password"}))
    
    class Meta:
        model = User
        fields = ["username", "email"]