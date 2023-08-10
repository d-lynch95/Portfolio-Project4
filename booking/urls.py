from django.urls import path
from . import views

# This is the app directory

urlpatterns = [
    path('', views.book_ticket_view, name='book_ticket'),
]