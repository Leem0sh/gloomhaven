# -*- encoding: utf-8 -*-
# ! python3

from __future__ import annotations


from django.forms import ModelForm
from django import forms
from gloomapp.models import CityEvents, RoadEvents, Contact


class CityEventForm(forms.Form):
    class Meta:
        model = CityEvents
        exclude = (
            "created",
            "updated",
            "author",
        )
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 450px; align: center;",
                    "placeholder": "Title",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 900px;",
                    "placeholder": "Content",
                }
            ),
        }


class RoadEventForm(forms.Form):
    class Meta:
        model = RoadEvents
        exclude = (
            "created",
            "updated",
            "author",
        )
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 450px; align: center;",
                    "placeholder": "Title",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 900px;",
                    "placeholder": "Content",
                }
            ),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        fields = ["name", "phone_number"]
        model = Contact
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
        }
