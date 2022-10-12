from django.template.defaulttags import register


@register.filter
def caption_with_date(date):
    return "test" + date
