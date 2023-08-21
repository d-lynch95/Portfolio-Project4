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

def submit_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')

    else: form = MyForm()

    return render(request, index.html, {'form': form})

class IndexView(ListView):
    model = Booking
    template_name = 'posts.html'

class bookingdata(CreateView):
    model = Booking
    fields = ['title', 'excerpt', 'author', 'published']
    template_name = 'form.html'
