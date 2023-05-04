from django import forms
from django.contrib.gis.db import models
from django.contrib.postgres.fields import ArrayField

import s100.models


class OrganisationContactArea(s100.models.FeatureType):
    class Meta:
        abstract = True


class SupervisedArea(OrganisationContactArea):
    class Meta:
        abstract = True


class ReportableServiceArea(SupervisedArea):
    class Meta:
        abstract = True


# FIXME: Est-ce qu'on a besoin de tout ? Est-ce qu'on peut faire ça dans l'admin ? Est-ce qu'on bouge ça dans un fields.py ?
class ChoiceArrayField(ArrayField):
    def formfield(self, **kwargs):
        defaults = {
            "form_class": forms.MultipleChoiceField,
            "choices": self.base_field.choices,
            "widget": forms.CheckboxSelectMultiple(
                # FIXME : Les classes s'appliquent sur les labels des checkbox en plus du parent
                attrs={"class": "choice-array-field"},
            ),
        }
        defaults.update(kwargs)

        return super(ArrayField, self).formfield(**defaults)


# To force english labels
BOOLEAN_CHOICES = (
    (True, "Yes"),
    (False, "No"),
)


class CategoryOfVessel(s100.models.CodeList):
    # fmt: off
    GENERAL_CARGO_VESSEL = "general cargo vessel" # general cargo vessel (a vessel designed to carry general cargo)
    CONTAINER_CARRIER = "container carrier" # container carrier (a vessel designed to carry ISO containers)
    TANKER = "tanker" # tanker (a vessel designed to carry bulk liquid or gas, including LPG and LNG)
    BULK_CARRIER = "bulk carrier" # bulk carrier (a vessel designed to carry bulk solid material)
    PASSENGER_VESSEL = "passenger vessel" # passenger vessel (a vessel designed to carry passengers; often a cruise ship)
    ROLL_ON_ROLL_OFF = "roll-on roll-off" # roll-on roll-off (a vessel designed to allow road vehicles to be driven on and off; often a ferry)
    REFRIGERATED_CARGO_VESSEL = "refrigerated cargo vessel" # refrigerated cargo vessel (a vessel designed to carry refrigerated cargo)
    FISHING_VESSEL = "fishing vessel" # fishing vessel (a vessel designed to catch or hunt fish)
    SERVICE = "service" # service (a vessel which provides a service such as a tug, anchor handler, survey or supply vessel)
    WARSHIP = "warship" # warship (a vessel designed for the conduct of military operations)
    TOWED_OR_PUSHED_COMPOSITE_UNIT = "towed or pushed composite unit" # towed or pushed composite unit (either a tug and tow, or any combination of a tug providing propulsion to barges or vessels secured ahead or alongside)
    TUG_AND_TOW = "tug and tow" # tug and tow (a combination of tug(s) and non-powered tow(s))
    LIGHT_RECREATIONAL = "light recreational" # light recreational (A pleasure boat or watercraft, or an excursion vessel used for short cruises such as whale watching)
    SEMI_SUBMERSIBLE_OFFSHORE_INSTALLATION = "semi-submersible offshore installation" # semi-submersible offshore installation (An installation which is designed to float at all times and which is normally anchored in position when deployed in the offshore gas and oil industry.)
    JACKUP_EXPLORATION_OR_PROJECT_INSTALLATION = "jackup exploration or project installation" # jackup exploration or project installation (An exploration or project installation with legs which can be raised and lowered. The legs are raised when the installation is repositioned. When stationary the legs are lowered to the sea floor and the working platform is raised clear of the sea surface)
    LIVESTOCK_CARRIER = "livestock carrier" # livestock carrier (A vessel designed to carry large quantities of live animals.)
    SPORT_FISHING = "sport fishing" # sport fishing (A vessel used in fishing for pleasure or competition.)
    # fmt: on
