from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()

class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    date_released = models.DateField()
    likes = models.CharField(max_length=400)


class Lyric(models.Model):
    Song = models.ForeignKey(Song, on_delete=models.CASCADE)
    song_id = models.ForeignKey(to=Song, on_delete=Song)
    content = models.CharField(max_length=200000000)



