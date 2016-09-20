from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reception(request):
    return render(request, 'reception.html')


def music(request):
    return render(request, 'music.html')
