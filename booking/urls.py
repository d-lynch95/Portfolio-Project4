from django.urls import path
from . import views

# This is the app directory

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contact.html', views.contact , name='contact'),
]