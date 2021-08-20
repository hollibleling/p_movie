from django.db import models

# Create your models here.

class Actor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    date_of_birth = models.DateField()
    
    class Meta:
        db_table = 'actors'
