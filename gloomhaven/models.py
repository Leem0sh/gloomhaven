# -*- encoding: utf-8 -*-
# ! python3

from __future__ import annotations

from django.db import models


class CityEvents(models.Model):
    id = models.IntegerField(primary_key=True)
    number: int = models.PositiveSmallIntegerField()
    text: str = models.TextField()
    optionA = models.JSONField()
    optionB = models.JSONField()
    image_url = models.URLField()
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.id


class RoadEvents(models.Model):
    id = models.IntegerField(primary_key=True)
    number: int = models.PositiveSmallIntegerField()
    text: str = models.TextField()
    optionA = models.JSONField()
    optionB = models.JSONField()
    image_url = models.URLField()
    verified = models.BooleanField(default=False)
