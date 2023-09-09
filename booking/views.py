from django.contrib import messages
from .models import Post
from .forms import ApptForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

# This class loads the different appointments
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('date')
    template_name = 'posts.html'

    # Users can only see their own appointments. Staff can see all 
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Post.objects.order_by('date')
        else:
            return Post.objects.filter(user=self.request.user).order_by('date')


# Sends users to the homepage
def homepage(request):
    return render(request, 'index.html')


# Sends users to the contact us page
def contact(request):
    return render(request, 'contact.html')


# Sends users to the posts page where appointments are stored
def posts(request):
    return render(request, 'posts.html')


# Allow users to create appointments
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


# Allow users to edit their appointments
class EditApptView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    form_class = ApptForm
    template_name = 'editform.html'
    success_url = '/posts/'

    # def form_valid(self, form):
    #     name = form.cleaned_data['name']
    #     phone = form.cleaned_data['phone']
    #     email = form.cleaned_data['email']
    #     date = form.cleaned_data['date']
    #     time = form.cleaned_data['time']
    #     slug = form.cleaned_data['slug']
    #     messages.success(
    #         self.request,
    #         f'Your appointment has been changed'
    #     )
    #     return super(EditApptView, self).form_valid(form)


# def edit_form(request, slug):
#     post = get_object_or_404(Post, slug=slug)

#     if request.method == "POST":
#         form = EditApptForm(request.POST, instance=post)
#         if form.is_valid():

#             form.save()
#             print(form)
#             return redirect("PostList")
#         else:
#             print(form.errors)
    
#     form = EditApptForm(instance=post)
#     return render(request, "editform.html", {"form": form})


# Allow users to delete their appointments
class DeleteAppt(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = "/posts/"
