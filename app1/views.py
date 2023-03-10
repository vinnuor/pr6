from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rolex(request):
    return HttpResponse('<h1>life time settelement raa!!</h1>')


def santaanam(request):
    return HttpResponse('<h1><marquee>never say to die</marquee></h1>')