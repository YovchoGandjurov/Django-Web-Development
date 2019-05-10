from django.urls import path, re_path, include

from . import views


urlpatterns = [
    path('profile/', views.redirect_user, name='redirect-user'),
    re_path('^profile/(?P<pk>\d+)/$', views.UserProfile.as_view(),
            name='user-profile'),
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup')
]
