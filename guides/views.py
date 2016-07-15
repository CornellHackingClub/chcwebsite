from django.shortcuts import render
from .models import Guides

# Just using function based views for now because they're easy
def guides_home(request):
    queryset = Guides.objects.all()
    context = {
        "guides": queryset,
    }

    return render(request, "guides.html", context)