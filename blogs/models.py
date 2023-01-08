from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Blogs(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    description = HTMLField()
    img = models.ImageField(upload_to="blogs/images")
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)