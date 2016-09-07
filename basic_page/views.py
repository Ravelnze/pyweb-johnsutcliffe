from django.shortcuts import render
from models import SiteContent


def load_home(request):
    query_set = SiteContent.objects.filter(page_name='').order_by('title')
    context = {'content': query_set}

    return render(request, 'home.html', context)


def load_reception(request):
    query_set = SiteContent.objects.filter(page_name='reception').order_by('title')
    context = {'content': query_set}

    return render(request, 'reception.html', context)

