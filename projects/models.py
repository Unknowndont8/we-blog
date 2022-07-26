from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    author = models.TextField()
    image = models.FilePathField(path="/img")
# Create your models here.
