from django.urls import path
from . import views

# This is the app directory

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contact/', views.contact , name='contact'),
    path('appointment/', views.appointment, name='appointment'),
    path('form/', views.MakeApptView.as_view(), name='form'),
    path('posts/', views.PostList.as_view(), name="PostList"),
    path('edit/<int:pk>/', views.EditApptView.as_view(), name='edit'),
    path('delete/', views.DeleteAppt.as_view(), name='delete'),
 ]