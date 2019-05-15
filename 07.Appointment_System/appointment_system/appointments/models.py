from django.db import models

from .enums import StatusEnum

from accounts.enums import Specialties
from accounts.models import Patient, Doctor


class Appointment(models.Model):
    date = models.DateField()
    reason = models.CharField(max_length=200)
    doctor_type = models.CharField(
                        max_length=20,
                        choices=[(s.name, s.value) for s in Specialties])
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE,
                                  blank=True, null=True)
    status = models.CharField(max_length=20,
                              choices=[(s.name, s.value) for s in StatusEnum],
                              default=StatusEnum.P)
