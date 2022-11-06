# -*- encoding: utf-8 -*-
# ! python3

from __future__ import annotations

from typing import Any

from django.shortcuts import render


def index(request: Any) -> Any:
    return render(request, "index.html")


def base(request: Any) -> Any:
    return render(request, "base.html")
