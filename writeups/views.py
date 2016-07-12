from django.shortcuts import render, get_object_or_404
from .models import Writeups

def writeups_home(request, name):
    instance = get_object_or_404(Writeups, name=name)
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