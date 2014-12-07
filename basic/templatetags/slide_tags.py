from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.inclusion_tag('_lowerbars.html')
def show_lowerbars(slides):
    return {'slides': slides}

@register.inclusion_tag('_sidebars.html')
def show_siderbars(slides):
    return {'slides': slides}

@register.inclusion_tag('_pics.html')
def show_pics(slides):
    return {'slides': slides}