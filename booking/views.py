from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib import messages
from .models import Post
from .forms import ApptForm

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('date')
    template_name = 'posts.html'


    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Post.objects.order_by('date')
        else:
            return Post.objects.filter(user=self.request.user).order_by('date')


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
        hide = form.fields['slug']
        hide.widget = hide.hidden_widget()
        return render(request, 'form.html', context)


    def post(self, request):
        form = ApptForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(
            self.request,
            f'Your appointment has been confirmed.')
            return redirect("/posts/")

        else:
            context = {"form": form}
            return render(request, 'form.html', context)

 
class EditApptView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    form_class = ApptForm
    template_name = 'editform.html'
    success_url = '/posts/'

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        form = self.form_class(instance=post)
        messages.success(
            self.request,
            f'Your appointment has been changed.')
        return render(request, "editform.html", {"form": form})


class DeleteAppt(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    messages.success(
            self.request,
            f'Your appointment has been deleted.')
    success_url = "/posts/"
