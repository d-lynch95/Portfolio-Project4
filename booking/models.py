from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Post(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    time = models.TimeField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    # need to add appointment Id and user information

# This class orders the appointments in reverse order
class Meta:
    ordering = ['-created_on']

def __str__(self):
    return self.title
