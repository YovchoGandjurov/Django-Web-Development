from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.views import generic


def redirect_to_user_profile(request):
    url = f'{request.user.pk}/'
    return HttpResponseRedirect(redirect_to=url)


class UserProfileDetail(generic.DetailView):
    model = User
    template_name = 'user_profile.html'
    context_object_name = 'user'


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/accounts/login/'
    template_name = 'signup.html'
