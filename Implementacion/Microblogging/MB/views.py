from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from .models import Perfil, Mensajes
from .models import Agregar_Seguidor
from .forms import SignUpForm, MensajesForm,Agregar_SeguidorForm,PerfilForm
from django.contrib.auth.views import LoginView, LogoutView 


#ENDPOINT LOGIN

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

class SignInView(LoginView):
    template_name = 'iniciar_sesion.html'

class SignOutView(LogoutView):
    pass
    
#ENDPOINT TABLÓN DE ANUNCIOS

def tablón_anuncios(request):
    mensajes=Mensajes.objects.all()
    #enviados=Mensajes.objects.filter(usuario=request.user.perfil)
    contexto={'mensajes':mensajes}
    return render(request, 'MB/bienvenida.html',contexto)

#ENDPOINT MENSAJES TABLÓN DE ANUNCIOS

def publicar_mensaje_tablón(request):
    formulario=MensajesForm(data=request.POST)
    if formulario.is_valid():
        formulario = formulario.save(commit=False)
        formulario.usuario=request.user.perfil
        formulario.save()
        formulario=MensajesForm()
    return render(request, 'MB/MensajeTabón/formulario_mensaje_tablón.html',{'form':formulario})

def republicar_mensaje_tablón(request,id_mensaje):
    mensaje=Mensajes.objects.get(id=id_mensaje)
    if request.method == 'GET':
        form=MensajesForm(instance=mensaje)
    else:
        form=MensajesForm(request.POST, instance=mensaje)
        if form.is_valid():
            form.save()
        return redirect('tablón')
    return render(request, 'MB/MensajeTabón/formulario_mensaje_tablón.html', {'form':form})

def eliminar_mensaje_tablón(request, id_mensaje):
    mensaje=Mensajes.objects.get(id=id_mensaje)
    if request.method == 'POST':
        mensaje.delete()
        return redirect('tablón')
    return render(request, 'MB/MensajeTabón/mensaje_tablón_eliminar.html', {'mensaje':mensaje})

#ENDPOINT SEGUIDORES Y SEGUIDOS

def consultar_siguiendo(request):
    siguiendo=Agregar_Seguidor.objects.filter(usuario=request.user.perfil)
    contexto={'siguiendo':siguiendo}
    return render(request, 'MB/Siguiendo/siguiendo_tablón.html',contexto)

def eliminar_siguiendo(request, id_siguiendo):
    siguiendo=Agregar_Seguidor.objects.get(id=id_siguiendo)
    if request.method == 'POST':
        siguiendo.delete()
        return redirect('ConsultarSiguiendo')
    return render(request, 'MB/Siguiendo/siguiendo_eliminar.html', {'siguiendo':siguiendo})

def listar_usuarios(request):
    usuarios=Perfil.objects.all()
    contexto={'usuarios':usuarios}
    return render(request, 'MB/Siguiendo/lista_usuarios.html',contexto)

#TODO:corregir
def añadir_seguido(request, id_seguido):
    seguidor=Agregar_SeguidorForm(data=request.POST)
    NuevoSeguidor=Agregar_Seguidor.objects.get(seguidor=id_seguido)
    if seguidor.is_valid():
        seguidor = seguidor.save(commit=False)
        seguidor.usuario=request.user.perfil
        seguidor.save()
        if request.method == 'POST':
            seguidor.seguidor.add(NuevoSeguidor)
            seguidor.save()
            return redirect('tablón')
        #formulario=MensajesForm()

#ENDPOINT PERFIL

def perfil_usuario(request):
    usuario=Perfil.objects.filter(usuario=request.user)
    contexto={'usuarios':usuario}
    return render(request, 'MB/Perfil/lista_perfil.html',contexto)

def editar_perfil(request):
    formulario=PerfilForm(data=request.POST)
    if formulario.is_valid():
        formulario = formulario.save(commit=False)
        formulario.usuario=request.user
        formulario.save()
        formulario=PerfilForm()
    return render(request, 'MB/Perfil/formulario_perfil.html',{'form':formulario})
