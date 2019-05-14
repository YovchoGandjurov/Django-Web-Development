from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Doctor
from .serializers import DoctorSerializer
from .permissions import DoctorPermission, IsOwnerOrReadOnly


class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    permission_classes = [IsAuthenticated, DoctorPermission]


class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated, DoctorPermission, IsOwnerOrReadOnly]
