from django.urls import path, re_path, include

from . import views


urlpatterns = [
    path('', views.FurnitureList.as_view(), name='furniture'),
    path('mine/', views.UserFurnitureList.as_view(), name='user-furniture'),
    path('create/', views.FurnitureCreate.as_view(), name='furniture-create')

]
