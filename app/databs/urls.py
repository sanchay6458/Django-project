from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.databs, name = 'post')
]