from django.urls import path
from . import views

# This is the app directory

urlpatters = [
    path('', views.homepage, name='homepage')
]