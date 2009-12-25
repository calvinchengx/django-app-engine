from django.contrib.syndication.feeds import Feed, FeedDoesNotExist

from blog.models import *

class LatestBlogEntries(Feed):
    title="Latest Entries from Calvin's Blog"
    link="/feeds/latest/"
    description="Django, App Engine, jQuery. Software Solutions for Business Problems."

    def items(self):
        return Post.all().fetch(10)

