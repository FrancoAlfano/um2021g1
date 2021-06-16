from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Perfil, Mensajes, Agregar_Seguidor

class SignUpForm(UserCreationForm):
    nombre = forms.CharField(max_length=140, required=True)
    apellido = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'nombre',
            'apellido',
            'password1',
            'password2',
        )

class MensajesForm(forms.ModelForm):
    class Meta:
        model=Mensajes
        fields=['mensaje','etiqueta']

class Agregar_SeguidorForm(forms.ModelForm):
    class Meta:
        model=Agregar_Seguidor
        fields=['usuario','seguidor']

class PerfilForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Perfil
        fields=['nombre','apellido','email','descripcion','telefono','cargo','imagen']