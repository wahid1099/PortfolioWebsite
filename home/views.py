from django.shortcuts import render
from projects.models import *
from .models import *
from blogs.models import *

# Create your views here.


def home(request):

    project=Project.objects.all()
    blog=Blog.objects.all()
    social=SocailMedia.objects.all()
    resume=ResumeLink.objects.first()


    context={
        'project':project,
        'blog':blog,
        'social':social,
        'resume':resume
    }

    return render(request,'index.html',context)