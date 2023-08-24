from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, UpdateView, CreateView

class MyCreateView(CreateView):
    model = booking
    form_class = MyForm