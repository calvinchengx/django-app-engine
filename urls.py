# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from ragendja.urlsauto import urlpatterns
from ragendja.auth.urls import urlpatterns as auth_patterns
from myapp.forms import UserRegistrationForm
from django.contrib import admin

from blog.feeds import LatestBlogEntries 

feeds = {
    'latest': LatestBlogEntries,
}

admin.autodiscover()

handler500 = 'ragendja.views.server_error'

urlpatterns = auth_patterns + patterns('',
    ('^admin/(.*)', admin.site.root),
    #(r'^$', 'django.views.generic.simple.direct_to_template',{'template': 'main.html'}),
    #(r'^$', 'homepage.views.index'),
    (r'^$', 'blog.views.index'),

    # Rss feeds
    (r'^feed/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),

    # Blog app
    (r'^category/(?P<name_slug>[^/]+)/$', 'blog.views.category'),
    url(r'^entry/', include('blog.urls')),

    # Contact app
    url(r'^contact/', include('contact.urls')),

    # Override the default registration form
    url(r'^account/register/$', 'registration.views.register',
        kwargs={'form_class': UserRegistrationForm},
        name='registration_register'),
) + urlpatterns
