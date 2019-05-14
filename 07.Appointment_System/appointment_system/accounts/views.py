from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Doctor
from .serializers import DoctorSerializer
from .permissions import DoctorPermission, IsOwnerOrReadOnly


class DoctorList(generics.ListCreateAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated, DoctorPermission]

    def get_queryset(self):
        specialty = self.request.query_params.get('specialty', None)
        if specialty is not None:
            queryset = Doctor.objects.all().filter(specialty=specialty)
            return queryset
        return Doctor.objects.all()


class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated, DoctorPermission, IsOwnerOrReadOnly]
