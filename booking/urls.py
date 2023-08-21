from django.urls import path
from . import views
# This is the app directory

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contact', views.contact, name='contact'),
    path('booking/', views.bookingdata.as_view(), name='booking'),
    path('posts', views.posts, name='posts'),
    path('submit/', views.submit_form, name='submit')
    
]