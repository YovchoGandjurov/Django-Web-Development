from django.urls import path

from . import views


urlpatterns = [
    path('', views.NewsList.as_view(), name='news-list')
]
