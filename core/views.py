import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def verifica_hora(request):
    context = {
        "hora": datetime.datetime.now(),
        "test": 10,
    }
    print("bem vindo ao verificador de hora!!")
    return render(request, 'hora.html', context)
