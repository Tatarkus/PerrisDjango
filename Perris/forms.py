from django import forms

class FormCliente(forms.Form):
    run=forms.CharField(widget=forms.TextInput(),required=True)
    nombre=forms.CharField(widget=forms.TextInput(),required=True)
    apellido=forms.CharField(widget=forms.TextInput(),required=True)
    telefono=forms.CharField(widget=forms.NumberInput(),required=True)

class FormMascota(forms.Form):
    codigo=forms.CharField(widget=forms.TextInput(),required=True)
    nombre=forms.CharField(widget=forms.TextInput(),required=True)
    color=forms.CharField(widget=forms.TextInput(),required=True)

class FormAdopcion(forms.Form):
    run=forms.CharField(widget=forms.TextInput(),required=True)
    codigo=forms.CharField(widget=forms.TextInput(),required=True)