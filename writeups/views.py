from django.shortcuts import render, get_object_or_404
from .models import CTF


def ctfs_home(request):
    queryset = CTF.objects.all().order_by('-timestamp')
    context = {
        "ctfs": queryset,
    }
    return render(request, "ctfs-main.html", context)


def ctf_detail(request, id):
    ctf = get_object_or_404(CTF, id=id)
    queryset = ctf.writeup_set.all()

    context = {
        "writeups": queryset,
        "ctf": ctf
    }
    return render(request, "ctf.html", context)
