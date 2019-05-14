from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('doctors/', views.DoctorList.as_view(), name='doctor-list'),
    re_path('^doctors/(?P<pk>\d+)/$', views.DoctorDetail.as_view(),
            name='doctor-detail'),
]
