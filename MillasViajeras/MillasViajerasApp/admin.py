from django.contrib import admin

from .models import *

# Register your models here.

class PublicacionesAdmin(admin.ModelAdmin):
    list_display = ('pais', 'titulo', 'descripcion', "fecha_viaje")
        

admin.site.register(Publicaciones, PublicacionesAdmin)
admin.site.register(Avatar)
admin.site.register(Comentario)