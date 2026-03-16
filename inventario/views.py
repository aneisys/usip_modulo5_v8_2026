from django.http import HttpResponse
from django.shortcuts import render

from .models import Categoria


def index(request):
    return HttpResponse("Hola mundo")

def contact(request, name):
    return HttpResponse(f"Hola {name} bienvenido a la clase de Django")

def categorias(request):
    categorias = Categoria.objects.all()
    
    # Filtro por nombre si se proporciona el parámetro
    nombre_filtro = request.GET.get('nombre')
    if nombre_filtro:
        categorias = categorias.filter(nombre__contains=nombre_filtro)
    
    return render(request, 'categorias.html', {
        "categorias": categorias
    })
