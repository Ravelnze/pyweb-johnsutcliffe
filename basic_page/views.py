from django.shortcuts import render


def load_home(request):
    return render(request, 'home.html')


def load_reception(request):
    return render(request, 'reception.html')
