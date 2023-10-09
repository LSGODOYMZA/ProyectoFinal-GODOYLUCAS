from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import *
from .forms import UsuarioFormulario, ClubesFormulariocreate, ClubesFormularioedit, UsuarioFormulario1, UserEditForm, AvatarFormulario

# Create your views here.

def inicio (req):
    
    try:
        avatar= Avatar.objects.get(user=req.user.id)
        return render (req, "Inicio.html", {"url_avatar":avatar.imagen.url})
    except:
        return render (req, "Inicio.html")
    
def crear_usuario (req):
    if req.method == 'POST':
        mi_formulario = UsuarioFormulario1 (req.POST)
        if mi_formulario.is_valid():
            data= mi_formulario.cleaned_data
            usuario = Usuario (Nombre_Usuario=data['Nombre_Usuario'], Email=data['Email'],Hincha=data['Hincha'], CrearContraseña=data['CrearContraseña'])
            usuario.save()
            return HttpResponse (f'{usuario.Nombre_Usuario} hincha de {usuario.Hincha} creado exitosamente')
        pass
    else:
        mi_formulario = UsuarioFormulario1 ()
        return render (req, "usuario_formularios.html", {'mi_formulario': mi_formulario})

@staff_member_required
def crear_equipos(request):
    if request.method == 'POST':
        mi_formulario = ClubesFormulariocreate(request.POST, request.FILES)
        if mi_formulario.is_valid():
            mi_formulario.save()
            nombre = mi_formulario.cleaned_data['Nombre']
            ciudad = mi_formulario.cleaned_data['Ciudad']
            provincia = mi_formulario.cleaned_data['Provincia']
            categoria = mi_formulario.cleaned_data['Categoria']
            return render(request, 'equipoexitoso.html', {'equipo_nombre': nombre})
    else:
        mi_formulario = ClubesFormulariocreate()
    
    return render(request, "clubes_formularios.html", {'mi_formulario': mi_formulario})
 
@login_required    
def busqueda_equipos(req):
    
    return render (req, 'BusquedaEquipos.html')

@login_required
def buscar_equipos(req):
    
    query = req.GET.get('q')
    if query:
        resultados = Clubes.objects.filter(Nombre=query)
    else:
        resultados = Clubes.objects.all()
    
    return render(req, 'ResultadoBusqueda.html', {'resultados': resultados})

@staff_member_required
def eliminar_equipos (req, id):
    
    if req.method == "POST":
        club = Clubes.objects.get(id=id)
        club.delete()
        
        equipos= Clubes.objects.all().order_by('Nombre')
        return render (req, "Equipos.html",{"equipos":equipos})

@staff_member_required
def editar_equipos (req, id):
    club = Clubes.objects.get(id=id) 
    if req.method == 'POST':
        mi_formulario = ClubesFormularioedit(req.POST, req.FILES, instance=club)
        if mi_formulario.is_valid():
            mi_formulario.save()
            return render (req, "Inicio.html")
            
        else:
            mi_formulario= ClubesFormularioedit(instance=club)
    return render (req, "EditarEquipos.html", {"mi_formulario": mi_formulario, "id":club.id})

def categorias(req):
    
    lista = Categoria.objects.all()
    
    return render (req, "Categorias.html", {"Categorias":lista})

@login_required
def equipos(req):
    
    equipos = Clubes.objects.all().order_by('Nombre')
    return render(req, 'Equipos.html', {'equipos': equipos})

@login_required
def PrimeraDivision(req):
    
    return render (req, "Primera.html")

@login_required
def acerca_de_mi (req):
    
    return render (req, "AcercadeMi.html")

@login_required
def BNacional(req):
    
    return render (req, "BNacional.html")

@login_required
def BMetro(req):
    
    return render (req, "BMetro.html")

@login_required
def Federal(req):
    
    return render (req, "Federal.html")

@login_required
def usuarios(req):
    
    usuarios = Usuario.objects.all().order_by('Nombre_Usuario')
    return render(req, 'Usuarios.html', {'usuarios': usuarios})

def editar_usuarios (req, id):
    user = Usuario.objects.get(id=id) 
    if req.method == 'POST':
        mi_formulario = UsuarioFormulario(req.POST)
        if mi_formulario.is_valid():
            data= mi_formulario.cleaned_data
            user.Nombre_Usuario = data ["Nombre_Usuario"]
            user.Email = data ["Email"]
            user.Hincha = data ["Hincha"]
            user.CrearContraseña = data ["Contraseña"]
            user.save()
            return render (req, "Inicio.html")
            
        else:
            mi_formulario= UsuarioFormulario(initial={"Nombre_Usuario":user.Nombre_Usuario, "Email":user.Email, "Hincha":user.Hincha, "Contraseña":user.CrearContraseña})
    return render (req, "EditarUsuarios.html", {"mi_formulario": mi_formulario, "id":user.id})

def eliminar_usuarios (req, id):
    
    if req.method == "POST":
        user = Usuario.objects.get(id=id)
        user.delete()
        
    user= Usuario.objects.all().order_by('Nombre_Usuario')
    return render (req, "Usuarios.html",{"usuarios":user})

def ver_usuarios (req, id):
    
    usuario = get_object_or_404(Usuario, id=id)
    
    return render(req, "usuario_detail.html", {"usuario": usuario})

def ver_equipos (req, id):
    
    equipo = get_object_or_404(Clubes, id=id)
    context = {
        'equipo': equipo,
    }
    return render(req, "EquipoDetalles.html", context)
 
def login_view (req):
    
    if req.method == 'POST':
        mi_formulario = AuthenticationForm(req, data=req.POST)
        if mi_formulario.is_valid():
            data= mi_formulario.cleaned_data
            usuario= data['username']
            psw= data['password']
            
            user= authenticate(username =usuario, password =psw)
            if user:
                login (req, user)
                return render (req, "Inicio.html", {"mensaje": f'Bienvenido {usuario}!!'})
        
        return render (req, "Inicio.html", {"mensaje": f'Datos Incorrectos'})
            
    else:
        mi_formulario= AuthenticationForm()
        return render (req, "Login.html", {"mi_formulario": mi_formulario})
    
def register (req):
    if req.method == 'POST':
        mi_formulario = UserCreationForm(req.POST)
        if mi_formulario.is_valid():
            data= mi_formulario.cleaned_data
            usuario= data['username']
            mi_formulario.save()
            return render (req, "Inicio.html", {"mensaje": f'Usuario {usuario} creado con exito!!'})
        
        return render (req, "Inicio.html", {"mensaje": f'Formulario Invalido'})
            
    else:
        mi_formulario= UserCreationForm()
        return render (req, "RegistroUser.html", {"mi_formulario": mi_formulario})

@login_required    
def editar_perfil (req):
    usuario= req.user 
    if req.method == 'POST':
        mi_formulario = UserEditForm(req.POST, instance= req.user)
        if mi_formulario.is_valid():
            
            data= mi_formulario.cleaned_data
            usuario.first_name = data ["first_name"]
            usuario.last_name = data ["last_name"]
            usuario.email = data ["email"]
            usuario.set_password(data["password1"])
            usuario.save()
            return render (req, "Inicio.html", {"mensaje": f'Datos actualizados con exito!'})
        else:
           return render (req, "EditarPerfil.html",{"mi_formulario": mi_formulario})     
    else:
        
        mi_formulario= UserEditForm(instance=usuario)
        return render (req, "EditarPerfil.html", {"mi_formulario": mi_formulario})
    
@login_required    
def crea_avatar (req):
    
    if req.method == 'POST':
        
        mi_formulario = AvatarFormulario(req.POST, req.FILES)
        
        if mi_formulario.is_valid():
            
            data= mi_formulario.cleaned_data
            
            avatar = Avatar(user=req.user, imagen=data["imagen"])
            
            avatar.save()
            
            return render (req, "Inicio.html", {"mensaje": f'Avatar actualizado con exito!'})
         
    else:
        mi_formulario= AvatarFormulario()
        return render (req, "AgregarAvatar.html", {"mi_formulario": mi_formulario})