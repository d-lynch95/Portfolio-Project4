from django.urls import path
from . import views
# This is the app directory

urlpatterns = [
    path('', index.html , name="home"),
]