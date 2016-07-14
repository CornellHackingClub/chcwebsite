from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Home(models.Model):
    title = models.CharField(max_length=125)
    start = models.DateTimeField(blank=False)
    end = models.DateTimeField(blank=False)
    allday = models.BooleanField()

    def __unicode__(self):
        # This is the title of the lecture that will display in the admin page
        return self.title