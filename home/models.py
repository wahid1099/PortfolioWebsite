from django.db import models

# Create your models here.


class SocailMedia(models.Model):
    name = models.CharField(max_length=255)
    link=models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ResumeLink(models.Model):
     
    link=models.CharField(max_length=255)
    def __str__(self):
        return self.link

    