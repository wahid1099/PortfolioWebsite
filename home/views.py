from django.shortcuts import render,redirect
from projects.models import *
from .models import *
from blogs.models import *
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.


def home(request):
   


    project=Project.objects.all()
    blog=Blog.objects.all()
    # social=SocailMedia.objects.all()
    facebook_link = SocailMedia.objects.get(name='facebook')
    linkedin_link = SocailMedia.objects.get(name='linkedin')
    youtube_link = SocailMedia.objects.get(name='youtube')
    github_link = SocailMedia.objects.get(name='github')
    twitter_link = SocailMedia.objects.get(name='twitter')

    resume=ResumeLink.objects.first()


    context={
        'project':project,
        'blog':blog,
        'facebook_link':facebook_link,
        'linkedin_link':linkedin_link,
        'youtube_link':youtube_link,
        'github_link':github_link,
        'twitter_link':twitter_link,

        'resume':resume
    }
    if request.method=="POST":
        message=request.POST["message"]
        # print("message",message)
        name=request.POST["name"]
        email = request.POST["email"]
        try:
            send_mail(
                'Contact Form',
                f'From :{email}\n and\n Name : {name}\n{message}',
                'mw0641295@gmail.com',
                ['wahid55100@gmail.com'],
                fail_silently=False,
            ) 

            messages.success(request,"Message send successfully!!....")
        except:
            messages.error(request, "Email send Failed")
        return render(request,'index.html',context)
    else:

     return render(request,'index.html',context)


