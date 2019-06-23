import datetime

from django.http import HttpResponse
from django.shortcuts import render


def verifica_hora(request):
    context = {
        "hora": datetime.datetime.now(),
        "test": 10,
    }
    return render(request, 'hora.html', context)

def verifica_hora2(request):
    return HttpResponse('hora 2 não esta disponivel')