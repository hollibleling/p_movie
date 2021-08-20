from django.db import models
from actors.models import Actor

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=45)
    release_date = models.DateField()
    running_time = models.IntegerField()
    actors = models.ManyToManyField(Actor)

    class Meta:
        db_table = 'movies'
