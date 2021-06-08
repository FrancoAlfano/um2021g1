from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from .models import Perfil, Mensajes
from .forms import SignUpForm
from django.contrib.auth.views import LoginView, LogoutView 


class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpForm

    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')

class BienvenidaView(TemplateView):
   template_name = 'MB/bienvenida.html'

class SignInView(LoginView):
    template_name = 'iniciar_sesion.html'

class SignOutView(LogoutView):
    pass

class Prueba(TemplateView):
    template_name = 'MB/prueba.html'

    #TODO:encontrar la manera de redirigir la pagina que no esta autenticada
    # def get(self, request, *args, **kwargs):
    #     username = request.POST['username']
    #     password = request.POST['password1']
    #     usuario = authenticate(request, username=username, password=password)
    #     login(request, user)
    #     if usuario is not None:
    #         pass
    #     else:
    #         print("no paso")

def tablón_anuncios(request):
    mensajes=Mensajes.objects.all()
    contexto={'mensajes':mensajes}
    return render(request, 'MB/tablon_anuncios.html',contexto)