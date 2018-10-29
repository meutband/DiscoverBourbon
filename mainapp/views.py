from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def facts(request):
    return render(request, 'facts.html')


def contact(request):
    return render(request, 'contact.html')