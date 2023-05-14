from django.db import models

# Create your models here.
from django.utils.text import slugify


# Create your models here.
class Blog(models.Model):
    blog_name = models.CharField(max_length=250)
    blog_image = models.ImageField(upload_to='project')
    slug = models.SlugField(max_length=255, unique=True)
    descriptions = models.CharField(max_length=500)
    
    live_link=models.CharField(max_length=255,null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.blog_name

    