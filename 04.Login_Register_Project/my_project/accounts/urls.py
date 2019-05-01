from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    re_path('logout/', views.LogoutView.as_view(),
            name='logout'),
    path('', include('django.contrib.auth.urls')),
    re_path('^profile/$', views.redirect_to_user_profile,
            name="redirect-user-detail"),
    re_path('^profile/(?P<pk>\d+)/$', views.UserProfileDetail.as_view(),
            name='user-detail'),
]
