from django.db import models


class Appointment(models.Model):
    date = models.DateTimeField()
    reason = models.CharField(max_length=200)
