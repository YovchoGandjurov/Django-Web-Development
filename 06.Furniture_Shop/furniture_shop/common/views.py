from django.shortcuts import render


def landing(request):
    return render(request, 'landing_page.html')
