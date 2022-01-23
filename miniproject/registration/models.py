from django.db import models

class UserTable(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)               
    password = models.CharField(max_length=20)                                
    email = models.CharField(null=True, max_length=50)
    user_name = models.CharField(max_length=20)
