from django.db import models

# Create your models here.

#Home Page Designs Images
class HmDesignImg(models.Model):
    design_name = models.CharField(max_length = 30)
    design_type = models.CharField(max_length = 20)
    design_img_link = models.CharField(max_length = 2000)

    class Meta:
        verbose_name = 'Home Design Image'
        verbose_name_plural = 'Home Design images'


#Customer Feedback
class CstmrFeed(models.Model):
    cst_name = models.CharField(max_length = 30)
    cst_feed_msg = models.CharField(max_length = 120)
    wrk_at_as = models.CharField(max_length = 40)
    cst_img = models.CharField(max_length=2000)

    class Meta:
        verbose_name = 'Customer Feedback'
        verbose_name_plural = 'Customer Feedback'


#Team Members
class TeamMembers(models.Model):
    mem_name = models.CharField(max_length = 30)
    mem_about = models.CharField(max_length = 120)
    mem_post = models.CharField(max_length = 40)
    mem_img = models.CharField(max_length=2000)
    mem_tweet = models.CharField(max_length=2000, blank=True, default='https://twitter.com/')
    mem_facebook = models.CharField(max_length=2000, blank=True, default='https://www.facebook.com/')
    mem_googlep = models.CharField(max_length=2000, blank=True, default='https://www.google.com/')
    mem_insta = models.CharField(max_length=2000, blank=True, default='https://www.instagram.com/')

    class Meta:
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'


#Team Members
class ClientsNLinks(models.Model):
    client_logo_link = models.CharField(max_length=2000, blank=False, default='https://ebaqdesign.com/wp-content/uploads/2018/04/your-logo-registered.png')
    client_link = models.CharField(max_length=2000, blank=False, default='https://goole.com/')

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

