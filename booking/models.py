from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Booking(models.Model):

    title = models.CharField(max_length=200)
    excerpt = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking')
    slug = models.SlugField(max_length=100, unique=True)
    published = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('bookingdata', args=[self.slug])

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title