from django.shortcuts import render,redirect
from django.http import HttpResponse
from Content.models import HmDesignImg, CstmrFeed, BlogPage, PrjImg
from Content.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages



# Create your views here.


def index(request):

        hm_design_img = HmDesignImg.objects.all()
        cst_feed = CstmrFeed.objects.all()
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
        if form.is_valid():
            form.save()
            subject = form.cleaned_data['vw_subject']
            from_email = form.cleaned_data['vw_email']
            message = form.cleaned_data['vw_msg']
            name = form.cleaned_data['vw_name']
           # success=True
            messages.success(request, "Thanks for contacting us.")
            messages.success(request, "We will respond you soon.")
            messages.success(request, "Entered details are: " )
            messages.success(request, f"  From: {name}")
            messages.success(request, f"  Subject: {subject}")
            messages.success(request, f"  Message: {message}")
            try:
                send_mail(subject, message, from_email, ['kriti.goel1988@gmail.com'])

            except BadHeaderError:

                messages.error(request,'Form is not submitted.''Please try again.')
                return HttpResponse('Invalid header found.')
    form = ContactForm()
    return render(request, 'contact.html', {"form": form})




def selecet_blog(request, topic):
    blog = BlogPage.objects.filter(blg_topic=topic)
    side_blg = BlogPage.objects.exclude(blg_topic=topic)

    return render(request, 'blog-single.html', {"blog": blog, "side_blg": side_blg})


def admin(request):
    if request.user.is_authenticated():
        return redirect(request,'admin_page')
