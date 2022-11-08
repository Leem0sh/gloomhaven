# -*- encoding: utf-8 -*-
# ! python3

from __future__ import annotations

from typing import Any

from django.shortcuts import render
from django.views.generic import ListView

from gloomapp.forms import CityEventForm
from gloomapp.models import RoadEvents, CityEvents


def index(request: Any) -> Any:
    form = CityEventForm()

    context = {
        "form": form,
    }

    return render(request, "index.html", context=context)


def get_event(request):
    text = request.POST.get("event-text")  # get data from form where name="contactname"
    event_type = request.POST.get("event-type")
    handler = CityEvents if event_type == "city" else RoadEvents


    events = handler.objects.all().filter(text__icontains=text)


    return render(
        request, "event-list.html", {"events": [*events]}
    )

class CityEventsList(ListView):
    template_name = "city-events.html"  # html file to display the list of contacts
    model = CityEvents
    context_object_name = (
        "cityevents"  # used in the HTML template to loop through and list contacts
    )


class RoadEventsList(ListView):
    template_name = "road-events.html"  # html file to display the list of contacts
    model = RoadEvents
    context_object_name = (
        "roadevents"  # used in the HTML template to loop through and list contacts
    )
