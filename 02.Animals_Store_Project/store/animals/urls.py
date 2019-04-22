from django.urls import path, re_path
from . import views


app_name = 'animals'


urlpatterns = [
    path('all/', views.AnimalList.as_view(), name='all'),
    re_path('^create/$', views.AnimalCreate.as_view(), name='create'),
    re_path('^details/(?P<pk>[-\w]+)/$', views.AnimalDetails.as_view(),
            name='details'),
    re_path('^edit/(?P<pk>[-\w]+)/$', views.AnimalUpdate.as_view(),
            name='edit'),
    re_path('delete/(?P<pk>\d+)/$', views.AnimalDelete.as_view(),
            name='delete'),
    path('dogs/', views.DogList.as_view(), name='dogs'),
    path('cats/', views.CatList.as_view(), name='cats')

    # path('all/ordered/', views.order_animals, name='all_ordered')
]
