from django.urls import path
from django.contrib.auth.views import LogoutView
from App1.views import *

urlpatterns = [
    path('', inicio, name = 'Inicio'),
    path('equipos/', equipos, name = 'Equipos'),
    path('categorias/', categorias, name = 'Categorias'),
    path('busqueda-equipos/', busqueda_equipos, name = 'Buscar Equipos'),
    path( 'buscar/', buscar_equipos, name='Buscar'),
    path( 'formulario-clubes/', crear_equipos, name='Formulario de Clubes'),
    path( 'primera/', PrimeraDivision, name='Primera A'),
    path( 'nacional/', BNacional, name='Nacional B'),
    path( 'metropolitana/', BMetro, name='Metro'),
    path( 'federal/', Federal, name='Federal'),
    path('formulario-usuarios/', crear_usuario, name='Formulario de Usuario'),
    path('eliminar-equipos/<int:id>', eliminar_equipos, name='Eliminar Clubes'),
    path('editar-equipos/<int:id>', editar_equipos, name='Editar Clubes'),
    path('usuario/', usuarios, name='Lista Usuarios'),
    path('editar-usuarios/<int:id>', editar_usuarios, name='Editar Usuario'),
    path('eliminar-usuarios/<int:id>', eliminar_usuarios, name='Eliminar Usuario'),
    path('ver-usuarios/<int:id>', ver_usuarios, name='Ver Usuario'),
    path('login/', login_view, name='Login'),
    path('registro/', register, name='Registro'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name='Cerrar Sesion'),
    path('editar-perfil/', editar_perfil, name='Editar Perfil'),
    path('avatar-user/', crea_avatar, name='Agregar Avatar'),
    path('clubes/<int:id>/', ver_equipos, name='detalle_club'),
    path('acercademi/', acerca_de_mi, name='AcercaDeMi'),
]