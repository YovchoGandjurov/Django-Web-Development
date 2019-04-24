from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path('^question/$', views.QuestionList.as_view(), name='questions'),
    re_path('^question/(?P<question_id>\d+)/$', views.QuestionDetail.as_view(), name='detail'),
]