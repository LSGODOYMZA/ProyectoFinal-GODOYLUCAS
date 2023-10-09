from django.contrib import admin
from .models import Categoria, Clubes, Usuario, Avatar, AvatarClubes

# Register your models here.

admin.site.register (Clubes)
admin.site.register (Usuario)
admin.site.register (Avatar)
admin.site.register (AvatarClubes)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Equipos', 'clubes_asociados')

admin.site.register(Categoria, CategoriaAdmin)