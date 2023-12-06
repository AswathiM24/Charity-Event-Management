from django.db import models
from user.models import Organization


# Create your models here.
class Login(models.Model):
    email = models.EmailField(unique=True)
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
    password = models.CharField(max_length=255)
    status = models.BooleanField(default=False)


class UserInfo(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    auth = models.OneToOneField(Login, on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

