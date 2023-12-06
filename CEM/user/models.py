import datetime

from django.db import models
from django.contrib.auth.hashers import make_password


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    fund_raised = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Login(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    obj = models.OneToOneField(Organization, on_delete=models.CASCADE, related_name='org')

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)


class Events(models.Model):
    Name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.TextField()
    org_name = models.CharField(max_length=255)
    org_email = models.EmailField()
    org_phone = models.IntegerField()
    is_booking = models.BooleanField(default=False)
    ticket_price = models.IntegerField()
    is_active = models.BooleanField(default=True)
    date = models.DateField(null=True, blank=True)
    organization = models.CharField(max_length=255)

    def __str__(self):
        return self.Name

class Tickets(models.Model):
    issue = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True)
    action= models.CharField(max_length=1000,blank=True,default='',null=True)
    open_date = models.DateField()
    closed_date = models.DateField(null=True, blank=True)


class payments(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    order_id = models.CharField(max_length=255)
    amount = models.IntegerField()
    merchant_key = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
