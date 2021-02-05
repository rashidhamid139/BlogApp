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


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey( Blog, on_delete=models.CASCADE)
    headline    = models.CharField( max_length=200)
    body_text   = models.TextField()
    pub_date    = models.DateField()
    mod_date    = models.DateField()
    authors     = models.ManyToManyField(Author)
    number_of_comments  = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating      = models.IntegerField()


    def __str__(self):
        return self.headline


class RemoteAPIAccount(models.Model):
    access_token = models.CharField(max_length=200)
    access_token_expires = models.DateTimeField()


    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_single_instance",
                check=models.Q(id=1),
            )
        ]