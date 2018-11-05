from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
	url(r'^registro$',views.registro, name="registro"),
	url('index',views.index, name="index"),
	url('inicio',views.inicio, name="inicio"), 
	url('clientes',views.clientes, name="clientes"), 
	url('rescatados',views.listar_rescatados, name="rescatados"), 
	url('rescatar',views.agregar_rescatado, name="agregar_rescatado"), 
	url(r'^actualizar/(?P<codigo>\d+)/$',views.modificar_rescatado, name="modificar_rescatado"),	
	url(r'^eliminar/(?P<codigo>\d+)/$',views.eliminar_rescatado, name="eliminar_rescatado"),
	url(r'^$',views.inicio, name="inicio"),
	url('^', include('django.contrib.auth.urls')), #necesario para el password reset
	#url(r'^accounts/login/$',views.ingresar,name="login"), #redireccion apropiada, django por defecto te envia a esa url, mat:de donde te envia a usa url?
	url(r'^login$',views.ingresar,name="login"),
	url(r'^salir$',views.salir,name="salir"),
	url(r'^adoptar/(?P<codigo>\d+)/$',views.adoptar,name="adoptar"),
	url(r'adopcion_exitosa',views.adopcion_exitosa,name="adopcion_exitosa"),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



