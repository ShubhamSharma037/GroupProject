from django.contrib import admin
from .models import HmDesignImg, CstmrFeed, TeamMembers, ClientsNLinks, ContactFormModel

# Register your models here.


class HmDesignImgAdmin(admin.ModelAdmin):
    list_display = ('design_name', 'design_type')


class CstmrFeedAdmin(admin.ModelAdmin):
    list_display = ('cst_name', 'wrk_at_as')


class TeamMembersAdmin(admin.ModelAdmin):
    list_display = ('mem_name', 'mem_post')


class ClientsNLinksAdmin(admin.ModelAdmin):
    list_display = ['client_link']


class ContactFormModelAdmin(admin.ModelAdmin):
    list_display = ('vw_name', 'vw_email', 'vw_subject')


admin.site.register(HmDesignImg, HmDesignImgAdmin)
admin.site.register(CstmrFeed, CstmrFeedAdmin)
admin.site.register(TeamMembers, TeamMembersAdmin)
admin.site.register(ClientsNLinks, ClientsNLinksAdmin)
admin.site.register(ContactFormModel, ContactFormModelAdmin)
