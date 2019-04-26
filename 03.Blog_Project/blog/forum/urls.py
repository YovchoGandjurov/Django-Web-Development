from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path('^question/$', views.QuestionsList.as_view(), name='questions'),
    re_path('^question/(?P<question_id>\d+)/$',
            views.QuestionDetail.as_view(),
            name='question_detail'),
    re_path('^question/(?P<question_id>\d+)/answers/$',
            views.AnswersList.as_view(),
            name='answers'),
    re_path('^question/(?P<question_id>\d+)/answer/(?P<answer_id>\d+)/$',
            views.AnswerDetail.as_view(),
            name='answers_detail'),
    re_path('^users/questions/$', views.UserList.as_view(), name='users')
]