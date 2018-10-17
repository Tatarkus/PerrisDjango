from django import forms

class FormCliente(forms.Form):
	run=forms.CharField(widget=forms.TextInput(),label="RUN",required=True)
	nombre=forms.CharField(widget=forms.TextInput(),required=True)
	apellido=forms.CharField(widget=forms.TextInput(),required=True)
	usuario=forms.CharField(widget=forms.TextInput(),required=True)
	password=forms.CharField(widget=forms.PasswordInput(),required=True)

class FormMascota(forms.Form):
	codigo=forms.CharField(widget=forms.TextInput(),required=True)
	nombre=forms.CharField(widget=forms.TextInput(),required=True)
	color=forms.CharField(widget=forms.TextInput(),required=True)

class FormAdopcion(forms.Form):
	run=forms.CharField(widget=forms.TextInput(),required=True)
	codigo=forms.CharField(widget=forms.TextInput(),required=True)

class Login(forms.Form):
	username=forms.CharField(widget=forms.TextInput(),label="Nombre Usuario")
	password=forms.CharField(widget=forms.PasswordInput(),label="contraseña")