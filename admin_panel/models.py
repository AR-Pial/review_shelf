import os
from django.db import models
import uuid
from django_countries.fields import CountryField
from accounts.models import TimestampedModel
from django.core.files.storage import default_storage

class Author(TimestampedModel):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255,db_index=True)
    bio = models.TextField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    country = CountryField(blank=True, null=True,db_index=True)
    image = models.ImageField(upload_to='authors/', blank=True, null=True) 

    class Meta:
        db_table = 'author'

    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        """Override delete method to remove the image file from the filesystem."""
        if self.image:
            if os.path.isfile(self.image.path):  # Ensure the file exists
                os.remove(self.image.path)  # Remove the image file from the filesystem
        super().delete(*args, **kwargs)


class Genre(TimestampedModel):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'genres'

    def __str__(self):
        return self.name


class Type(TimestampedModel):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'types'

    def __str__(self):
        return self.name


class Book(TimestampedModel):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255,db_index=True)
    isbn = models.CharField(max_length=255, null=True, blank=True,db_index=True)
    cover_photo = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    prologue = models.TextField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='books',blank=True, null=True,db_index=True)
    co_authors = models.ManyToManyField(Author, related_name='co_authored_books', blank=True)
    first_release_date = models.DateField(blank=True, null=True)
    latest_release_date = models.DateField(blank=True, null=True)
    last_version = models.CharField(max_length=50, blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, related_name='books', null=True, blank=True)
    type = models.ManyToManyField(Type, related_name='books', blank=True)
    

    class Meta:
        db_table = 'books'

    def save(self, *args, **kwargs):
        if self.pk: 
            try:
                old_cover_photo = Book.objects.get(pk=self.pk).cover_photo
                if old_cover_photo and old_cover_photo != self.cover_photo:
                    # Delete the old cover photo if it's different from the new one
                    if default_storage.exists(old_cover_photo.path):
                        default_storage.delete(old_cover_photo.path)
            except Book.DoesNotExist:
                # Handle if for any reason the book doesn't exist
                pass
        
        super(Book, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete the cover photo when the book is deleted
        if self.cover_photo:
            if default_storage.exists(self.cover_photo.path):
                default_storage.delete(self.cover_photo.path)
        
        super(Book, self).delete(*args, **kwargs)

    def __str__(self):
        return self.title
