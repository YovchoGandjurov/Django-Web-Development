from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.validators import validators

from .enums import Specialties, Gender


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(validators=[
                validators.MinValueValidator(25)])
    specialty = models.CharField(max_length=20, choices=[
                                (e.name, e.value) for e in Specialties
                                ])

    def __str__(self):
        return f'{self.user}'


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=8,
                              choices=[(g.name, g.value) for g in Gender])

    def __str__(self):
        return f'{self.user}'
