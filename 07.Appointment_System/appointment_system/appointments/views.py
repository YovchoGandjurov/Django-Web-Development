from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Appointment
from .serializers import AppointmentSerializier, AppointmentCreateSerializer
from .permissions import PatientChecker, IsOwner
from .method_serializer_view import MethodSerializerView


class AppointmentList(MethodSerializerView, generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    method_serializer_classes = {
        ('GET', ): AppointmentSerializier,
        ('POST'): AppointmentCreateSerializer
    }
    permission_classes = [IsAuthenticated, PatientChecker]


class AppointmentDetail(MethodSerializerView,
                        generics.RetrieveUpdateDestroyAPIView):

    queryset = Appointment.objects.all()

    method_serializer_classes = {
        ('GET', ): AppointmentSerializier,
        ('PUT', 'PATCH'): AppointmentCreateSerializer
    }

    permission_classes = [IsAuthenticated, PatientChecker, IsOwner]
