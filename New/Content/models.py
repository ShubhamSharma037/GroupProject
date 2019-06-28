from django.db import models

# Create your models here.

class HmDesignImg(models.Model):
    design_name = models.CharField(max_length = 30)
    design_type = models.CharField(max_length = 20)
    design_img_link = models.CharField(max_length = 2000)
