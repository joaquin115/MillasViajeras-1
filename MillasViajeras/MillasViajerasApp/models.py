from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import *

# Create your models here.

class Persona(models.Model):

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha = models.DateField(max_length=20)

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