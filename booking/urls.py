from django.urls import path
from . import views

# This is the app directory

urlpatterns = [
    path('hello/', views.hello_view, name='hello'),
]