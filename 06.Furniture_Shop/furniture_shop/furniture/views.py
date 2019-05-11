from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Furniture
from accounts.models import Profile
from .forms import CreateFurnitureForm


class FurnitureList(generic.ListView):
    model = Furniture
    template_name = 'furniture_list.html'
    context_object_name = 'furniture'


class UserFurnitureList(LoginRequiredMixin, generic.ListView):
    model = Furniture
    template_name = 'furniture_list.html'
    context_object_name = 'furniture'

    def get_queryset(self):
        # user_profile = Profile.objects.get(
        #                   user__pk=int(self.request.user.id))
        furniture = Furniture.objects.all().filter(
                        user_id=self.request.user.pk)

        return furniture


class FurnitureCreate(LoginRequiredMixin, generic.CreateView):
    model = Furniture
    template_name = 'furniture_create.html'
    form_class = CreateFurnitureForm
    success_url = '/furniture/'

    def form_valid(self, form):
        form.instance.user = Profile.objects.get(user__pk=self.request.user.id)
        return super().form_valid(form)
