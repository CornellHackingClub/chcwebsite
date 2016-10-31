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
