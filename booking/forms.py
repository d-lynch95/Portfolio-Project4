from django import forms
from .models import Post

class ApptForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'phone', 'email', 'time', 'date', 'user', 'slug',)
