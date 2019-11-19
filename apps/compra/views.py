from django.shortcuts import render
from django.http import HttpResponse



def index_compra(request):
    return HttpResponse("soy la pagina principal de la app compra")
