from django.urls import path
from . import views
# This is the app directory

urlpatterns = [
    path('', views.homepage, name='homepage'),
    #path('appointment', views.IndexView.as_view(), name='appointment'),
    path('contact', views.contact, name='contact'),
    path('booking/', views.booking, name='booking'),
    path('appointment', views.appointment, name='appointment'),
    path('posts', views.posts, name='posts'),
    path('', bookingdata.as_view(), name='bookingdata' ),
]