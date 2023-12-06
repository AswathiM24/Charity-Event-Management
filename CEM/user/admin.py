from django.contrib import admin
from .models import User, Organization, Login, Events

# Register your models here.
# admin.site.register(User)
# admin.site.register(Login)
# admin.site.register(Organization)
# admin.site.register(Events)

from django.apps import apps


models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass