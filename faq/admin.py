from django.contrib import admin

# Register your models here.
from .models import FAQ

class FAQModelAdmin(admin.ModelAdmin):
    list_display = ["title"]
    list_filter = ["title"]
    search_fields = ["title", "user"]
    class Meta:
        model = FAQ


admin.site.register(FAQ, FAQModelAdmin)
