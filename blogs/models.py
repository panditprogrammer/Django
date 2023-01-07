from django.db import models


# Create your models here.
class Blogs(models.Model):
    slug = models.SlugField(null=True,blank=True)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    img = models.ImageField(upload_to="blogs/images")
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)