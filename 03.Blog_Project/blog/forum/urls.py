from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path('^question/$', views.QuestionList.as_view(), name='questions'),
    re_path('^question/(?P<question_id>\d+)/$', views.QuestionDetail.as_view(),
            name='question_detail'),
    # re_path('^question/(?P<question_id>\d+)/answers/$', views.PLACEHOLDER.as_view(),
    #         name='answers'),
    # re_path('^question/(?P<question_id>\d+)/answers/(?P<question_id>\d+)/$', views.PLACEHOLDER.as_view(),
    #         name='answers_detail'),
]