from django.urls import path
from .views import *

urlpatterns = [
    path('', indexpage, name='home'),
    path('learn/', learnpage, name='learn'),
    path('about/', aboutpage, name='about'),
    path('contact/', contactpage, name='contact'),
    path('view/', viewpage, name='view'),
]