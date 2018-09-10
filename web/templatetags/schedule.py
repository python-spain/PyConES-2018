from django import template
from django.utils.text import slugify

from web.views import TALKS

register = template.Library()


@register.inclusion_tag('blocks/schedule-talk.html')
def schedule_talk(title):
    try:
        slug = slugify(title)
        talk = TALKS[slug]
        names = talk["name"].replace(' & ', ',').replace(' y ', ',').split(',')
        talk["speakers"] = ", ".join(names) if len(names) > 2 else "\n".join(names)
        return talk
    except KeyError:
        return {
            title: title,
        }
