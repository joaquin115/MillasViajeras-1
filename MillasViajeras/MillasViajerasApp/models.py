from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import *

# Create your models here.

class Publicaciones(models.Model):
    imagen = models.ImageField(null=True, blank=True)
    pais = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    # descripcion = models.TextField()
    descripcion = RichTextField(blank=True, null=True)
    fecha_viaje = models.DateField()
    autor = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) 

    class Meta:
        verbose_name_plural = "Publicaciones"
        db_table = "imageupload"

class Avatar(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='avatar/', null=True, blank=True)


class Comentario(models.Model):
    comentario = models.CharField(max_length=130)
    autor = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    fecha = models.DateField()



# class Mensaje(models.Model):

#     remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='remitente')
#     destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='destinatario')

#     mensaje = models.TextField(max_length=500, blank=True, null=True)

#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.mensaje