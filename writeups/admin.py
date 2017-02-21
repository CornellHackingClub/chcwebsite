from django.contrib import admin

# Register your models here.
from .models import CTF, Writeup

class CTFModelAdmin(admin.ModelAdmin):
    list_display = ["name_of_CTF", "date_competed", "place"]
    list_filter = ["place", "date_competed"]
    search_fields = ["name_of_CTF", "description"]
    class Meta:
        model = CTF


admin.site.register(CTF, CTFModelAdmin)

class WriteupModelAdmin(admin.ModelAdmin):
    list_display = ["name_of_challenge", "ctf", "category"]
    list_filter = ["ctf", "category"]
    search_fields = ["name_of_challenge", "ctf"]
    class Meta:
        model = CTF


admin.site.register(Writeup, WriteupModelAdmin)
