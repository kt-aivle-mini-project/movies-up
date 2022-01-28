from django.db import models

class UserTable(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20, null=False)
    password = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=50, null=True)
    user_name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.user_name

