from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
# Do I need both of these views imports?
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

class MakeApptView(LoginRequiredMixin, generic.CreateView):
    def get(self, request):
        form = ApptForm()
        context = {"form": form}
        return render(request, 'form.html', context)

    def get_initial(self):
        initial = super().get_initial()
        initial['name'] = self.request.name
        initial['phone'] = ''
        initial['email'] = self.request.email
        initial['time'] = ''
        initial['date'] = ''
        initial['user'] = self.request.user
        return initial
        # Why does this not work to autofill the form?
    
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

class EditApptView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    form_class = ApptForm
    template_name = 'editform.html'
    success_url = '/posts/'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_pk'] = self.object.pk
        return context

    def form_valid(self, form):
        post = Post.objects.get(pk=self.request.POST['post_pk'])
        form.instance.post = post
        return super().form_valid(form)

class DeleteAppt(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/posts/"