from django.shortcuts import render
from django.views import generic

from .models import Furniture


class FurnitureList(generic.ListView):
    model = Furniture
    template_name = 'furniture_list.html'
    context_object_name = 'furniture'
