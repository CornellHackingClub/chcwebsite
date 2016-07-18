from django.shortcuts import render
from .models import Lectures
from django.db.models import Q

# Just using function based views for now because they're easy
def lectures_home(request):
    queryset = Lectures.objects.all()
    search = request.GET.get("query")
    if search:
        queryset = queryset.filter(
            Q(title__icontains=search) | Q(description__icontains=search))
    context = {
        "lectures": queryset,
    }
    return render(request, "lectures.html", context)