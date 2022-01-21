from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class indexpage(TemplateView):
    template_name = 'indexs.html'

class about(TemplateView):
    template_name = 'about.html'

class contact(TemplateView):
    template_name = 'contact.html'

class more(TemplateView):
    template_name = 'more.html'


# Create your views here.
