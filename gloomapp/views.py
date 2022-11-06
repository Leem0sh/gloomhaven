# -*- encoding: utf-8 -*-
# ! python3

from __future__ import annotations

from typing import Any

from django.shortcuts import render

from gloomapp.forms import CityEventForm


def index(request: Any) -> Any:
    form = CityEventForm()

    context = {
        'form': form,
    }

    return render(request, "gloomhaven/index.html", context=context)


def base(request: Any) -> Any:
    return render(request, "base.html")

def middleware_tester(request: Any) -> Any:
    return render(request, "gloomhaven/middleware-tester.html")
