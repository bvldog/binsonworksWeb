from django.db import models

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    descriptions = models.TextField()
    my_name = models.CharField(max_lengt=100)
    captain_photo = models.ImageField(upload_to='media/captain_photo/')
    capatin_intro = models.TextField()
    
