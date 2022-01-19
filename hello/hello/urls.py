"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Note:- Explanation of bellow code:- the client can be request a page then that request go to urls.py of that main page(like:- hello is a project name then index is page of that project so "index/urls.py")
# then after urls match the request to set path and then the url is match then send to the views.py of the project page (means "index/views.py")
# then after match the request and provide the respoce on the cliend side.
from django.contrib import admin
from django.urls import path,include

# in this file we are set he path of pages of the project

urlpatterns = [
    path('admin/', admin.site.urls), # This code link to admin page
    path('', include('index.urls')), # This code link to index page
]
