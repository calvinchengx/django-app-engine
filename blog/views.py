# -*- coding: utf-8 -*-
import datetime

from django.http import HttpResponseRedirect, Http404
from django.utils.translation import ugettext as _
from ragendja.template import render_to_response

from blog.models import *

import code

def index(request):
    
    query = Post.all()
    post_list = query.filter('is_published =', True).order('-created')
    if not post_list:
        post_list = None

    current_time = datetime.datetime.now()
    data = {'post_list': post_list, 'current_time': current_time}

    return render_to_response(request, 'blog/index.html', data) 

def post(request, title_slug):
    
    query = Post.all()
    post = query.filter('title_slug =', title_slug).get() 
    if not post:
        post = None
        raise Http404

    edit_link = None
    if request.user == post.author:
        edit_link = '%s/%s/' % (post.get_absolute_url(), 'edit')

    data = {'post': post, 'edit_link': edit_link}

    return render_to_response(request, 'blog/post.html', data) 
    
def category(request, name_slug):

    query = Category.all()
    category = query.filter('name_slug =', name_slug).get()
    if not category:
        category = None
        post_list = None
        raise Http404
    else:
        query = Post.all()
        post_list = query.filter('category =', category)
        if not post_list:
            post_list = None

    data = {'category': category, 'post_list': post_list}

    return render_to_response(request, 'blog/category.html', data)


