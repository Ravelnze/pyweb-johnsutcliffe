from __future__ import unicode_literals

from django.db import models


class Enquiry(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email_contact = models.EmailField(blank=False)
    phone_contact = models.CharField(max_length=10, blank=True)
    venue = models.CharField(max_length=30, blank=True)
    wedding_date = models.DateField(null=True, blank=True)
    comments = models.TextField(blank=True)
