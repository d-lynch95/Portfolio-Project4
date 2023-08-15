from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def booking(request):
    return render(request, 'form.html')