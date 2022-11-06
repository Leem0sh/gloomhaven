# -*- encoding: utf-8 -*-
# ! python3

from __future__ import annotations

from django.db import models

from gloomhaven.events.types import EventTypes


class CityEvents(models.Model):
    id = models.IntegerField(primary_key=True)
    number: int = models.PositiveSmallIntegerField()
    text: str = models.TextField()
    optionA = models.ForeignKey("gloomhaven.OptionA", on_delete=models.CASCADE, null=True)
    optionB = models.ForeignKey("gloomhaven.OptionB", on_delete=models.CASCADE, null=True)
    image_url = models.URLField()
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.id


class RoadEvents(models.Model):
    id = models.IntegerField(primary_key=True)
    number: int = models.PositiveSmallIntegerField()
    text: str = models.TextField()
    optionA = models.ForeignKey("gloomhaven.OptionA", on_delete=models.CASCADE, null=True)
    optionB = models.ForeignKey("gloomhaven.OptionB", on_delete=models.CASCADE, null=True)
    image_url = models.URLField()
    verified = models.BooleanField(default=False)


class OptionA(models.Model):
    type = models.CharField(max_length=16, choices=EventTypes.choices, default=EventTypes.City)
    choice = models.TextField()
    outcome = models.TextField()
    image_url = models.URLField()


class OptionB(models.Model):
    type = models.CharField(max_length=16, choices=EventTypes.choices, default=EventTypes.City)
    choice = models.TextField()
    outcome = models.TextField()
    image_url = models.URLField()
