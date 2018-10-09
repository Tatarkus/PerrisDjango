from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^cliente$',views.cliente, name="clientes"),
    url(r'^mascota$',views.mascota, name="mascotas"),    
    url(r'^adopcion$',views.adopcion, name="adopcion"),   
    url(r'^$',views.cliente, name="clientes"),  

]