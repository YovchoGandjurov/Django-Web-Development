from django.db import models


class Owner(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


class Animal(models.Model):
    KIND_CHOICES = (
        ('C', 'Cat'),
        ('D', 'Dog')
    )

    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    breed = models.CharField(max_length=20)
    description = models.TextField()
    image_url = models.URLField()
    kind = models.CharField(max_length=1, choices=KIND_CHOICES)
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True,
                              blank=True)

    def __str__(self):
        return f"{self.name}, kind {self.breed}"
