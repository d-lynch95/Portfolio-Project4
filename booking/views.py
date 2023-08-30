from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import Post
from .forms import ApptForm

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('date')
    template_name = 'posts.html'

def homepage(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def appointment(request):
    return render(request, 'appointment.html')

def posts(request):
    return render(request, 'posts.html')

class MakeApptView(generic.CreateView):
    def get(self, request):
        form = ApptForm()
        context = {"form": form}
        return render(request, 'form.html', context)
    
    def post(self, request):
        form = ApptForm(request.POST)
        if form.is_valid():
            # appt = ApptForm()
            # appt.instance.email = request.user.email
            # appt.instance.name = request.user.username
            # appt.date = form.cleaned_data['date']
            # appt.time = form.cleaned_data['time']
            # appt.user = request.user
            # appt.slug = 'newslug'
            # appt.save()
            form.save()
            return redirect("/posts/")
        else:
            context = {"form": form}
            return render(request, 'form.html', context)

def edit_form(request):
    scheduled = get_object_or_404(Post)
    form = ApptForm(instance=scheduled)
    context = {"form": form}
    return render (request, 'editform.html', context)