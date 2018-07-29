# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Scale

# Create your views here.

def home(request):
    scale = Scale.objects.all()
    return render(request, 'home.html', {'scale': scale})