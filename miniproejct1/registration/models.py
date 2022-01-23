from django.db import models

class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)               # user
    password = models.CharField(max_length=20)                                # user
    email = models.CharField(null=True, max_length=50)
    user_name = models.CharField(max_length=20)                               # user