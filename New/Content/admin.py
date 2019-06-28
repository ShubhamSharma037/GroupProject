from django.contrib import admin
from .models import HmDesignImg

# Register your models here.


class HmDesignImgAdmin(admin.ModelAdmin):
    list_display = ('design_name', 'design_type')


admin.site.register(HmDesignImg, HmDesignImgAdmin)