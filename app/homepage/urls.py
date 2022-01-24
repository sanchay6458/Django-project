from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('about/', about.as_view(), name='about'),
    path('contact/', contact.as_view(), name='contact'),
    path('more/', more.as_view(), name='more'),
    path('view', view.as_view(), name='view')
]