from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Guides(models.Model):
    title = models.CharField(max_length=125)
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    document = models.FileField(null=False, blank=False)

    def __unicode__(self):
        # This is the title of the lecture that will display in the admin page
        return self.title