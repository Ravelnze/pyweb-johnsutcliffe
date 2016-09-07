from __future__ import unicode_literals

from django.db import models


class SiteContent(models.Model):
    page_name = models.CharField(max_length=30, blank=True)  # Leave empty for default page
    title = models.CharField(max_length=30, blank=False)  # What is the object?
    text_content = models.TextField(blank=True)  # Can be used for entire HTML blocks
