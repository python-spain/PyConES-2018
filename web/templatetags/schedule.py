from django import template
from django.utils.text import slugify
from django.utils.translation import gettext as _

from web.views import TALKS

register = template.Library()


@register.simple_tag
def locale_category(category):
    if category == "ml":
        return _("Machine Learning")
    if category == "core":
        return _("Core")
    if category == "web":
        return _("Web")
    if category == "edu":
        return _("Education")
    if category == "science":
        return _("Science")
    if category == "dev":
        return _("DevOps & Tools")
    if category == "testing":
        return _("Testing")
    if category == "sec":
        return _("Security")
    if category == "mc":
        return _("Microservices")
    if category == "workshop":
        return _("Workshop")
    return ""


@register.inclusion_tag('blocks/schedule-talk.html')
def schedule_talk(title):
    try:
        slug = slugify(title)
        talk = TALKS[slug]

        return talk
    except KeyError:
        return {
            title: title,
        }
