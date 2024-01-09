from django.db import models

class ksasha(models.Model):
    name = models.CharField(max_length=255)
    image=models.CharField(max_length=2080)
    payment=models.FloatField()
    email=models.EmailField()
    reg_no=models.CharField(max_length=50)