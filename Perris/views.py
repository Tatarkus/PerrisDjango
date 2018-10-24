from django.shortcuts import render, render_to_response
from .models import Cliente, Mascota,Adopcion
from django.template import loader,RequestContext
from django.http import HttpResponse
from .forms import FormRegistroCliente, Login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import CreateView
# Create your views here.

class ClienteCreateView(CreateView):
    model = Cliente
    campos = ('run','nombre','apellido','telefono')

def ingresar(request):
    form=Login(request.POST)
    active_tab = 'tab5'
    if form.is_valid():
        data=form.cleaned_data
        user=authenticate(username=data.get("username"),password=data.get("password"))
        if user is not None:
            login(request,user)
            return redirect('gestionarUsuarios')
    return render(request,"login.html",{'form':form,'active_tab':active_tab})

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

def bienvenido(request):  
    plantilla=loader.get_template("index.html")
    return render(request,"bienvenido.html")

def registrar(request):    
    return render(request,"registro.html")

def registro(request):    
    active_tab = 'tab6'
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FormRegistroCliente(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FormRegistroCliente()
    return render(request, 'registro.html', {'form': form,'active_tab':active_tab})

def index(request):
    active_tab = 'tab1'
    return render(request,"index.html", {'active_tab':active_tab})
	
def inicio(request):
    active_tab = 'tab1'
    return render(request,"inicio.html", {'active_tab':active_tab})
