from django.contrib import admin
from .models import Perfil, Mensajes

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'bio', 'web')

class MensajesAdmin(admin.ModelAdmin):
    list_display=('usuario','fecha','mensaje','etiqueta')

admin.site.register(Mensajes,MensajesAdmin)
