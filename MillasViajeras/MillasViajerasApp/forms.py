from ctypes import WinDLL
from dataclasses import fields
from tkinter import W
from xmlrpc.client import TRANSPORT_ERROR
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.fields import *
from django.forms import ModelForm, Textarea
from numpy import size


from .models import Avatar, Comentario


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar", widget=forms.PasswordInput)
    
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']

        help_texts = {k:"" for k in fields}
        
class UserEditForm(forms.Form):

    email = forms.EmailField(label="Email")  
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")    
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

        # help_texts = {k:"" for k in fields}

class CrearPublicacion(forms.Form):
    imagen = forms.ImageField(allow_empty_file=True)
    pais = forms.CharField(max_length=50)
    titulo = forms.CharField(max_length=50)
    descripcion = RichTextFormField()

class AvatarForm(forms.Form):

    imagen = forms.ImageField(label="Imagen", required=False)

    class Meta:
        model = Avatar
        fields = ['imagen']

class CrearComentario(forms.Form):
    comentario = forms.CharField(max_length=130, widget=Textarea)
      

# class CrearMensaje(forms.Form):
#     usuario = []
#     usuarios = User.objects.all()

#     for user in usuarios:
#         usuario.append(user.email)
    

#     destinatario = forms.EmailField(label='Email', required=True, widget=forms.Select(choices=[usuario]))

#     mensaje = RichTextFormField(label='Mensaje', required=True, widget=forms.Textarea)