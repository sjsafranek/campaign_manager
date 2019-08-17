import uuid
import base64
from django.db import models
from django.contrib.auth.models import User
from django.db.models.constraints import UniqueConstraint
# from django.contrib.postgres.fields import ArrayField



class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')


class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    file = models.ImageField(upload_to='files')


class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    contents = models.TextField(blank=True)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    UniqueConstraint(fields=['slug'], name='unique_slug')

    def __str__(self):
        return self.title


class Character(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    biography = models.TextField(blank=True)
    is_pc = models.BooleanField(default=False)
    gender = models.CharField(
        max_length=10,
        choices=[
            ('male', 'male'),
            ('female', 'female'),
            ('other', 'other'),
        ],
        default='other'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Campaign(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    users = models.ManyToManyField(User, blank=True)
    pages = models.ManyToManyField(Page, blank=True)
    files = models.ManyToManyField(File, blank=True)
    images = models.ManyToManyField(Image, blank=True)
    characters = models.ManyToManyField(Character, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
