from turtle import title
from django.db import models

class dbms1(models.Model):
    title = models.CharField(max_length=20)
    quantity = models.IntegerField()
    def __str__(self):
        return self.title[:30]

# Create your models here.
