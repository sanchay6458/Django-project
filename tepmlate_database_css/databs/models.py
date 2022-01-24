from django.db import models

class db1(models.Model):
    particular = models.CharField(max_length=20)
    quantity = models.IntegerField()
    description = models.TextField()
    def __str__(self):
        return self.particular

# Create your models here.
