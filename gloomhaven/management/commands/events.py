# -*- encoding: utf-8 -*-
# ! python3

from __future__ import annotations

import logging
from typing import Final

from pydantic import parse_obj_as

from gloomhaven.events.city import CITY_EVENTS
from gloomhaven.events.road import ROAD_EVENTS
from django.core.management.base import BaseCommand

from gloomhaven.events.types import EventTypes
from gloomhaven.models import CityEvents, RoadEvents, OptionA, OptionB
from gloomhaven.schemas import CityEvent, RoadEvent

logger: Final = logging.getLogger(__name__)


class Command(BaseCommand):
    help = """
    Sends the data from the NDJson table to the GW dimensions.
    """

    # def add_arguments(self, parser) -> None:
    #     """
    #     :param parser:
    #     :return:
    #     """
    #     parser.add_argument(
    #         "--model-name",
    #         type=str,
    #         help="The model name we want to update. [FURNITURE/TEXTILE]",
    #     )
    def handle(self, *args, **options) -> None:
        logger.info("Starting to load the events")
        logger.info("Loading the city events")
        city_events = parse_obj_as(list[CityEvent], CITY_EVENTS)
        for city_event in city_events:
            CityEvents.objects.get_or_create(
                id=city_event.id,
                number=city_event.number,
                text=city_event.text,
                optionA=OptionA.objects.get_or_create(
                    type=EventTypes.City,
                    choice=city_event.optionA.choice,
                    outcome=city_event.optionA.outcome,
                    image_url=city_event.optionA.imageUrl,
                )[0],
                optionB=OptionB.objects.get_or_create(
                    type=EventTypes.City,
                    choice=city_event.optionB.choice,
                    outcome=city_event.optionB.outcome,
                    image_url=city_event.optionB.imageUrl,
                )[0],
                image_url=city_event.imageUrl,
            )

        logger.info("City events loaded")
        logger.info("Starting to load the road events")
        road_events = parse_obj_as(list[RoadEvent], ROAD_EVENTS)
        for road_event in road_events:
            RoadEvents.objects.get_or_create(
                id=road_event.id,
                number=road_event.number,
                text=road_event.text,
                optionA=OptionA.objects.get_or_create(
                    type=EventTypes.Road,
                    choice=road_event.optionA.choice,
                    outcome=road_event.optionA.outcome,
                    image_url=road_event.optionA.imageUrl,
                )[0],
                optionB=OptionB.objects.get_or_create(
                    type=EventTypes.Road,
                    choice=road_event.optionB.choice,
                    outcome=road_event.optionB.outcome,
                    image_url=road_event.optionB.imageUrl,
                )[0],
                image_url=road_event.imageUrl,
            )
        logger.info("Road events loaded")