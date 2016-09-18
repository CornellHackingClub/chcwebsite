from __future__ import unicode_literals

from django.db import models

# Create your models here.
class FAQ(models.Model):
    title = models.CharField(max_length=125)
    answer = models.CharField(max_length=512,default="Please wait for your question to be answered")
    user = models.CharField(max_length=125)

    def __unicode__(self):
        # This is the title of the lecture that will display in the admin page
        return self.title