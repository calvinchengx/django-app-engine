import logging

from django.template import Library

register = Library()

@register.inclusion_tag("menu/menu.html")
def show_menu(current_path=''):
    return {'current_path': current_path} 
    
