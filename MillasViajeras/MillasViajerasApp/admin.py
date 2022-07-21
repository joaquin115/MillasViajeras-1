from django.contrib import admin

from .models import *

# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'apellido', 'fecha')

class PublicacionesAdmin(admin.ModelAdmin):
    list_display = ('pais', 'titulo', 'descripcion', "fecha_viaje")
        

admin.site.register(Persona, PersonaAdmin)
admin.site.register(Publicaciones, PublicacionesAdmin)
admin.site.register(Avatar)