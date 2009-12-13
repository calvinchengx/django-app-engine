# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from ragendja.template import render_to_response
from blog.models import *

def index(request):
    
    post_list = Post.all().filter('is_published =', True).order('-created')
    
    if not post_list:
        post_list = None

    data = {'post_list': post_list}

    return render_to_response(request, 'homepage/index.html', data) 
