from django.shortcuts import render, render_to_response
from .models import Cliente, Mascota,Adopcion
from django.template import loader,RequestContext
from django.http import HttpResponse


# Create your views here.

def cliente(request):
    clientes=Cliente.objects.all()
    plantilla=loader.get_template("cliente.html")
    contexto={
        'clientes:':clientes,
    }
    return HttpResponse(plantilla.render(contexto,request))

def mascota(request):
    mascotas=Mascota.objects.all()
    plantilla=loader.get_template("mascota.html")
    contexto={
        'mascotas:':Mascota.objects.all(),
    }
    return HttpResponse(plantilla.render(contexto,request))

def adopcion(request):  

    plantilla=loader.get_template("mascota.html")
    contexto={
        'adopciones:':Adopcion.objects.all(),
    }
    return HttpResponse(plantilla.render(contexto,request))
