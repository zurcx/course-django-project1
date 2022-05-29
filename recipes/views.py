from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={
        'nome': 'Luiz Cruz'
    })


def contato(request):
    return HttpResponse('CONTATO da View')


def sobre(request):
    return HttpResponse('SOBRE da View')
