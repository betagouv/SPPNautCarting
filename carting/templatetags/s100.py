from django import template
from xsdata.formats.dataclass.parsers import XmlParser

from carting.models import S1xyObject
from carting.s127_models import Dataset

register = template.Library()


def retrieve_dataset_from_href(href):
    id = href.replace("#", "")
    s1xyobject = S1xyObject.objects.get(id=id)

    parser = XmlParser()
    dataset = parser.from_string(s1xyobject.content, Dataset)
    return dataset


@register.inclusion_tag("contact_details.html")
def contact_details(href):
    dataset = retrieve_dataset_from_href(href)
    # TODO A partir d'ici + inclusion_tag, ce n'est plus générique
    contact_details = dataset.imember[0].contact_details

    return {"self": contact_details}


@register.inclusion_tag("autority.html")
def authority(href):
    dataset = retrieve_dataset_from_href(href)
    # TODO A partir d'ici + inclusion_tag, ce n'est plus générique
    authority = dataset.imember[0].authority

    return {"self": authority}


@register.inclusion_tag("ship_report.html")
def ship_report(href):
    dataset = retrieve_dataset_from_href(href)
    # TODO A partir d'ici + inclusion_tag, ce n'est plus générique
    ship_report = dataset.imember[0].ship_report

    return {"self": ship_report}


@register.inclusion_tag("rx_n.html")
def rx_n(href):
    dataset = retrieve_dataset_from_href(href)
    # TODO A partir d'ici + inclusion_tag, ce n'est plus générique
    regulations = dataset.imember[0].regulations

    return {"self": regulations}


@register.inclusion_tag("pilot_boarding_place.html")
def consist_of(href):
    dataset = retrieve_dataset_from_href(href)

    # TODO A partir d'ici + inclusion_tag, ce n'est plus générique
    pilot_boarding_place = dataset.member[0].pilot_boarding_place

    return {"self": pilot_boarding_place}


@register.inclusion_tag("permission.html")
def permission(href):
    dataset = retrieve_dataset_from_href(href)

    # TODO A partir d'ici + inclusion_tag, ce n'est plus générique
    permission_type = dataset.imember[0].permission_type
    return {"self": permission_type}


@register.inclusion_tag("applicability.html")
def applicability(href):
    dataset = retrieve_dataset_from_href(href)

    # TODO A partir d'ici + inclusion_tag, ce n'est plus générique
    applicability = dataset.imember[0].applicability
    print(applicability)
    return {"self": applicability}
