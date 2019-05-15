from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.AppointmentList.as_view(),
         name='appointment-list')
]