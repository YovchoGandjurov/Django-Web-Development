from django.db import models


class News(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    text = models.TextField()
