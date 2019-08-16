from django.db import models
import datetime
# Create your models here.

#Home Page Designs Images
class HmDesignImg(models.Model):
    design_name = models.CharField(max_length = 30, verbose_name="Design Name")
    design_type = models.CharField(max_length = 10, verbose_name="Design Type", choices=(
                                                                 ('interior', 'Interior'),
                                                                 ('exterior', 'Exterior')))
    design_img_link = models.ImageField(max_length=2000,verbose_name="Image Link", blank=False)

    class Meta:
        verbose_name = 'Home Page Designs Image'
        verbose_name_plural = 'Home Page Design images'

#Project Page Design Images
class PrjImg(models.Model):
    design_name = models.CharField(max_length=30, verbose_name="Design Name")
    design_type = models.CharField(max_length=30, verbose_name="Design Type", choices=(
                                                                 ('Bed Room','Bed Room'),
                                                                 ('Drawing Room','Drawing Room'),
                                                                 ('Kids Room','Kids Room'),
                                                                 ('Ceiling', 'Ceiling'),
                                                                 ('Wardrobe','Wardrobe'),
                                                                 ('Kitchen','Kitchen'),
                                                                 ('Living Room','Living Room'),
                                                                 ('Dining Room','Dining Room'),
                                                                 ))
    design_img_link = models.ImageField(verbose_name="Image Link", blank=False)



    class Meta:
        verbose_name = 'Project Page Designs Image'
        verbose_name_plural = 'Project Page Design Images'


#Customer Feedback
class CstmrFeed(models.Model):
    cst_name = models.CharField(max_length = 30, verbose_name="Customer's Name")
    cst_feed = models.TextField(max_length = 1000, verbose_name="Feedback Message")


    class Meta:
        verbose_name = 'Customers Feedback'
        verbose_name_plural = 'Customers Feedback'



#Blogs
class BlogPage(models.Model):
    blg_topic=models.CharField(max_length=50,null=False, verbose_name="Blog Name")
    blg_desc=models.TextField(max_length=10000,null=False, verbose_name="Blog Content")
    blg_pic=models.ImageField( verbose_name="Blog Image", blank=False)
    blg_date=models.DateField( default=datetime.date.today, verbose_name="Blog Date")
    blg_name_blgger=models.CharField(max_length=20,null=False, verbose_name="Blogger Name")



    class Meta:
        verbose_name='Blog'
        verbose_name_plural='Blogs'


#Contact Form
class ContactFormModel(models.Model):
    vw_name = models.CharField(max_length=30, verbose_name="Visitor's Name")
    vw_email = models.EmailField(max_length=50, verbose_name="Visitor's E-Mail")
    vw_subject = models.CharField(max_length=50, verbose_name="Visitor's Subject")
    vw_msg = models.TextField(max_length=5000, verbose_name="Visitor's Message")

    class Meta:
        verbose_name = 'Visitor  Details'
        verbose_name_plural = 'Visitors Details'



