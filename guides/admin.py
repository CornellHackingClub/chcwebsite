from django.contrib import admin

# Register your models here.
from .models import Guides

class LectureModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"]
    list_filter = ["timestamp"]
    search_fields = ["title", "description"]
    class Meta:
        model = Guides


admin.site.register(Guides, LectureModelAdmin)
