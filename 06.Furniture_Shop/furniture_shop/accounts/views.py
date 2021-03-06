from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


def redirect_user(request):
    url = f'/furniture/'
    return HttpResponseRedirect(url)


class UserProfile(generic.DetailView):
    model = Profile
    template_name = 'user_profile.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super(UserProfile, self).get_context_data(**kwargs)
        context['profile_id'] = pk
        print(context['profile_id'], '*'*100)
        return context


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/accounts/login/'
    template_name = 'signup.html'
