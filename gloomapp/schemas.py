# -*- encoding: utf-8 -*-
# ! python3

from __future__ import annotations

from pydantic import BaseModel, HttpUrl


class optionAModel(BaseModel):
    choice: str
    outcome: str
    imageUrl: str

class optionBModel(BaseModel):
    choice: str
    outcome: str
    imageUrl: str

class CityEvent(BaseModel):
    id: int
    number: int
    text: str
    optionA: optionAModel
    optionB: optionBModel
    imageUrl: str
    verified: bool

class RoadEvent(BaseModel):
    id: int
    number: int
    text: str
    optionA: optionAModel
    optionB: optionBModel
    imageUrl: str
    verified: bool





