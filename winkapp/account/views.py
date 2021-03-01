from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth import login, logout
from django.contrib.admin import forms
from django.urls import reverse_lazy
from . import forms

# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "registration/registration.html"
    
