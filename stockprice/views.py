from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


def home(request):
    template_name = 'home/login.html'
    template_vars = {}
    return render(request, template_name, template_vars)