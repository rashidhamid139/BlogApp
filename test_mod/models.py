from django.db import models

# Create your models here.

# class Person(models.Model):
#     first_name  = models.CharField( max_length = 100)
#     last_name   = models.CharField( max_length = 100)

class Musician( models.Model ):
    first_name  = models.CharField( max_length = 100 )
    last_name   = models.CharField( max_length = 100 )
    instrument  = models.CharField( max_length = 100 )

class Album( models.Model ):
    artist  = models.ForeignKey( Musician, on_delete=models.CASCADE )
    name    = models.CharField(max_length=100)
    release_date    = models.DateField()
    num_stars       = models.IntegerField()


class Person( models.Model ):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', "Large"),
    )
    name = models.CharField( max_length=100 )
    shirt_size  = models.CharField( max_length=1, choices=SHIRT_SIZES )


class Runner( models.Model ):
    MedalType   =   models.TextChoices( 'MedalType', 'GOLD SILVER BRONZE' )
    name        =   models.CharField( max_length=100 )
    medal       =   models.CharField( blank=True, choices=MedalType.choices, max_length=10 )