from django.db import models

class UserTable(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20, null=False)
    password = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=50, null=True)
    user_name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.user_name

class PostTable(models.Model):
    post_id = models.AutoField(primary_key=True, null=False) #autoincrement 로 하려면 없애야하나?
    post_title = models.CharField(max_length=50, null=False)
    post_image = models.ImageField()
    post_contents = models.TextField(max_length=1000, null=False)
    post_like = models.IntegerField(default=0, null=False)
    date = models.DateField(null=False)
    user_id = models.ForeignKey(UserTable, on_delete=models.CASCADE)

