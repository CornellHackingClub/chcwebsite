from django.shortcuts import render
from django.http import HttpResponse

from .models import Lectures
# Create your views here.
# Just using function based views for now because they're easy

def lectures_create(request):
    return HttpResponse("<h1>Hello</h1>")

def lectures_retrieve(request):
    return HttpResponse("<h1>retrieve</h1>")

def lectures_list(request):
    queryset = Lectures.objects.all()
    if request.user.is_authenticated():
        context = {
        "object_list": queryset,
        "title":"List"
    }
    else:
        context = {
        "title":"bruh"
    }

    return render(request, "lectures.html", context)

def lectures_update(request):
    return HttpResponse("<h1>update</h1>")

def lectures_delete(request):
    return HttpResponse("<h1>delete</h1>")