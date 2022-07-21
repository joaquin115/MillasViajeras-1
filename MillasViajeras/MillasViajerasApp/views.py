from pyclbr import Class
from xmlrpc.client import DateTime
from django.contrib import messages
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
import datetime
from django.contrib import messages

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from .models import *
from .forms import *

from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.

def inicio(request):
    publicaciones = Publicaciones.objects.all()    
    ultima_publicacion = publicaciones.last()
    total_publicaciones = publicaciones.count()    

    usuarios = User.objects.all()        
    total_usuarios = usuarios.count()    

    return render(request, "MillasViajerasApp/index.html", {"publicaciones":publicaciones,'total_usuarios':total_usuarios, 'total_publicaciones':total_publicaciones, 'ultima_publicacion':ultima_publicacion,})

def publicaciones(request):
        publicaciones = Publicaciones.objects.all().order_by('-id')

        return render(request, "MillasViajerasApp/publicaciones.html", {"publicaciones":publicaciones})

def registro(request):

    if request.method == "POST":

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            form.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('inicio')            
            else:
                return redirect('login')
        
        return render(request, 'MillasViajerasApp/registro.html', {"form":form})
    
    form = UserRegisterForm()

    return render(request, 'MillasViajerasApp/registro.html', {"form":form})

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)                
                return redirect("inicio")
            else:                
                return redirect("login")
                
        else:
            return redirect("login")
    
    form = AuthenticationForm()

    return render(request,"MillasViajerasApp/login.html",{"form":form})

def logout_request(request):
    logout(request)
    return redirect("inicio")

@login_required
def editar_perfil(request):

    user = request.user

    if request.method == "POST":

        form = UserEditForm(request.POST)

        if form.is_valid():

            info = form.cleaned_data
            user.email = info['email']
            user.first_name = info['first_name']
            user.last_name = info['last_name']

            user.save()

            return redirect('inicio')

    else:
        form = UserEditForm(initial={'email':user.email, "first_name":user.first_name, "last_name":user.last_name})
    
    return render (request, 'MillasViajerasApp/editarPerfil.html', {"form":form})

@login_required
def agregar_avatar(request):

    if request.method == "POST":

        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():

            user = request.user

            avatar = Avatar(user=user, imagen=form.cleaned_data["imagen"])

            avatar.save()

            return redirect("inicio")

    else:

        form = AvatarForm()

    return render(request, "MillasViajerasApp/agregar_avatar.html", {"form":form})

@login_required
def crear_publicacion(request):   
   
    if request.method == "POST":
        
        publicacion = CrearPublicacion(request.POST, request.FILES)
        
        if publicacion.is_valid():

            informacion = publicacion.cleaned_data

            publicacion_nueva = Publicaciones(imagen=informacion["imagen"],pais=informacion["pais"], titulo=informacion["titulo"], descripcion=informacion["descripcion"], fecha_viaje=datetime.datetime.today(), autor=request.user)
            publicacion_nueva.save()

            return redirect('inicio')
        
        return render(request, "MillasViajerasApp/crearpublicacion.html", {"publicacion":publicacion})
    
    publicacion = CrearPublicacion()
    return render(request, 'MillasViajerasApp/crearpublicacion.html', {'publicacion':publicacion})

@login_required
def mis_publicaciones(request):
    publicaciones = Publicaciones.objects.filter(autor=request.user).order_by('-id')        

    return render(request, "MillasViajerasApp/mis_publicaciones.html", {"publicaciones":publicaciones})

def about(request):

    return render(request, "MillasViajerasApp/about.html", {})

class ver_publicacion(DetailView):

    model = Publicaciones
    template_name = "MillasViajerasApp/ver_publicacion.html"   

@login_required
def editar_publicacion(request, publicacion_id):
    
    publicacion = Publicaciones.objects.get(id=publicacion_id)

    if request.method == "POST":

        formulario = CrearPublicacion(request.POST, request.FILES)

        if formulario.is_valid():

            info_publicacion = formulario.cleaned_data

            publicacion.imagen = info_publicacion["imagen"]
            publicacion.pais = info_publicacion["pais"]
            publicacion.titulo = info_publicacion["titulo"]
            publicacion.descripcion = info_publicacion["descripcion"]           

            publicacion.save()
            
            return redirect ("mis_publicaciones")

    
    formulario = CrearPublicacion(initial={"pais":publicacion.pais, "titulo":publicacion.titulo, "descripcion":publicacion.descripcion, "fecha_viaje":datetime.datetime.today()})

    return render (request, "MillasViajerasApp/editar_publicacion.html", {"form":formulario})

@login_required
def eliminar_publicacion(request, publicacion_id):

    publicacion = Publicaciones.objects.get(id=publicacion_id)
    publicacion.delete()

    return redirect("mis_publicaciones")