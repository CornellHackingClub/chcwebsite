from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Writeups(models.Model):
    name_of_CTF = models.CharField(max_length=125)
    url_of_CTF = models.URLField()
    date_competed = models.CharField(max_length=125)
    place = models.IntegerField()
    out_of = models.IntegerField()
    description = models.TextField()
    writeup = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        # This is the title of the lecture that will display in the admin page
        return self.name_of_CTF