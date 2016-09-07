from __future__ import unicode_literals

from django.db import models


class SiteContent(models.Model):
    page_name = models.CharField(max_length=30, blank=True)  # Leave empty for default page
    text_content = models.TextField(blank=True)
