from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserForm
from .models import TasksModel


class IndexView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("todoweb:login")
    model = TasksModel
    fields = ["name"]
    template_name = "index.html"
    success_url = reverse_lazy("todoweb:index")
    
    def form_valid(self, form):
        if form.cleaned_data.get("name"):
            form.save()
            return super().form_valid(form)
        return super().form_invalid(form)
              
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
    
class ShowTaskView(ListView):
    template_name = "viewTask.html"
    model = TasksModel
    context_object_name = "tasks" 
    
class DetailTaskView(DetailView):
    template_name = "detail.html"
    model = TasksModel
    context_object_name = "detail"

class UpdateTaskView(UpdateView):
    template_name = "update.html"
    model = TasksModel
    context_object_name = "update"
    
    
    
    