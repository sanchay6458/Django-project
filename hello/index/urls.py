from django.urls import path
from .views import *

# in this folder we are set the url request and response path

urlpatterns = [
    path('index', indexpage, name='homes'), # in this code client can be request to index page then it link to indexpage function/method to the views.py. and then that function returns the responce in the written by indexpage.
    path('learn/', learnpage, name='learn'),# in this code client can be request to learn page then it link to indexpage function/method to the views.py. and then that function returns the responce in the written by indexpage.
    path('about/', aboutpage, name='about'), # in this code client can be request to about page then it link to indexpage function/method to the views.py. and then that function returns the responce in the written by indexpage.
    path('contact/', contactpage, name='contact'), # in this code client can be request to contact page then it link to indexpage function/method to the views.py. and then that function returns the responce in the written by indexpage.
    path('view/', viewpage, name='view'), # in this code client can be request to view page then it link to indexpage function/method to the views.py. and then that function returns the responce in the written by indexpage.
    path('', home.as_view(), name='indexs'), # in this code client can be request to home page then it link to home class to the views.py. and then that function returns the responce in the written by indexpage.
    path('detail/', about.as_view(), name='abouts'), # in this code client can be request index page then it link to about class to the views.py. and then that function returns the responce in the written by indexpage.
    path('connection/', contact.as_view(), name='contacts'), # in this code client can be request index page then it link to contact class to the views.py. and then that function returns the responce in the written by indexpage.
    path('more/', more.as_view(), name='more') # in this code client can be request index page then it link to more class to the views.py. and then that function returns the responce in the written by indexpage.
]