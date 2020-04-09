from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(requset):
    return HttpResponse('hello')
