from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import Booking
from django.views.generic import ListView, DetailView, UpdateView

def homepage(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def booking(request):
    return render(request, 'form.html')

def appointment(request):
    if request.method== "POST" :
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_date = request.POST['your-date']
        your_message = request.POST['your-message']
        
        return render(request, 'appointment.html', {
            'your_name': your_name,
 			'your_phone': your_phone,
 			'your_email': your_email,
 			'your_address': your_address,
 			'your_schedule': your_schedule,
 			'your_date': your_date,
 			'your_message': your_message
 			}) 
    
    else:
        return render(request, 'home.html', {})

class IndexView(ListView):
    model = booking
    template_name = 'booking/appointment.html'

class SingleView(DetailView):
    model = booking
    template_name = 'booking/single.html'
    context_object_name = 'post'

class PostsView(ListView):
    model = booking
    template_name = 'booking/posts.html'
    context_object_name = 'post_list'

