from django.db import models

from accounts.models import Profile
from furniture.models import Furniture


class Review(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    score = models.PositiveIntegerField()
    furniture = models.ForeignKey(Furniture, on_delete=models.CASCADE)
