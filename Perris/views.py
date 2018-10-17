from django.shortcuts import render, render_to_response
from .models import Cliente, Mascota,Adopcion
from django.template import loader,RequestContext
from django.http import HttpResponse
from .forms import FormCliente, Login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def ingresar(request):
    form=Login(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        user=authenticate(username=data.get("username"),password=data.get("password"))
        if user is not None:
            login(request,user)
            return redirect('gestionarUsuarios')
    return render(request,"login.html",{'form':form,})

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
