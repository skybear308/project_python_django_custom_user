# stockprice urls.py

from django.urls import path
from .views import *
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', home, name='home'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('profile/', profile, name='profile'),
]