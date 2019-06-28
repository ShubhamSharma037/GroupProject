from django.db import models

# Create your models here.

#Home Page Designs Images
class HmDesignImg(models.Model):
    design_name = models.CharField(max_length = 30)
    design_type = models.CharField(max_length = 20)
    design_img_link = models.CharField(max_length = 2000)


#Customer Feedback
class CstmrFeed(models.Model):
    cst_name = models.CharField(max_length = 30)
    cst_feed_msg = models.CharField(max_length = 120)
    wrk_at_as = models.CharField(max_length = 40)
    cst_img = models.CharField(max_length=2000)
