from django.db import models

# Create your models here.
class MainPage(models.Model):
    site_logo = models.CharField(max_length=200)
    site_image = models.ImageField(upload_to='media', blank=True)
    site_image2 = models.ImageField(upload_to='media', blank=True)
    site_image3 = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.site_logo


class About(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    descriptions = models.TextField(blank=True)
    my_name = models.CharField(max_length=100)
    captain_photo = models.ImageField(upload_to='media/captain_photo/')
    captain_intro = models.TextField(blank=True)


    def __str__(self):
        return self.title
