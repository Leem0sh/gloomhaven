# -*- encoding: utf-8 -*-
# ! python3

from __future__ import annotations

import logging
from typing import Final

from pydantic import parse_obj_as

from gloomhaven.events.city import CITY_EVENTS
from gloomhaven.events.road import ROAD_EVENTS
from django.core.management.base import BaseCommand

from gloomhaven.models import CityEvents, RoadEvents
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
        for city_event in CITY_EVENTS:
            print(city_event)
            city_event = parse_obj_as(CityEvent, city_event)
            CityEvents.objects.get_or_create(
                id=city_event.id,
                number=city_event.number,
                text=city_event.text,
                optionA=city_event.optionA.json(),
                optionB=city_event.optionB.json(),
                image_url=city_event.imageUrl,
            )
        for road_event in ROAD_EVENTS:
            road_event = parse_obj_as(RoadEvent, road_event)
            RoadEvents.objects.get_or_create(
                id=road_event.id,
                number=road_event.number,
                text=road_event.text,
                optionA=road_event.optionA.json(),
                optionB=road_event.optionB.json(),
                image_url=road_event.imageUrl,
            )
