from django.shortcuts import render
from rest_framework import generics

from .models import Appointment
from .serializers import AppointmentSerializier


class AppointmentList(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializier
