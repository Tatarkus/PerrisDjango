from django.conf.urls import url, include
from . import views

urlpatterns=[
	url(r'^registro$',views.registro, name="registro"),
	url(r'^login$',views.ingresar, name="login"), 
	url('index',views.index, name="index"),
	url('inicio',views.inicio, name="inicio"), 
	url('clientes',views.clientes, name="clientes"), 
    url(r'^$',views.inicio, name="inicio"),
    url('^', include('django.contrib.auth.urls')), #necesario para el password reset
    url(r'^accounts/login/$',views.index,name="inicio"), #redireccion apropiada, django por defecto te envia a esa url
]