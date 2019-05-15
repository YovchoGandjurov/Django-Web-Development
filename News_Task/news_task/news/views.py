from django.shortcuts import render
from rest_framework import generics

from .models import News
from .serializers import NewsSerializer


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
