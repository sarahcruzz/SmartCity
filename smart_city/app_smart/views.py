from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def abre_index(request):
    mensagem = "Bem vindo ao Smart City"
    return HttpResponse(mensagem)