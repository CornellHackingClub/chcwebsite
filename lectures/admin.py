from django.contrib import admin

# Register your models here.
from .models import Lectures

class LectureModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"]
    list_filter = ["timestamp"]
    search_fields = ["title", "description"]
    class Meta:
        model = Lectures


admin.site.register(Lectures, LectureModelAdmin)
