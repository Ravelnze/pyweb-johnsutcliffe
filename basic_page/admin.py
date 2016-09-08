from django.contrib import admin
from models import SiteContent


@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    list_display = ['page_name_display', 'title']

    def page_name_display(self, obj):
        if obj.page_name == '':
            return 'home'
        return obj.page_name
