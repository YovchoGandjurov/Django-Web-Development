from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Animal
from django.core.serializers import serialize
import json
from .forms import AnimalForm
from django.contrib import messages
from django.views.generic import ListView, CreateView, DetailView, \
    UpdateView, DeleteView # , BlogListView
from django.db.models import Q


# replaced with form and CreateView
def create_animal(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    kind = request.GET.get('kind')
    image_url = request.GET.get('image_url')
    description = request.GET.get('description')
    breed = request.GET.get('breed')

    animal = Animal(name=name, age=age, kind=kind, image_url=image_url,
                    description=description, breed=breed)
    animal.save()
    return HttpResponse('created')


# replaced with UpdateView
def edit_animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    name = request.GET.get('name')
    animal.name = name
    animal.save()
    return HttpResponse('edited')


# replaced with DeleteView
def delete_animal(request, animal_id):
    Animal.objects.get(pk=animal_id).delete()
    return HttpResponse('deleted')


def serialized_data(data):
    try:
        return serialize('json', data)
    except:
        return serialize('json', [data])


# replaced with ListView
def get_all_animals(request):
    name = request.GET.get('name')
    if name:
        animal = Animal.objects.all().filter(name=name)
        return HttpResponse(serialized_data(animal))

    animals = Animal.objects.all()
    return HttpResponse(serialized_data(animals))


# replaced with ListView
def get_animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    return HttpResponse(serialized_data(animal))


# replaced with DogView
def get_all_dogs(request):
    dogs = Animal.objects.filter(age=16, kind='D')
    return HttpResponse(serialized_data(dogs))


def order_animals(request):
    animals = Animal.objects.all().order_by('age')
    return HttpResponse(serialized_data(animals))


# replace with CreateView
def create_animal_form(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)

        if form.is_valid():
            form.save()
            animals = Animal.objects.all()
            return HttpResponseRedirect('/animals/all/')
        else:
            messages.error(request, 'Error')
            return render(request, template_name='create.html',
                          context={'form': form})
            # for field in form.errors:
            #     form[field].field.widget.attrs['class'] += \
            #                             ' alert alert-danger'
    else:
        form = AnimalForm()

    return render(request, template_name='create.html',
                  context={'form': form})


def search(request):
    query = request.GET['search']
    # t = 

# ###################################################################
# CRUD - Class Based View
# ###################################################################


class AnimalList(ListView):
    model = Animal
    context_object_name = 'animals'
    template_name = 'animal_list.html'

    def get_queryset(self):
        name = self.request.GET.get('name')

        if name is None:
            animals = Animal.objects.all()
        else:
            animals = Animal.objects.filter(name=name)
        return animals


class DogList(ListView):
    model = Animal
    context_object_name = 'animals'
    template_name = 'animal_list.html'

    def get_queryset(self):
        animals = Animal.objects.filter(kind='D')
        return animals


class CatList(ListView):
    model = Animal
    context_object_name = 'animals'
    template_name = 'animal_list.html'

    def get_queryset(self):
        animals = Animal.objects.filter(kind='C')
        return animals


class AnimalCreate(CreateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'create.html'
    success_url = '/animals/all/'


class AnimalDetails(DetailView):
    model = Animal
    template_name = 'animal_details.html'
    context_object_name = 'animal'


class AnimalUpdate(UpdateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'create.html'
    success_url = '/animals/all/'


class AnimalDelete(DeleteView):
    model = Animal
    template_name = 'animal_delete.html'
    success_url = '/animals/all/'
