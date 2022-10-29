from django.db import models

class Artiste(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

class Song(models.Model):
    Title = models.CharField(max_length=30)
    date_released = models.DateField()
    likes = models.CharField(max_length=20)
    artiste_id = models.CharField(max_length=20)
    
class Lyric(models.Model):
    content = models.CharField(max_length=30)
    song_id = models.CharField(max_length=30)

