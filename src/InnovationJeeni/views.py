from django.shortcuts import render
from django.core.context_processors import request
'''
Created on 3 Jun 2015

@author: Adam
'''


def index(request):
    print("Main index Page")
    return render(request, 'web/index.html', {})

def innovation(request):
    print("Innovation Page")
    return render(request, 'web/innovation.html', {})

def closethegap(request):
    print("Innovation Page")
    return render(request, 'web/closethegap.html', {})


def executeyourbusiness(request):
    print("executeyourbusiness Page")
    return render(request, 'web/executeyourbusiness.html', {})

def highperformanceteams(request):
    print("highperformanceteams Page")
    return render(request, 'web/highperformanceteams.html', {})

def fastsoftwaredelivery(request):
    print("fastsoftwaredelivery Page")
    return render(request, 'web/fastsoftwaredevelopment.html', {})

def websitesthatkill(request):
    print("websitesthatkill Page")
    return render(request, 'web/websitesthatkill.html', {})

def casestudies(request):
    print("casestudies Page")
    return render(request, 'web/casestudies.html', {})

