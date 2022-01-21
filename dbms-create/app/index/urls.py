from django.urls import path
from .views import *

urlpatterns = [
    path('', indexpage.as_view() ,name='indexs'),
    path('about/', about.as_view() , name='about'),
    path('contact/', contact.as_view() , name='contact'),
    path('more/', more.as_view() , name='more')
]