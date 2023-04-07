from django import template
from xsdata.formats.dataclass.parsers import XmlParser

from carting.models import S1xyObject
from carting.s127_models import Dataset

register = template.Library()


@register.inclusion_tag("pilot_boarding_place.html")
def consist_of(href):
    id = href.replace("#", "")
    s1xyobject = S1xyObject.objects.get(id=id)

    parser = XmlParser()
    dataset = parser.from_string(s1xyobject.content, Dataset)

    # TODO A partir d'ici + inclusion_tag, ce n'est plus générique
    pilot_boarding_place = dataset.member[0].pilot_boarding_place

    return {"self": pilot_boarding_place}


@register.inclusion_tag("permission.html")
def permission(href):
    id = href.replace("#", "")
    s1xyobject = S1xyObject.objects.get(id=id)

    parser = XmlParser()
    dataset = parser.from_string(s1xyobject.content, Dataset)

    # TODO A partir d'ici + inclusion_tag, ce n'est plus générique
    permission_type = dataset.imember[0].permission_type
    return {"self": permission_type}


@register.inclusion_tag("applicability.html")
def applicability(href):
    id = href.replace("#", "")
    s1xyobject = S1xyObject.objects.get(id=id)

    parser = XmlParser()
    dataset = parser.from_string(s1xyobject.content, Dataset)

    # TODO A partir d'ici + inclusion_tag, ce n'est plus générique
    applicability = dataset.imember[0].applicability
    print(applicability)
    return {"self": applicability}
