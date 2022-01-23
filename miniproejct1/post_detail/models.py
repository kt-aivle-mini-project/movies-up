from turtle import update
from django.db import models
from registration.models import User


class MovieTable(models.Model):
    movie_id = models.IntegerField(primary_key=True, null=False)
    movie_title = models.CharField(max_length=100, null=False)
    
    # media/image/ 아래에 저장
    movie_image_info = models.ImageField(blank=True, upload_to="images/", null=False)
    genres = (
        ('AO', 'Action'),
        ('RE', 'Romance'),
        ('HR', 'Horror'),
        ('CY', 'Comedy'),
        ('DA', 'Drama'),
    )
    genre_tag = models.CharField(choices=genres, max_length=30, null=False)
    # 액션, 로맨스, 공포, 코미디, 드라마


class PostTable(models.Model):
    post_id = models.IntegerField(primary_key=True, null=False)
    post_title = models.CharField(max_length=50, null=False)
    post_image = models.ImageField(blank=True, upload_to="images/", null=False)
    post_contents = models.TextField(max_length=1000, null=False)
    recommender = models.ManyToManyField(User, blank=True, related_name='recommend_user')
    date = models.DateTimeField(auto_now_add=True, null=False)
    modify_date = models.DateTimeField(null=True, blank=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    movie_genres = models.ForeignKey(MovieTable, on_delete=models.CASCADE) # 추후 movie_genres로 변경