from django.db import models
import uuid
from django_countries.fields import CountryField


class Author(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    country = CountryField(blank=True, null=True)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return self.name


class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'genres'

    def __str__(self):
        return self.name


class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'types'

    def __str__(self):
        return self.name


class Book(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    cover_photo = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    prologue = models.TextField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    co_authors = models.ManyToManyField(Author, related_name='co_authored_books', blank=True)
    first_release_date = models.DateField(blank=True, null=True)
    latest_release_date = models.DateField(blank=True, null=True)
    last_version = models.CharField(max_length=50, blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='books', null=True, blank=True)
    types = models.ManyToManyField(Type, related_name='books', blank=True)

    class Meta:
        db_table = 'books'

    def __str__(self):
        return self.title
