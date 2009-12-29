from django.template import Library
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

from misc.BeautifulSoup import BeautifulSoup

import re
import logging

register = Library()

@stringfilter
def spacify(value, autoescape=None):
    """Given a string in django template,
    convert whitespaces into &nbsp;"""
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    value = mark_safe(re.sub(' ', '&'+'nbsp;', esc(value)))
    return value

spacify.needs_autoescape = True
register.filter(spacify)

@stringfilter
def soup(content):
    content = BeautifulSoup(str(content))
    return content

register.filter(soup)
