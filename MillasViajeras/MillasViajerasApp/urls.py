from django.urls import path

from .views import *

urlpatterns = [
    
    path('', inicio, name='inicio'),
    path('publicaciones', publicaciones, name='publicaciones'),
    path('publicaciones/<pk>', ver_publicacion.as_view(), name='ver_publicacion'),
    path('registro', registro, name='registro'),
    path('login', login_request, name='login'),
    path('logout', logout_request, name='logout'),
    path('editarperfil', editar_perfil, name='editar_perfil'),  
    path('editarperfil/agregar_avatar', agregar_avatar, name='agregar_avatar'),  
    path('crearpublicacion', crear_publicacion, name='crear_publicacion'),
    path('editar_publicacion/<publicacion_id>', editar_publicacion, name='editar_publicacion'),
    path('eliminar_publicacion/<publicacion_id>', eliminar_publicacion, name='eliminar_publicacion'),
    path('mis_publicaciones', mis_publicaciones, name='mis_publicaciones'),
    path('about', about, name='about'),        
]