from django.urls import path, re_path, include


urlpatterns = [
    path('rest_auth/', include('rest_auth.urls')),
]