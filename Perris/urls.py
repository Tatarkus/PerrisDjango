from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^clientes$',views.cliente, name="clientes"),
    url(r'^mascota$',views.mascota, name="mascotas"),    
    url(r'^adopcion$',views.adopcion, name="adopcion"),   
    url('',views.index, name="index"),  

]