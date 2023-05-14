from django.db import models
from django.utils.text import slugify


# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=250)
    project_image = models.ImageField(upload_to='project')
    slug = models.SlugField(max_length=255, unique=True)
    description = models.CharField(max_length=500)
    gihubLink = models.CharField(max_length=255,null=True, blank=True)
    live_link=models.CharField(max_length=255,null=True, blank=True)
    serversite = models.CharField(max_length=255,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.project_name

    