# -*- encoding: utf-8 -*-
# ! python3

from __future__ import annotations

import logging
from typing import Final, TypeVar, Type

from django.db import models, IntegrityError
from pydantic import parse_obj_as

from gloomhaven.events.city import CITY_EVENTS
from gloomhaven.events.road import ROAD_EVENTS
from django.core.management.base import BaseCommand

from gloomhaven.events.types import EventTypes
from gloomapp.models import CityEvents, RoadEvents, OptionA, OptionB
from gloomapp.schemas import CityEvent, RoadEvent

logger: Final = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options) -> None:
        logger.info("Starting to load the events")
        logger.info("Loading the city events")
        city_events = parse_obj_as(list[CityEvent], CITY_EVENTS)
        process_events(CityEvents, city_events, EventTypes.City)
        logger.info("City events loaded")
        logger.info("Starting to load the road events")
        road_events = parse_obj_as(list[RoadEvent], ROAD_EVENTS)
        process_events(RoadEvents, road_events, EventTypes.Road)
        logger.info("Road events loaded")


def process_events(
    event_handler: Type[CityEvents | RoadEvents],
    events: list[CityEvent | RoadEvent],
    event_type: EventTypes,
) -> None:
    for event in events:
        try:
            event_handler.objects.get_or_create(
                id=event.id,
                number=event.number,
                text=event.text,
                optionA=OptionA.objects.get_or_create(
                    type=event_type,
                    choice=event.optionA.choice,
                    outcome=event.optionA.outcome,
                    image_url=event.optionA.imageUrl,
                )[0],
                optionB=OptionB.objects.get_or_create(
                    type=event_type,
                    choice=event.optionB.choice,
                    outcome=event.optionB.outcome,
                    image_url=event.optionB.imageUrl,
                )[0],
                image_url=event.imageUrl,
            )
        except IntegrityError:
            logger.error(f"Could not create event {event.id}")
