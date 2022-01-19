# Note:- Explanation of bellow code:- the client can be request a page then that request go to urls.py of that main page(like:- hello is a project name then index is page of that project so "index/urls.py")
# then after urls match the request to set path and then the url is match then send to the views.py of the project page (means "index/views.py")
# then after match the request and provide the respoce on the cliend side.
from django.shortcuts import render
from django.http import HttpResponse #import cliend responce
from django.views.generic import TemplateView #importing html codes

def indexpage(request): #creating indexpage method
    return HttpResponse('Hello, WEB MASTER') # returns the responce after request indexpage

def learnpage(request): #creating learnpage method
    return HttpResponse('Hi, i am smart boy ')

def aboutpage(request): #creating aboutpage method
    return HttpResponse('Hi, see about page ')

def contactpage(request): #creating contactpage method
    return HttpResponse('Hi, i am contact detail')

def viewpage(request): #creating viewpage method
    return HttpResponse('Hi, i am view page')

class home(TemplateView): #creating home class. home class is a chield class and templates is pairent class.
    template_name = 'index.html' # it returns respone of html page by request of home class

class about(TemplateView):
    template_name = 'about.html'

class contact(TemplateView):
    template_name = 'contact.html'

class more(TemplateView):
    template_name = 'more.html'
# Create your views here.


 
