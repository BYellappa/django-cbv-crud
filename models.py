from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=20)
    location=models.CharField()
    ceo=models.CharField()