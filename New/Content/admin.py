from django.contrib import admin
from .models import HmDesignImg, CstmrFeed, TeamMembers

# Register your models here.


class HmDesignImgAdmin(admin.ModelAdmin):
    list_display = ('design_name', 'design_type')


class CstmrFeedAdmin(admin.ModelAdmin):
    list_display = ('cst_name', 'wrk_at_as')


class TeamMembersAdmin(admin.ModelAdmin):
    list_display = ('mem_name', 'mem_post')


admin.site.register(HmDesignImg, HmDesignImgAdmin)
admin.site.register(CstmrFeed, CstmrFeedAdmin)
admin.site.register(TeamMembers, TeamMembersAdmin)
