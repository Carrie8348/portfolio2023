from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class UX_Projects(models.Model):
    title = models.CharField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=300)
    created_time = models.CharField(max_length=300)
    tool = models.CharField(max_length=300)
    introduction = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.title
