# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    try:
        print request.session['user_id']
    except KeyError:
        print "no such key"
    return render(request, 'my_app/index.html')

def test(request, user_id):
    request.session['user_id'] = user_id
    return HttpResponse("testing we got {} as user_id".format(user_id))

def reset(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')