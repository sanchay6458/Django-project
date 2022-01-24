from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class index(TemplateView):
    template_name = 'index.html'

class about(TemplateView):
    template_name = 'about.html'

class contact(TemplateView):
    template_name = 'contact.html'

class view(TemplateView):
    template_name = 'view.html'

class more(TemplateView):
    template_name = 'more.html'

# Create your views here.
