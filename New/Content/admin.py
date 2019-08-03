from django.contrib import admin
from .models import HmDesignImg, CstmrFeed, ContactFormModel, BlogPage, PrjImg







class HmDesignImgAdmin(admin.ModelAdmin):
    list_display = ('design_name', 'design_type')
    list_editable = ['design_type']
    search_fields = ['design_name']
    list_filter = ['design_type']
    list_per_page = 10


class PrjDesignImgAdmin(admin.ModelAdmin):
    list_display = ('design_name', 'design_type','design_img_link')
    list_editable = ['design_type']
    search_fields = ['design_name','design_type']
    list_filter = ['design_type']
    list_per_page = 10




class CstmrFeedAdmin(admin.ModelAdmin):
    list_display = ['cst_name']




class BlogPageAdmin(admin.ModelAdmin):
    list_display = ('blg_name_blgger', 'blg_topic', 'blg_date')
    list_editable=['blg_topic']
    search_fields = ['blg_topic', 'blg_name_blgger']
    list_filter = ['blg_name_blgger', 'blg_date']
    list_per_page = 5



class ContactFormModelAdmin(admin.ModelAdmin):
    list_display = ('vw_name', 'vw_email', 'vw_subject')
    readonly_fields=['vw_name','vw_email','vw_subject','vw_msg']
    list_filter = ['vw_name', 'vw_subject']
    search_fields = ['vw_name']
    list_per_page = 5

# Register your models here.
admin.site.register(HmDesignImg, HmDesignImgAdmin)
admin.site.register(PrjImg, PrjDesignImgAdmin)
admin.site.register(CstmrFeed, CstmrFeedAdmin)
admin.site.register(BlogPage, BlogPageAdmin)
admin.site.register(ContactFormModel, ContactFormModelAdmin)

#admin title changes
admin.site.site_header = "Welcome to DpdzineS"
admin.site.site_title = "DpdzineS Admin Panel"
admin.site.index_title = "Admin Panel"