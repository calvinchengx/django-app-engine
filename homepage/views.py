# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from ragendja.template import render_to_response

def index(request):
    return render_to_response(request, 'homepage/index.html')
