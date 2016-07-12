from django.shortcuts import render
from .models import Writeups

def writeups_home(request):
    queryset = Writeups.objects.all()
    if request.user.is_authenticated():
        context = {
        "object_list": queryset,
        "title":"List"
    }
    else:
        context = {
        "title":"bruh"
    }

    return render(request, "writeups-main.html", context)