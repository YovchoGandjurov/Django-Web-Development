from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.BookView.as_view(), name="books"),
    re_path('^(?P<pk>\d+)/$', views.BookDetail.as_view(), name="book-detail"),
]
