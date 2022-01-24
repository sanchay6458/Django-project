from django.shortcuts import render
from .models import db1

def databs(request):
    fruit = {
        'frts' : db1.objects.all()
    }
    return render(request, 'dbdata.html', fruit)
# Create your views here.
