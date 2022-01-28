from django.db import models

GENRE_CHOICES = (

    ('action', 'Action'),
    ('romance', 'Romance'),
    ('horror', 'Horror'),
    ('comedy', 'Comedy'),
    ('drama', 'Drama'),
)


STATUS_CHOICES = (
    ('RA','RECENTLY ADDED'),
    ('MC','MOST COMMENTED'),
    ('TR','TOP RATED'),
)

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True, null=False)
    movie_title = models.CharField(max_length=100, null=False)
    movie_image_info = models.ImageField(upload_to = 'movies', null=False)
    genre_tag = models.CharField(choices=GENRE_CHOICES,max_length=10, null=False)
    status = models.CharField(choices=STATUS_CHOICES,max_length=2, null=False)
    movie_image_bg = models.ImageField(upload_to = 'images',null = True)

    def __str__(self):
        return self.movie_title

