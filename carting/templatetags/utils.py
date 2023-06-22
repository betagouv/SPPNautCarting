from django.template.defaulttags import register
from django import template

register = template.Library()

@register.filter(name='lookup')
def lookup(value, arg):
    return value[arg]

