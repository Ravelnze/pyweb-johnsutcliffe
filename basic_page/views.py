from django.shortcuts import render


def load_page(request):
    return render(request, 'home.html')
