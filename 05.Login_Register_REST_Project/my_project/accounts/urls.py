from django.urls import path, re_path, include
from . import views


urlpatterns = [
    path('rest_auth/', include('rest_auth.urls')),
    path('register/', views.UserCreate.as_view(), name='register')
]
