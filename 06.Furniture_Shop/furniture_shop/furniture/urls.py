from django.urls import path, re_path, include

from . import views


urlpatterns = [
    path('', views.FurnitureList.as_view(), name='furniture'),
    path('mine/', views.UserFurnitureList.as_view(), name='user-furniture'),
    path('create/', views.FurnitureCreate.as_view(), name='furniture-create'),
    re_path('^details/(?P<pk>\d+)/$', views.FurnitureDetail.as_view(),
            name="furniture-detail"),
    re_path('^edit/(?P<pk>\d+)/$', views.FurnitureEdit.as_view(),
            name='furniture-edit'),
    re_path('^delete/(?P<pk>\d+)/$', views.FurnitureDelete.as_view(),
            name='furniture-delete'),
    re_path('^material/$', views.CreateMaterial.as_view(),
            name='material-add'),
]
