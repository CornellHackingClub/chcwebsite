import os

from django.shortcuts import render
import json

from CHCWebsite import settings
from .models import Home


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
    web_flag = request.GET.get("web_flag")
    crypto_flag = request.GET.get("crypto_flag")
    forensic_flag = request.GET.get("forensic_flag")
    reverse_flag = request.GET.get("reverse_flag")
    error = None
    error_text = "Sorry, not quite."

    if web_flag:
        print "got web flag" + web_flag
        # if web_flag is os.env['WEB_FLAG']:
        #     return render(request, "home.html") # redirect to form.
        # else: error = error_text

    if crypto_flag:
        print "got crypto flag" + crypto_flag

        # if crypto_flag is os.env['CRYPTO_FLAG']:
        #     return render(request, "home.html") # redirect to form.
        # else: error = error_text

    if forensic_flag:
        print "got forensic flag" + forensic_flag

        # if forensic_flag is os.env['FORENSIC_FLAG']:
        #     return render(request, "home.html") # redirect to form.
        # else: error = error_text

    if reverse_flag:
        print "got reverse flag" + reverse_flag
        error = error_text

        # if reverse_flag is os.env['REVERSE_FLAG']:
        #     return render(request, "home.html") # redirect to form.
        # else: error = error_text

    context = {
        "error": error,
    }
    return render(request, "challenge.html", context)

def form(request):
    return render(request, "completion_form.html")
