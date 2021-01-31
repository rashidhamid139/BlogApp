from django.db import models

# Create your models here.

# class Person(models.Model):
#     first_name  = models.CharField( max_length = 100)
#     last_name   = models.CharField( max_length = 100)


class Musician(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', "Large"),
    )
    name = models.CharField(max_length=100)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


class Runner(models.Model):
    MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
    name = models.CharField(max_length=100)
    medal = models.CharField(
        blank=True, choices=MedalType.choices, max_length=10)


class MetaClassOptions(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        pass
        # abstract    =   True #This class will be used as abstract base class
        # app_label   =   "my_app" #if you are writing this Model outside specify the app_name to which this class belongs
        # db_table    =   "music_album" #the name of table in the database

# Many-to-one Relationship


class Reporter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name } { self.last_name }"


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.headline } By {self.reporter.first_name  }"

    class Meta:
        ordering = ['headline']
