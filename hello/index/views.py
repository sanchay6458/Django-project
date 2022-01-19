from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

def indexpage(request):
    return HttpResponse('Hello, WEB MASTER')

def learnpage(request):
    return HttpResponse('Hi, i am smart boy ')

def aboutpage(request):
    return HttpResponse('Hi, see about page ')

def contactpage(request):
    return HttpResponse('Hi, i am contact detail')

def viewpage(request):
    return HttpResponse('Hi, i am view page')

# Create your views here.
