from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Perfil, Mensajes, Agregar_Seguidor

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
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
        fields=['first_name','last_name','email','descripcion']