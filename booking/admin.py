from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_filter = ('name','date','time')
    search_fields = ['name', 'date', 'time', 'phone', 'email',]
    list_display = ('name', 'date', 'time', 'phone', 'email',)


