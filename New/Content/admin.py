from django.contrib import admin
from .models import HmDesignImg, CstmrFeed, ContactFormModel, BlogPage, PrjImg





class HmDesignImgAdmin(admin.ModelAdmin):
    list_display = ('design_name', 'design_type')


class PrjDesignImgAdmin(admin.ModelAdmin):
    list_display = ('design_name', 'design_type')


class CstmrFeedAdmin(admin.ModelAdmin):
    list_display = ['cst_name']



# class TeamMembersAdmin(admin.ModelAdmin):
#     list_display = ('mem_name', 'mem_post')


# class ClientsNLinksAdmin(admin.ModelAdmin):
#     list_display = ['client_link']


class BlogPageAdmin(admin.ModelAdmin):
    list_display = ('blg_name_blgger', 'blg_topic')



class ContactFormModelAdmin(admin.ModelAdmin):
    list_display = ('vw_name', 'vw_email', 'vw_subject')
    readonly_fields=['vw_name','vw_email','vw_subject','vw_msg']

# Register your models here.
admin.site.register(HmDesignImg, HmDesignImgAdmin)
admin.site.register(PrjImg, PrjDesignImgAdmin)
admin.site.register(CstmrFeed, CstmrFeedAdmin)
admin.site.register(BlogPage, BlogPageAdmin)
admin.site.register(ContactFormModel, ContactFormModelAdmin)

#admin title changes
admin.site.site_header = "DpdzineS"
admin.site.site_title = "DpdzineS Admin Panel"
admin.site.index_title = "Admin Panel"