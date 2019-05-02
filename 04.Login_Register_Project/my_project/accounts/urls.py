from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    re_path('logout/', TemplateView.as_view(template_name='logout.html'),
            name='logout'),
    re_path('^profile/$', views.redirect_to_user_profile,
            name="redirect-user-detail"),
    re_path('^profile/(?P<pk>\d+)/$', views.UserProfileDetail.as_view(),
            name='user-detail'),
    path('signup/', views.SignUp.as_view(), name='signup'),

    path('', include('django.contrib.auth.urls')),
]
