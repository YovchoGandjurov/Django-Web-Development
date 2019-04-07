from django.urls import path
from . import views


urlpatterns = [
    path('all/', views.get_all_animals, name='all'),
    path('all/<int:animal_id>/', views.get_animal, name="animal"),
    path('all/dogs/', views.get_all_dogs, name='dogs')
]
