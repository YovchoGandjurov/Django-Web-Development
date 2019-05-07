from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='user')

    def __str__(self):
        return f"{self.user}"


class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               related_name="books")
    description = models.TextField()
    cover_image_url = models.URLField(blank=True)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"book {self.title} with author {self.author}"
