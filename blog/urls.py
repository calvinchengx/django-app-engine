from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
                       (r'^$', 'index'),
                       url(r'^(?P<title_slug>[^/]+)/$', 'post'), 
                      )
