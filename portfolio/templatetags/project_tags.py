from django import template
from django.template.defaultfilters import stringfilter
# from django.contrib.gis.gdal.prototypes.errcheck import arg_byref
from random import randrange

register = template.Library()

@register.filter
@stringfilter
def upper(value):
    """Converts a string into all uppercase"""
    return value.upper()

# @register.filter
# def linkjoin(value, arg):
#     

@register.filter
@stringfilter
def include(value, arg):
    if value == 'None':
        return ''
    return arg

@register.filter
@stringfilter
def get_tree(value):
    if value == 'None':
        return 'flower-' + str(randrange(4)) + '.svg'
    return 'tree-' + str(randrange(5)) + '.svg'

@register.inclusion_tag('_projects.html')
def show_projects(projects):
    return {'projects': projects}

@register.inclusion_tag('_trees.html')
def show_trees(trees):
    return {'trees': trees}

@register.inclusion_tag('_navi.html')
def show_navi():
    pass
