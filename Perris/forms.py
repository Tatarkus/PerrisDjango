from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div
from .models import Cliente
from django.contrib.auth.models import User

class FormRegistroCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        # specify what fields should be used in this form.
        fields = ('run',
                  'nombre', 'apellido','email',
                  'telefono',
                 )

    def __init__(self, *args, submit_title="Enviar", **kwargs):
        super().__init__(*args, **kwargs)
        my_field_text= [
            # (field_name, Field title label, Detailed field description)
            ('run', 'run', 'run de cliente'),
            ('nombre', 'nombre', 'nombre cliente'),
            ('apellido', 'apellido', 'apellido clienjte'),
            ('telefono', '', ''),
            
         ]  
    # Set layout for fields.
        self.helper=FormHelper()
        self.helper.layout = Layout(
            Div('run', 'nombre'),
            Div(
                Div('apellido', css_class="col-sm-2"),
                Div('telefono', css_class="col-sm-10"),
                css_class = 'row'
            )
        )           
        self.helper.add_input(Submit('POST', submit_title))

class FormRegistroUsuario(forms.ModelForm):
    class Meta:
        model = User
        # specify what fields should be used in this form.
        fields = ('email',
                  'username', 'password',
                 )

    def __init__(self, *args, submit_title="Enviar", **kwargs):
        super().__init__(*args, **kwargs)
    # Set layout for fields.
        self.helper=FormHelper()
        self.fields['username'].help_text = None



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