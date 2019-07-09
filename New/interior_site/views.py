from django.shortcuts import render
from django.http import HttpResponse
from Content.models import HmDesignImg, CstmrFeed, TeamMembers, ClientsNLinks, BlogPage
from Content.forms import ContactForm


# Create your views here.


def index(request):
    hm_design_img = HmDesignImg.objects.all()
    cst_feed = CstmrFeed.objects.all()
    tm_mem = TeamMembers.objects.all()
    cl_logo = ClientsNLinks.objects.all()
    blogs = BlogPage.objects.all()
    return render(request,'index.html', {"hm_design_img": hm_design_img, "cst_feed": cst_feed, "tm_mem": tm_mem, "cl_logo": cl_logo, "blogs": blogs})


def about(request):
    cst_feed = CstmrFeed.objects.all()
    return render(request, 'about.html', {"cst_feed": cst_feed})


def project(request):
    hm_design_img = HmDesignImg.objects.all()
    return render(request, 'project.html', {"hm_design_img": hm_design_img})


def services(request):
    return render(request, 'services.html')


def team(request):
    tm_mem = TeamMembers.objects.all()
    hm_design_img = HmDesignImg.objects.all()
    return render(request, 'team.html', {"hm_design_img": hm_design_img, "tm_mem": tm_mem})


def blog(request):
    blg_page = BlogPage.objects.all()
    return render(request, 'blog.html', {"blg_page": blg_page})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    return render(request,'contact.html', {"form": form})


# def blogS(request):
#     return render(request,'blog-single.html')


def selecet_blog(request, topic):
    blog = BlogPage.objects.filter(blg_topic=topic).values()
    side_blg = BlogPage.objects.exclude(blg_topic=topic)

    return render(request, 'blog-single.html', {"blog": blog, "side_blg": side_blg})


