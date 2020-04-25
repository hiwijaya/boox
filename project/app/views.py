from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def signin(request):
    context = {
        'flag': 'SIGNIN'
    }
    return render(request, 'auth.html', context)


def signup(request):
    context = {
        'flag': 'SIGNUP',
    }
    return render(request, 'auth.html', context)
