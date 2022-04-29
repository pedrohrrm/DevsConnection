from django.db import reset_queries
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def  orcamento(request):
    pass

def  projetos(request):
    pass

def sobre(request):
    pass