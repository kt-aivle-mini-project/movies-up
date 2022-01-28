from django.db import models
from myinfo.models import UserTable
from main.models import Movie

class PostTable(models.Model):
    post_id = models.AutoField(primary_key=True, null=False)
    post_title = models.CharField(max_length=50, null=False)
    post_image = models.ImageField(blank=True, upload_to="images/", null=False)
    post_contents = models.TextField(max_length=1000, null=False)
    recommender = models.ManyToManyField(UserTable, blank=True, related_name='recommend_user')
    date = models.DateTimeField(auto_now_add=True, null=False)
    modify_date = models.DateTimeField(null=True, blank=True)
    user_name = models.ForeignKey(UserTable, on_delete=models.CASCADE, related_name='post_user')
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title
    
class CommentTable(models.Model):
    comment_id = models.AutoField(primary_key=True, null=False)
    author = models.ForeignKey(UserTable, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000, null=False)
    create_date = models.DateTimeField(auto_now_add=True, null=False)
    post_table = models.ForeignKey(PostTable, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.user_name
