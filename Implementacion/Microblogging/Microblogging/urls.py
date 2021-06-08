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
from MB.views import SignUpView, BienvenidaView, SignInView, SignOutView,Prueba, tablón_anuncios
from django.contrib.auth.decorators import login_required
#from MB import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BienvenidaView.as_view(), name='bienvenida'),
    path('registrate/', SignUpView.as_view(), name='sign_up'),
    path('incia-sesion/', SignInView.as_view(), name='sign_in'),
    path('cerrar-sesion/', SignOutView.as_view(), name='sign_out'),
    path('prueba/',login_required(Prueba.as_view()), name='bienvenida'),
    path('anuncios/',login_required(tablón_anuncios), name='tablón')
]
