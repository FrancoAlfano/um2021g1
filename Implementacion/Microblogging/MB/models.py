from django.db import models
#from .forms import SignUpForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime, timedelta

seleccion_estado_etiqueta=[(1,'trabajo'),(2,'cuentas'),(3,'facturas')]

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True)
    web = models.URLField(blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=100, blank=True)

    # Python 3
    def __str__(self): 
        return self.usuario.username

@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfil.save()

class Mensajes(models.Model):
    usuario=models.ForeignKey(Perfil, null=True, on_delete=models.CASCADE)
    fecha=models.DateField(default=datetime.now())
    mensaje=models.CharField(max_length=140)
    etiqueta=models.IntegerField(null=False,blank=True,choices=seleccion_estado_etiqueta)

class Agregar_Seguidor(models.Model):
    usuario=models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='usuarios')
    seguidor=models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='seguidores')
