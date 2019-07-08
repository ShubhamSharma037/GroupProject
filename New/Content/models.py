from django.db import models
import datetime
# Create your models here.

#Home Page Designs Images
class HmDesignImg(models.Model):
    design_name = models.CharField(max_length = 30, verbose_name="Design Name")
    design_type = models.CharField(max_length = 20, verbose_name="Design Type(Interior/Exterior)")
    design_img_link = models.CharField(max_length = 2000, verbose_name="Image Link")

    class Meta:
        verbose_name = 'Home Design Image'
        verbose_name_plural = 'Home Design images'


#Customer Feedback
class CstmrFeed(models.Model):
    cst_name = models.CharField(max_length = 30, verbose_name="Customer Name")
    cst_feed_msg = models.TextField(max_length = 1000, verbose_name="Feedback Message")
    #wrk_at_as = models.CharField(max_length = 40, verbose_name="Work At/As")
    #cst_img = models.CharField(max_length=2000, verbose_name="Customer Image")

    class Meta:
        verbose_name = 'Customer Feedback'
        verbose_name_plural = 'Customer Feedback'


#Team Members
class TeamMembers(models.Model):
    mem_name = models.CharField(max_length = 30, verbose_name="Member Name")
    mem_about = models.CharField(max_length = 120, verbose_name="About Member")
    mem_post = models.CharField(max_length = 40, verbose_name="Member Post/Rank")
    mem_img = models.CharField(max_length=2000, verbose_name="Member Image")
    mem_tweet = models.CharField(max_length=2000, blank=True, default='https://twitter.com/', verbose_name="Twitter Link")
    mem_facebook = models.CharField(max_length=2000, blank=True, default='https://www.facebook.com/', verbose_name="Facebook Link")
    mem_googlep = models.CharField(max_length=2000, blank=True, default='https://www.google.com/', verbose_name="Google+ Link")
    mem_insta = models.CharField(max_length=2000, blank=True, default='https://www.instagram.com/', verbose_name="Instagram Link")

    class Meta:
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'


#Team Members
class ClientsNLinks(models.Model):
    client_logo_link = models.CharField(max_length=2000, blank=False, default='https://ebaqdesign.com/wp-content/uploads/2018/04/your-logo-registered.png', verbose_name="Client Logo")
    client_link = models.CharField(max_length=2000, blank=False, default='https://goole.com/', verbose_name="Client Link")

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


#Blogs
class BlogPage(models.Model):
    blg_topic=models.CharField(max_length=50,null=False, verbose_name="Blog Name")
    blg_desc=models.TextField(max_length=10000,null=False, verbose_name="Blog Content")
    blg_pic=models.CharField(max_length=2000, verbose_name="Blog Image")
    blg_date=models.DateField( default=datetime.date.today, verbose_name="Blog Date")
    blg_name_blgger=models.CharField(max_length=20,null=False, verbose_name="Blogger Name")


    class Meta:
        verbose_name='BlogUpdate'
        verbose_name_plural='BlogUpdates'


#Contact Form
class ContactFormModel(models.Model):
    vw_name = models.CharField(max_length=30, verbose_name="Viewer Name")
    vw_email = models.EmailField(max_length=50, verbose_name="Viewer E-Mail")
    vw_subject = models.CharField(max_length=50, verbose_name="Viewer Subject")
    vw_msg = models.TextField(max_length=5000, verbose_name="Viewer Message")

    class Meta:
        verbose_name = 'Viewer Contact Detail'
        verbose_name_plural = 'Viewer Contact Details'


