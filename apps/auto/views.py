from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.auto.models import Auto
from apps.auto.forms import AutoForm


# Create your views here.

def index(request):
    return render(request, 'auto/index.html')

def quienesSomos(request):
    return render(request, 'auto/quienesSomos.html')

def contacto(request):
    return render(request, 'auto/contacto.html')

def auto_view(request):
    if request.method == 'POST':
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(auto_listar)
    else:
        form = AutoForm()

    return render(request, 'auto/auto_form.html', {'form':form}) 

def auto_listar(request):
    auto = Auto.objects.all().order_by('id')
    contexto = {'autos':auto}
    return render(request, 'auto/auto_list.html', contexto)

def auto_editar(request, id_auto):
    auto = Auto.objects.get(id=id_auto)
    if request.method == 'GET':
        form = AutoForm(instance=auto)
    else:
        form = AutoForm(request.POST, instance=auto)
        if form.is_valid():
            form.save()
        return redirect(auto_listar) 
    return render(request, 'auto/auto_form.html', {'form':form})     

def auto_eliminar(request, id_auto):
    auto = Auto.objects.get(id=id_auto)
    if request.method =='POST':
        auto.delete()
        return redirect(auto_listar)
    return render(request, 'auto/auto_delete.html', {'auto':auto})    
         