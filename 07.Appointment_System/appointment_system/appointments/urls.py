from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.AppointmentList.as_view(),
         name='appointment-list'),
    re_path('(?P<pk>\d+)/', views.AppointmentDetail.as_view(),
            name='appointment-detail')
]
