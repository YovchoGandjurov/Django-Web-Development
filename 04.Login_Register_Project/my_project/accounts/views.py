from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views import generic


def redirect_to_user_profile(request):
    url = f'{request.user.pk}/'
    return HttpResponseRedirect(redirect_to=url)


def logged_out(request):
    auth.logout(request)
    return render(request, 'logout.html')


class LogoutView(generic.TemplateView):
    template_name = 'logout.html'


class UserProfileDetail(generic.DetailView):
    model = User
    template_name = 'user_profile.html'
    context_object_name = 'user'
