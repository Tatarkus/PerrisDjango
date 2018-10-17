from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^registro$',views.registro, name="registro"),
    url(r'^registrar$',views.registrar, name="registrar"),
    url(r'^bienvenido$',views.bienvenido, name="bienvenido"),
    url(r'^login$',views.ingresar, name="login"),
    url(r'^mascota$',views.mascota, name="mascotas"),    
    url(r'^adopcion$',views.adopcion, name="adopcion"),   
    url('index',views.index, name="index"), 

]