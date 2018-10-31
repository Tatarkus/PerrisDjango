from django.shortcuts import render, render_to_response
from .models import Cliente, Mascota,Adopcion
from django.template import loader,RequestContext
from django.http import HttpResponse
from .forms import FormRegistroCliente, Login, FormRegistroUsuario
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
            return render(request,"login.html",{'form':form,'active_tab':active_tab})
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

def clientes(request):  
    lista = Clientes.objects.all()
    return render(request, 'clientes.html', {'lista':lista})


def registro(request):    
    active_tab = 'tab6'
    print("REQUEST")
    if request.method == 'POST':
        print("POST")
        # create a form instance and populate it with data from the request:
        form = FormRegistroCliente(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print("FORMA VALIDA")
            data=form.cleaned_data
            regDB=User.objects.create_user(data.get("run"),data.get("email"),data.get("password"))
            cliente=Cliente(user=regDB,nombre=data.get("nombre"),apellido=data.get("apellido"),email=data.get("email"),telefono=data.get("telefono"))
            regDB.save()
            cliente.save()
            lista = Clientes.objects.all()
            active_tab = 'tab1'
            return render(request, 'clientes.html', {'lista':lista,'active_tab':active_tab})
    # if a GET (or any other method) we'll create a blank form
    else:
        formUsr = FormRegistroUsuario()
        print("NO ES POST")
        form = FormRegistroCliente()
    return render(request, 'registro.html', {'form': form,'active_tab':active_tab,'form2':formUsr})

def index(request):
    active_tab = 'tab1'
    return render(request,"index.html", {'active_tab':active_tab})
	
def inicio(request):
    active_tab = 'tab1'
    return render(request,"inicio.html", {'active_tab':active_tab})
