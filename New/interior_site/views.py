from django.shortcuts import render,redirect
from django.http import HttpResponse
from Content.models import HmDesignImg, CstmrFeed, BlogPage, PrjImg
from Content.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
import os


# Create your views here.


def index(request):
    hm_design_img = HmDesignImg.objects.all()
    cst_feed = CstmrFeed.objects.all()
   # tm_mem = TeamMembers.objects.all()
    #cl_logo = ClientsNLinks.objects.all()
    blogs = BlogPage.objects.all()
    return render(request,'index.html', {"hm_design_img": hm_design_img, "cst_feed": cst_feed, "blogs": blogs})


def about(request):
    cst_feed = CstmrFeed.objects.all()
    return render(request, 'about.html', {"cst_feed": cst_feed})


def project(request):
    prj_img = PrjImg.objects.all()
    return render(request, 'project.html', {"prj_img": prj_img})


def services(request):
    return render(request, 'services.html')


def blog(request):
    blg_page = BlogPage.objects.all()
    return render(request, 'blog.html', {"blg_page": blg_page})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        #success=False
        if form.is_valid():
            form.save()
            subject = form.cleaned_data['vw_subject']
            from_email = form.cleaned_data['vw_email']
            message = form.cleaned_data['vw_msg']
           # success=True
            messages.success(request, "FORM SUBMISSION SUCCESSFUL", )
            messages.success(request, f" > From: {from_email}")
            messages.success(request, f" > To: kriti.goel1988@gmail.com")
            messages.success(request, f" > Subject: {subject}")
            messages.success(request, f" > Message: {message}")
            try:
                send_mail(subject, message, from_email, ['kriti.goel1988@gmail.com'])
                #print("passed")
            except BadHeaderError:
                #print("error")
                messages.error(request,'Form is not submitted.''Please try again.')
                return HttpResponse('Invalid header found.')
    form = ContactForm()
    return render(request, 'contact.html', {"form": form})




# def blogS(request):
#     return render(request,'blog-single.html')


def selecet_blog(request, topic):
    blog = BlogPage.objects.filter(blg_topic=topic).values()
    side_blg = BlogPage.objects.exclude(blg_topic=topic)

    return render(request, 'blog-single.html', {"blog": blog, "side_blg": side_blg})


