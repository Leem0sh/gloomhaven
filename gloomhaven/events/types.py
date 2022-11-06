# -*- encoding: utf-8 -*-
# ! python3

from __future__ import annotations
from django.db import models

from typing import Any


class EventTypes(models.TextChoices):
    Road = "Road"
    City = "City"
