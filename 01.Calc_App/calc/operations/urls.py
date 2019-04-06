from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    # path(r'add/<int:arg1>/<int:arg2>/', views.add, name='add')
    re_path(r'(?P<operator>.*)/(?P<arg1>.*)/(?P<arg2>.*)/', views.calculate,
            name='calculator')
]
