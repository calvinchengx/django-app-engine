from django.template import Library
from google.appengine.ext import db
register = Library()

@register.inclusion_tag("myapp/person.html")
def show_person():
    from myapp.models import Person 
    from django.contrib.auth.models import User
    person = None
    u = User.all().filter('username =', 'admin').get()
    return { 'person': person, 'u': u}
