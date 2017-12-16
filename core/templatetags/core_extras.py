
from django import template

from json2html import json2html

from core import utils

register = template.Library()


@register.filter
def render_json2html(data, path):
    if path:
        jdata = utils.access(data, path)
    else:
        jdata = data
    return json2html.convert(json=jdata, table_attributes="class=\"table table-striped table-bordered table-hover\"")


@register.filter
def range(value):
    return xrange(value)
