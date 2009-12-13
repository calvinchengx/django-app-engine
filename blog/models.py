# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from google.appengine.ext import db

class Post(db.Model):
    title = db.StringProperty(required = True)
    title_slug = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    modified = db.DateTimeProperty(auto_now = True)
    created = db.DateTimeProperty(auto_now_add = True)
    author = db.UserProperty()
    author_email = db.EmailProperty()
    num_views = db.IntegerProperty(default = 0)
    is_published = db.BooleanProperty(default = False)

    def __unicode__(self):
        return '%s' % (self.title)
