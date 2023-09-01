from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    # change prepoplated fields slug: to (appointment number) when it is set up
    prepopulated_fields = {'slug': ('id',)}
    summernote_fields = ('name')
    # The name field is only a placeholder and does not need summernote
    list_filter = ('name','date','time')
    search_fields = ['name', 'date', 'time', 'phone', 'email',]
    list_display = ('name', 'date', 'time', 'phone', 'email',)
