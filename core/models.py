from django.db import models

# Create your models here.

class Post(models.Model):
    id = models.UUIDField(primary_key=True, auto_created=True)
    title = models.TextField(max_length=255)
    content = models.TextField(max_length=100000)
    image = models.ImageField()