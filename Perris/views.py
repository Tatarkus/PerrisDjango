from django.shortcuts import render, render_to_response
from .models import Cliente, Mascota,Adopcion
from django.template import loader,RequestContext
from django.http import HttpResponse
from .forms import FormCliente

# Create your views here.

#def cliente(request):
 #   clientes=Cliente.objects.all()
  #  plantilla=loader.get_template("cliente.html")
   # contexto={
    #    'clientes:':clientes,
    #}
   # return HttpResponse(plantilla.render(contexto,request))

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

def cliente(request):    
    form=FormCliente(request.POST)
    if form.is_valid():
        data=form.cleaned_data #crea lista con todos los datos
        regDB=Cliente(run=data.get("run"),nombre=data.get("nombre"),apellido=data.get("apellido"),telefono=data.get("telefono"))
        regDB.save()
    form=FormCliente
    clientes=Cliente.objects.all()
   
    return render(request,"cliente.html",{'clientes':clientes,'form':form},)

def index(request):
    return render(request,"index.html")
