from django.urls import path, re_path, include

from . import views


urlpatterns = [
    path('', views.FurnitureList.as_view(), name='furniture'),
]
