from django.shortcuts import render
from django.http import HttpResponse
from Content.models import HmDesignImg

# Create your views here.
def index(request):
    hm_design_img = HmDesignImg.objects.all()
    return render(request,'index.html', {"hm_design_img" : hm_design_img})

def  about(request):
    return render(request,'about.html')

def project(request):
   return render(request,'project.html')

def services(request):
    return render(request,'services.html')

def team(request):
    return render(request,'team.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def blogS(request):
    return render(request,'blog-single.html')

def contact2(request):
    return render(request,'contact2.html')