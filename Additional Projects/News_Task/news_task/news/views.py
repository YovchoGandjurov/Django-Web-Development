from django.shortcuts import render
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import News
from .serializers import NewsSerializer


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    ordering_fields = ('date', 'title')
    filterset_fields = ('date', 'title')

    # Overriding the queryset
    #
    # def get_queryset(self):
    #     date_query = self.request.query_params.get('date', None)
    #     title_query = self.request.query_params.get('title', None)
    #     print(self.request.query_params)
    #     if date_query is not None and title_query is not None:
    #         queryset = News.objects.all().filter(date=date_query,
    #                                              title=title_query)
    #     elif date_query is not None:
    #         queryset = News.objects.all().filter(date=date_query)
    #     elif title_query is not None:
    #         queryset = News.objects.all().filter(title=title_query)
    #     else:
    #         queryset = News.objects.all()
    #     return queryset
