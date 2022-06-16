from django.shortcuts import render
from django.http import HttpResponse
from .models import FeriadoModel
from .models import FeriadoModelApi
from datetime import date
from .FeriadosAPI import FeriadosAPI

def cadastro_feriados(request):
   if request.method == 'GET':
        return render(request, 'cadastro.html')

def index(request):

    hoje = date.today()

    if FeriadoModel.objects.filter(ano=hoje.year, mes=hoje.month, dia=hoje.day).exists():
        response = {
            'isFeriado': True,
        }
    else:
        response = {
            'isFeriado': False,
        }
    return render(request, 'index.html', response)

def cadastra_feriados_api(request):
    api = FeriadosAPI(2022)

    for feriado in api.feriados:
        nome, data = feriado
        cadastro = FeriadoModelApi(nome=nome, data=data)
        cadastro.save()

    return HttpResponse('')
