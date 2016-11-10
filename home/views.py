import os

from django.http import HttpResponse
from django.shortcuts import render
import json

from CHCWebsite import settings
from .models import Home, Form


# Just using function based views for now because they're easy
def calendar(request):
    queryset = Home.objects.all().order_by('start').reverse()
    context = {
        "events": queryset,
    }
    return render(request, "index.html", context)


def build_events_json():
    header = {"left": "prev,next today",
              "center": "title",
              "right": "month,agendaWeek,agendaDay"}
    events = []
    queryset = Home.objects.all()
    for data in queryset:
        event = {
            "title": data.title,
            "start": data.start.strftime(settings.DATE_INPUT_FORMATS),
            "end": data.end.strftime(settings.DATE_INPUT_FORMATS),
            "allDay": data.allday
        }
        events.append(event)
    result = {"header": header,
              "events": events}
    return json.dumps(result)


def challenges(request):
    web_flag = request.POST.get("web_flag")
    crypto_flag = request.POST.get("crypto_flag")
    forensic_flag = request.POST.get("forensic_flag")
    reverse_flag = request.POST.get("reverse_flag")
    error = None
    error_text = "Sorry, not quite."

    if web_flag:
        print "got web flag" + web_flag
        if web_flag == os.getenv('WEB_FLAG', 0):
              return form(request, 'web')
        else: error = error_text

    if crypto_flag:
        print "got crypto flag" + crypto_flag
        if crypto_flag == os.getenv('CRYPTO_FLAG', 0):
             return form(request, 'crypto')
        else: error = error_text

    if forensic_flag:
        print "got forensic flag" + forensic_flag
        if forensic_flag == os.getenv('FORENSIC_FLAG',0) or True:
            return form(request, 'forensics')
        else: error = error_text

    if reverse_flag:
        print "got reverse flag" + reverse_flag
        if reverse_flag == os.getenv('REVERSE_FLAG', 0):
             return form(request, 'reversing')
        else: error = error_text

    context = {
        "error": error,
    }
    return render(request, "challenge.html", context)


def form(request, challenge):
    name = request.GET.get("name")
    netid = request.GET.get("netid")
    year = request.GET.get("year")
    error = None
    if name and netid and year:
        query = Form(name = name , netid = netid, year = year, challenge = challenge)
        query.save()
    elif name or netid or year:
        error ="Please fill out all fields."
    context = {
        "error": error,
    }
    return render(request, "completion_form.html", context) #redirect to thank you message and remove cookie
