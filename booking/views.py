from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import Booking
from django.views.generic import ListView, DetailView, UpdateView, CreateView
