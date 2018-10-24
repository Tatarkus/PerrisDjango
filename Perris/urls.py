from django.conf.urls import url, include
from . import views

urlpatterns=[
    url(r'^registro$',views.registro, name="registro"),
    url(r'^registrar$',views.registrar, name="registrar"),
    url(r'^login$',views.ingresar, name="login"),
    url(r'^mascota$',views.mascota, name="mascotas"),    
    url(r'^adopcion$',views.adopcion, name="adopcion"),   
    url('index',views.index, name="index"), 
	url('inicio',views.inicio, name="inicio"), 
	url('clientes',views.clientes, name="clientes"), 
    url('^', include('django.contrib.auth.urls')), #necesario para el password reset
    url(r'^accounts/login/$',views.index,name="inicio"), #redireccion apropiada, django por defecto te envia a esa url