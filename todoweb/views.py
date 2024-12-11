from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserForm


class IndexView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy("todoweb:login")
    template_name = "index.html"
    
class SignupView(FormView):
    template_name = "signup.html"
    form_class = UserForm
    success_url = reverse_lazy("todoweb:login")
    
    def form_valid(self, form):
        password1 = form.cleaned_data["password1"]
        password2 = form.cleaned_data["password2"]
        
        if password1 == password2:
            user = form.save(commit=False)
            user.set_password(password1)
            user.save()
            return super().form_valid(form)
        
        form.add_error("password2", "password doesnt math.")
        return super().form_invalid(form)
    
class LoginViewZ(LoginView):
    redirect_authenticated_user = True
    template_name = "login.html"
    
    def get_success_url(self):
        return reverse_lazy("todoweb:index")