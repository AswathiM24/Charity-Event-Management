from django.contrib import admin
from .models import User,Organization,Login
# Register your models here.
admin.site.register(User)
admin.site.register(Login)
admin.site.register(Organization)