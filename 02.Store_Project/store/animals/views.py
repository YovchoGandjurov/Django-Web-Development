from django.shortcuts import render
from django.http import HttpResponse
from .models import Animal
from django.core.serializers import serialize
import json


def serialized_data(data):
    try:
        return serialize('json', data)
    except:
        return serialize('json', [data])


def get_all_animals(request):
    animals = Animal.objects.all()
    return HttpResponse(serialized_data(animals))


def get_animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    return HttpResponse(serialized_data(animal))


def get_all_dogs(request):
    dogs = Animal.objects.filter(age=16, kind='D')
    return HttpResponse(serialized_data(dogs))
