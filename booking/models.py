from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Post(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    time = models.TimeField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    # need to add appointment Id and user information

    def save(self, *args, **kwargs):
            if not self.slug:
                self.slug = slugify(self.name)
            super().save(*args, **kwargs)

# This class orders the appointments in reverse order
class Meta:
    ordering = ['-created_on']

def __str__(self):
    return self.title
