from django.template import Library
from google.appengine.ext import db

from blog.models import *

register = Library()

@register.inclusion_tag("blog/blogroll.html")
def show_blogroll():
    blogroll = BlogRoll.all() 
    return {'blogroll': blogroll}

@register.inclusion_tag("blog/categories.html")
def show_categories():
    c_list = Category.all() 
    return {'c_list': c_list}

