from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
# Create your views here.


def home(request):
    template_name = 'registration/login.html'
    template_vars = {}
    return render(request, template_name, template_vars)

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    
def profile(request):
    template_name = "profile.html"
    template_vars = {}
    return render(request, template_name, template_vars)