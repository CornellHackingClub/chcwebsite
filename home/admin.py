from django.contrib import admin

from .models import Home

class HomeModelAdmin(admin.ModelAdmin):
    list_display = ["title", "start", "end"]
    list_filter = ["start"]
    search_fields = ["title"]
    class Meta:
        model = Home


admin.site.register(Home, HomeModelAdmin)
