from django.db import models

# Create your models here.

class Post(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True)
    slug = models.SlugField(verbose_name="Slug")
    title = models.TextField(max_length=255)
    content = models.TextField(max_length=100000)
    image = models.ImageField(upload_to='images')

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True)
    name = models.TextField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(max_length=10000)