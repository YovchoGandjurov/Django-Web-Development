from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Appointment
from .serializers import AppointmentSerializier
from .permissions import PatientChecker, IsOwner


class AppointmentList(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializier
    permission_classes = [IsAuthenticated, PatientChecker]


class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializier
    permission_classes = [IsAuthenticated, PatientChecker, IsOwner]
