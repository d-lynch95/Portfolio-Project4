from django.urls import path
from . import views

# This is the app directory

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contact', views.contact, name='contact'),
    path('booking', views.booking, name='booking'),
]