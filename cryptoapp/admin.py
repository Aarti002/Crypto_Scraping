from django.contrib import admin

# Register your models here.

from .models import SubscribedUsers
admin.site.register(SubscribedUsers)