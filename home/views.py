# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    template = loader.get_template('home/about.html')
    #return HttpResponse("Hello, world. You're at tdfgsdfxhe polls index.")
    context={}
    return HttpResponse(template.render(context, request))