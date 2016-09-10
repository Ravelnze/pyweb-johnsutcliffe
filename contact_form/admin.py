from django.contrib import admin
from models import Enquiry


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email_contact', 'wedding_date', 'venue']
