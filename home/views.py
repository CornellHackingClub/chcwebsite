import os

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

    name = request.POST.get("name")
    netid = request.POST.get("netid")
    year = request.POST.get("year")

    if name or netid or year:
        return completed_challenge(request, name, netid, year)

    error = None
    error_text = "Sorry, not quite."

    if web_flag:
        if web_flag == os.getenv('WEB_FLAG', 0):
            response = render(request, "completion_form.html")
            response.set_cookie('web_flag', web_flag)
            return response
        else:
            error = error_text

    if crypto_flag:
        if crypto_flag == os.getenv('CRYPTO_FLAG', 0):
            response = render(request, "completion_form.html")
            response.set_cookie('crypto_flag', crypto_flag)
            return response
        else:
            error = error_text

    if forensic_flag:
        if forensic_flag == os.getenv('FORENSIC_FLAG', 0):
            response = render(request, "completion_form.html")
            response.set_cookie('forensic_flag', forensic_flag)
            return response
        else:
            error = error_text

    if reverse_flag:
        if reverse_flag == os.getenv('REVERSE_FLAG', 0):
            response = render(request, "completion_form.html")
            response.set_cookie('reverse_flag', reverse_flag)
            return response
        else:
            error = error_text

    context = {
        "error": error,
    }
    return render(request, "challenge.html", context)

def completed_challenge(request, name, netid, year):
    web = request.COOKIES.get('web_flag', None)
    crypto = request.COOKIES.get('crypto_flag', None)
    forensic = request.COOKIES.get('forensic_flag', None)
    reverse = request.COOKIES.get('reverse_flag', None)
    challenge = check_flag(web, crypto, forensic, reverse)

    error = None
    thanks = None
    if name and netid and year and challenge:
        query = Form(name=name, netid=netid, year=year, challenge=challenge)
        query.save()
        thanks = "Thank you and great job! You'll be hearing from us shortly"
    elif name or netid or year  or challenge:
        error = "Please fill out all fields."
    context = {
        "error": error,
        "thanks": thanks,
    }
    return render(request, "completion_form.html", context)


def check_flag(web_flag, crypto_flag, forensic_flag, reverse_flag):
    completed = ""
    if web_flag:
        if web_flag == os.getenv('WEB_FLAG', 0):
            completed += "web "

    if crypto_flag:
        if crypto_flag == os.getenv('CRYPTO_FLAG', 0):
            completed += "crypto "

    if forensic_flag:
        if forensic_flag == os.getenv('FORENSIC_FLAG', 0):
            completed += "forensics "

    if reverse_flag:
        if reverse_flag == os.getenv('REVERSE_FLAG', 0):
            completed += "reversing "

    if completed == "":
        completed = None

    return completed