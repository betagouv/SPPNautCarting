from django import template
from xsdata.formats.dataclass.parsers import XmlParser

from carting.models import S1xyObject
from carting.s127_models import Dataset

register = template.Library()


@register.filter
def follow_link_through(dataclass, model_instance):
    return model_instance.follow_link(dataclass)


def _retrieve_dataclass_from_href(href):
    id = href.replace("#", "")
    s1xyobject = S1xyObject.objects.get(id=id)
    return {"self": s1xyobject.as_dataclass}


@register.inclusion_tag("pilot_boarding_place.html")
def consist_of(href):
    return _retrieve_dataclass_from_href(href)
