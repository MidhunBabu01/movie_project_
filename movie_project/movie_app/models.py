from django.db import models
from embed_video.fields import EmbedVideoField


# Create your models here.



# in theatre



class ComingSooon(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="pictures")

# MOVIE DETIALS

class MovieDetailss(models.Model):
    category_choices = (
        ('popular', 'popular'),
        ('comingsoon', 'comingsoon'),
        ('toprated', 'toprated'),
        ('flop', 'flop'),
    )
    def __str__(self):
       return self.moviename
    overview = models.TextField()
    moviename = models.CharField(max_length=150)
    year = models.IntegerField()

    categories = models.CharField(max_length=250, choices=category_choices)
    rating = models.FloatField()
    # cast
    heroorgname = models.CharField(max_length=150)
    img_hero = models.ImageField(upload_to="pictures")
    heroinorgname = models.CharField(max_length=150)
    img_heroine = models.ImageField(upload_to="pictures")
    anotherartistorgname = models.CharField(max_length=150)
    img_artist1 = models.ImageField(upload_to="pictures")
    anotherartistorgname2 = models.CharField(max_length=150)
    img_artist2 = models.ImageField(upload_to="pictures")
    heromoviename = models.CharField(max_length=150)
    heroinmoviename = models.CharField(max_length=150)
    anotherartistmoviename = models.CharField(max_length=150)
    anotherartistmoviename2 = models.CharField(max_length=150)

    director = models.CharField(max_length=150)
    writer = models.CharField(max_length=150)
    genere = models.CharField(max_length=150)
    rlsdate = models.CharField(max_length=150)
    runtime = models.CharField(max_length=150)
    img = models.ImageField(upload_to="pictures")
    trailerlink = EmbedVideoField()
    traillername = models.CharField(max_length=250)
    trillerimg = models.ImageField(upload_to="pictures")

    # # MEDIA
    video_song_img = models.ImageField(upload_to="pictures",blank=True)
    video_song_name = models.CharField(max_length=100,blank=True)
    video_song_link = EmbedVideoField(blank=True)
    video_song_img2 = models.ImageField(upload_to="pictures",blank=True)
    video_song_name2 = models.CharField(max_length=100,blank=True)
    video_song_link2 = EmbedVideoField(blank=True)
    video_song_name3 = models.CharField(max_length=100,blank=True)
    video_song_img3 = models.ImageField(upload_to="pictures",blank=True)
    video_song_link3 = EmbedVideoField(blank=True)
    video_song_img4 = models.ImageField(upload_to="pictures",blank=True)
    video_song_name4 = models.CharField(max_length=100,blank=True)
    video_song_link4 = EmbedVideoField(blank=True)



class LatestNews(models.Model):
    def __str__(self):
        return self.tittle
    img = models.ImageField(upload_to="pictures")
    tittle = models.CharField(max_length=250)
    desc = models.TextField()




