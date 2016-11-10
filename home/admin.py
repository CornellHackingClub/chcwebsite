from django.contrib import admin

from .models import Home, Form

class HomeModelAdmin(admin.ModelAdmin):
    list_display = ["title", "start", "end"]
    list_filter = ["start"]
    search_fields = ["title"]
    class Meta:
        model = Home

class FormModelAdmin(admin.ModelAdmin):
    list_display = ["name", "netid", "year", "challenge","time"]
    list_filter = ["name"]
    search_fields = ["netid"]
    class Meta:
        model = Form


admin.site.register(Home, HomeModelAdmin)
admin.site.register(Form, FormModelAdmin)

