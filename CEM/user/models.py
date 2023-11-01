from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    