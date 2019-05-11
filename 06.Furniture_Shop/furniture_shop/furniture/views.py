from django.shortcuts import render, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Furniture
from accounts.models import Profile
from .forms import CreateFurnitureForm
from reviews.models import Review


def has_user_access_to_modify(current_user, current_obj):
    if current_user.is_superuser or current_user.id == current_obj.user.id:
        return True
    return False


class FurnitureList(generic.ListView):
    model = Furniture
    template_name = 'furniture_list.html'
    context_object_name = 'furniture'


class UserFurnitureList(LoginRequiredMixin, generic.ListView):
    model = Furniture
    template_name = 'furniture_list.html'
    context_object_name = 'furniture'

    def get_queryset(self):
        furniture = Furniture.objects.all().filter(
                        user_id=self.request.user.pk)

        return furniture


class FurnitureCreate(LoginRequiredMixin, generic.CreateView):
    template_name = 'furniture_create.html'
    form_class = CreateFurnitureForm
    success_url = '/furniture/'

    def form_valid(self, form):
        form.instance.user = Profile.objects.get(user__pk=self.request.user.id)
        return super().form_valid(form)


class FurnitureDetail(LoginRequiredMixin, generic.DetailView):
    model = Furniture
    template_name = 'furniture_detail.html'
    context_object_name = 'furniture'

    def get_context_data(self, *, object_list=None, **kwargs):
        # import pdb; pdb.set_trace()
        context = super(FurnitureDetail, self).get_context_data(**kwargs)
        context['reviews'] = Review.objects.all().filter(
                                furniture=self.get_object())

        current_user = self.request.user
        if has_user_access_to_modify(current_user, self.get_object()):
            context['is_users_furniture'] = True
        else:
            context['is_users_furniture'] = False
        return context


class FurnitureEdit(LoginRequiredMixin, generic.UpdateView):
    model = Furniture
    template_name = 'furniture_create.html'
    form_class = CreateFurnitureForm
    success_url = '/furniture/'

    def form_valid(self, form):
        form.instance.user = Profile.objects.get(user__pk=self.request.user.id)
        return super().form_valid(form)


class FurnitureDelete(LoginRequiredMixin, generic.DeleteView):
    model = Furniture
    template_name = 'furniture_delete.html'
    context_object_name = 'furniture'
    success_url = '/furniture/'

    def get(self, request, pk):
        if has_user_access_to_modify(request.user, self.get_object()):
            return render(request, 'furniture_delete.html',
                          {'furniture': self.get_object()})
        return render(request, 'permission_denied.html')

    def post(self, request, pk):
        if has_user_access_to_modify(request.user, self.get_object()):
            furniture = self.get_object()
            furniture.delete()
            return HttpResponseRedirect('/furniture/')
        return render(request, 'permission_denied.html')
