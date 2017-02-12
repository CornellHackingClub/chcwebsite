from __future__ import unicode_literals

import django.utils
from django.db import models

# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=125)
    start = models.DateTimeField(blank=False)
    end = models.DateTimeField(blank=False)
    location = models.CharField(max_length=125)
    allday = models.BooleanField()

    def __unicode__(self):
        return self.title

class Form(models.Model):
    name = models.CharField(max_length=125)
    netid = models.CharField(max_length=125)
    year = models.CharField(max_length=125)
    challenge = models.CharField(max_length=125)
    time = models.DateTimeField(default=django.utils.timezone.now, blank=True)


    def __unicode__(self):
        return self.name