from django.db import models
from django.contrib.auth.models import User
import pytz 

class Categoria(models.Model):
    Nombre = models.CharField(max_length=100)
    Equipos = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.Nombre}'
    
    def clubes_asociados(self):
        return ", ".join([f"{club.Nombre} ({club.Ciudad})" for club in self.clubes.all()])

class Clubes(models.Model):
    Nombre = models.CharField(max_length=100)
    Ciudad = models.CharField(max_length=100)
    Provincia = models.CharField(max_length=100)
    Categoria = models.ForeignKey(Categoria, related_name='clubes', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='clubes_avatares/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def fecha_creacion_buenos_aires(self):
        tz = pytz.timezone('America/Argentina/Buenos_Aires')
        fecha_buenos_aires = self.fecha_creacion.astimezone(tz)
        return fecha_buenos_aires.strftime('%d/%m/%Y %H:%M:%S')

    class Meta:
        unique_together = ('Nombre', 'Ciudad', 'Provincia')

    def __str__(self):
        return f'{self.Nombre} ({self.Provincia})'

class Usuario(models.Model):
    Nombre_Usuario = models.CharField(unique=True, max_length=120)
    Email = models.EmailField()
    Hincha = models.ForeignKey(Clubes, related_name='usuarios', on_delete=models.CASCADE)
    CrearContraseña = models.CharField(max_length=150)
    
    def __str__(self):
        return f'{self.Nombre_Usuario}'
    
    
class Avatar (models.Model):
    
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null=True)
    
class AvatarClubes (models.Model):
    
    user= models.ForeignKey(Clubes, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null=True)