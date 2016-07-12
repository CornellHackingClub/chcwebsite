from django.contrib import admin

# Register your models here.
from .models import Writeups

class WriteupsModelAdmin(admin.ModelAdmin):
    list_display = ["name_of_CTF", "date_competed", "place"]
    list_filter = ["place", "date_competed"]
    search_fields = ["name_of_CTF", "description"]
    class Meta:
        model = Writeups


admin.site.register(Writeups, WriteupsModelAdmin)
