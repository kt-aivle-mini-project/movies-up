# Generated by Django 4.0.1 on 2022-01-26 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_posttable_movie_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_image_bg',
            field=models.ImageField(null=True, upload_to='movies'),
        ),
    ]
