from django.shortcuts import render
from django.http import HttpResponse

def book_ticket_view(request):
    return HttpResponse("Hello World")