# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from google.appengine.ext import db

from misc.utils import set_trace


class Category(db.Model):
    name = db.StringProperty(multiline=False, default='')
    name_slug = db.StringProperty(multiline=False, default='')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/%s/%s' % ('category', self.name_slug)

    class Meta:
        verbose_name_plural = 'Categories'

class Tag(db.Model):
    name = db.StringProperty(multiline=False, default='')
    name_slug = db.StringProperty(multiline=False, default='')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/%s/%s' % ('tag', self.name_slug)

class Post(db.Model):
    title = db.StringProperty(required=True)
    title_slug = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    img = db.BlobProperty()
    modified = db.DateTimeProperty(auto_now=True)
    created = db.DateTimeProperty(auto_now_add=True)
    author = db.ReferenceProperty(User) # Django User
    #author = db.UserProperty()         # Google Account User    
    author_email = db.EmailProperty()
    num_views = db.IntegerProperty(default=0)
    is_published = db.BooleanProperty(default=False)

    #tag = db.ListProperty(db.Key)
    category = db.ReferenceProperty(Category)

    def __unicode__(self):
        return '%s' % (self.title)

    def get_absolute_url(self):
        return '/%s/%s' % ('entry', self.title_slug)

    #def save(self):
        #import logging
        #logging.info(self.content)
        #super(Post, self).save()

class TagPost(db.Model):
    post = db.ReferenceProperty(Post, required=True, 
                                collection_name='post')
    tag = db.ReferenceProperty(Tag, required=True,
                               collection_name='Tag')

    def __unicode__(self):
        return '%s is tagged as %s' % (self.post, self.tag)

class BlogRoll(db.Model):
    link = db.StringProperty()
    desc = db.StringProperty()
    target = db.StringProperty(default='_blank', 
                               multiline=False,
                               choices=['_blank', '_self'])
    created = db.DateTimeProperty(auto_now_add=True)
    status = db.BooleanProperty(default=True)

    def __unicode__(self):
        return '<a target="%s" href="http://%s">%s</a>' % (self.target, 
                                                    self.link,
                                                    self.desc)

