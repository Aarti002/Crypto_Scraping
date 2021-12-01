from django.db import models

# Create your models here.
class SubscribedUsers(models.Model):
    email = models.CharField(unique=True, max_length=50,null=True)
    password = models.CharField(max_length=50,null=True)
    yes_no=models.BooleanField(default=False,null=True)
    objects = models.Manager()
