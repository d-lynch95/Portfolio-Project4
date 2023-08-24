from django.urls import path
from . import views

# This is the app directory

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contact', views.contact , name='contact'),
    path('appointment', views.appointment, name='appointment'),
    path('form', views.form, name='form'),
    path('posts', views.posts, name='posts'),
]