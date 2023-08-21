from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .models import Booking
from django.views.generic import ListView, DetailView, UpdateView, CreateView

def homepage(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def booking(request):
    return render(request, 'form.html')

def posts(request):
    return render(request, 'posts.html')

# def booking_list(request):
#     bookings = Booking.objects.all()
#     return render(request, 'booking.html', {'bookings': bookings})

def appointment(request):
    if request.method == "POST" :
        title = request.POST['title']
        excerpt = request.POST['excerpt']
        author = request.POST['author']
        updated = request.POST['updated']
        published = request.POST['published']
        
        return render(request, 'appointment.html', {
            'title': title,
            'excerpt': excerpt,
            'author': author,
            'updated': updated,
            'published': published
            
 			}) 
    
    else:
        return render(request, 'home.html', {})

class IndexView(ListView):
    model = Booking
    template_name = 'appointment.html'

class bookingdata(CreateView):
    model = Booking
    fields = ['title', 'excerpt', 'author', 'updated', 'published']
