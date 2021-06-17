from django.contrib import admin
from .models import Perfil, Mensajes, Agregar_Seguidor

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario','nombre','apellido','email')

class MensajesAdmin(admin.ModelAdmin):
    list_display=('usuario','fecha','mensaje','etiqueta')

class Agregar_SeguidorAdmin(admin.ModelAdmin):
    list_display=('usuario','seguidor')

admin.site.register(Mensajes,MensajesAdmin)
admin.site.register(Agregar_Seguidor,Agregar_SeguidorAdmin)