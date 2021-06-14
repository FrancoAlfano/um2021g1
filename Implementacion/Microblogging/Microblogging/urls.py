"""Microblogging URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MB.views import SignUpView, BienvenidaView, SignInView, SignOutView, tablón_anuncios, publicar_mensaje_tablón, republicar_mensaje_tablón, eliminar_mensaje_tablón, consultar_siguiendo,eliminar_siguiendo,listar_usuarios,añadir_seguido,perfil_usuario,editar_perfil
from django.contrib.auth.decorators import login_required
#from MB import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', BienvenidaView.as_view(), name='bienvenida'),
    path('',tablón_anuncios, name='tablón'),
    path('registrate/', SignUpView.as_view(), name='sign_up'),
    path('incia-sesion/', SignInView.as_view(), name='sign_in'),
    path('cerrar-sesion/', SignOutView.as_view(), name='sign_out'),
    path('MensajeTablón/', login_required(publicar_mensaje_tablón), name='NuevoMensaje'),
    path('republicar/<int:id_mensaje>', login_required(republicar_mensaje_tablón), name='NuevoMensajeEditar'),
    path('eliminar/<int:id_mensaje>', login_required(eliminar_mensaje_tablón), name='NuevoMensajeEliminar'),
    path('siguiendo/', login_required(consultar_siguiendo), name='ConsultarSiguiendo'),
    path('siguiendo/eliminar/<int:id_siguiendo>', login_required(eliminar_siguiendo), name='SiguiendoEliminar'),
    path('siguiendo/añadir/', login_required(listar_usuarios), name='ListarUsuarios'),
    path('siguiendo/añadir/seguir/<int:id_siguido>', login_required(añadir_seguido), name='SeguirUsuarios'),
    path('perfil/', login_required(perfil_usuario), name='PerfilUsuario'),
    path('perfil/editar', login_required(editar_perfil), name='EditarPerfil'),
]
