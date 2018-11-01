from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div
from .models import Cliente
from django.contrib.auth.models import User

class FormRegistroCliente(forms.Form):

    run=forms.CharField(widget=forms.TextInput(),label="RUN")
    nombre=forms.CharField(widget=forms.TextInput(),label="Nombre Usuario")
    apellido=forms.CharField(widget=forms.TextInput(),label="Apellido")
    mail=forms.EmailField(widget=forms.TextInput(),label="Correo Electronico")
    telefono=forms.CharField(widget=forms.TextInput(),label="Telefono")
    username=forms.CharField(widget=forms.TextInput(),label="Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
    password2=forms.CharField(widget=forms.PasswordInput(),label="Confirmar Contraseña")


    def __init__(self, *args, submit_title="Enviar", **kwargs):
        super().__init__(*args, **kwargs)

        self.helper=FormHelper()
        self.fields['password'].help_text = "La contraseña debe contener mínimo 4 caracteres."
        self.helper.layout = Layout(
            Div(
                Div('run', css_class="col-sm-6"),
                Div('mail', css_class="col-sm-6"),
                css_class = 'row'
            ),
            Div(
                Div('nombre', css_class="col-sm-6"),
                Div('apellido', css_class="col-sm-6"),
                css_class = 'row'
            ),
            Div(
                Div('username', css_class="col-sm-6"),
                Div('telefono', css_class="col-sm-6"),
                css_class = 'row'
            ),
            Div(
                Div('password', css_class="col-sm-6"),
                Div('password2', css_class="col-sm-6"),
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