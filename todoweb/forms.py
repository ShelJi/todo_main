from django.contrib.auth.models import User
from django import forms

# from django.views.generic import CreateView

# from .models import TasksModel


class UserForm(forms.ModelForm):
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"class": "password"}))
    
    class Meta:
        model = User
        fields = ["username", "email"]
        