from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import Post

class PostCreateView(CreateView):
    model = Post
    fields = ['name', 'phone', 'email', 'time', 'date', 'user', 'slug']
    template_name = 'post_form.html'

def homepage(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def appointment(request):
    return render(request, 'appointment.html')

def form(request):
    return render(request, 'form.html')

def posts(request):
    return render(request, 'posts.html')