from django.shortcuts import render
from models import SiteContent


def load_home(request):
    context = {'content': SiteContent.objects.filter(page_name='')}
    return render(request, 'home.html', context)


def load_reception(request):
    context = {'content': SiteContent.objects.filter(page_name='reception')}
    return render(request, 'reception.html', context)

