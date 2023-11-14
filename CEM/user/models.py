from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class Organization(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=10)
    def __str__(self):
        return self.name


class Login(models.Model):
    email=models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    obj=models.OneToOneField(Organization,on_delete=models.CASCADE,related_name='org')

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)