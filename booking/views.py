from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import Post

class PostCreateView(CreateView):
    model = Post
    fields = ['name', 'phone', 'email', 'time', 'date', 'user', 'slug']
    template_name = 'post_form.html'