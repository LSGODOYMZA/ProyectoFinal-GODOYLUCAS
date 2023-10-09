from django import forms
from .models import Categoria, Clubes, Usuario, Avatar, AvatarClubes
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

#Crear formulario con Form
class UsuarioFormulario(forms.Form):
    Nombre_Usuario = forms.CharField(max_length=120)
    Email = forms.EmailField()
    Hincha = forms.ModelChoiceField(queryset=Clubes.objects.all())
    Contraseña = forms.CharField()

#Crear formulario con ModelForm    
class UsuarioFormulario1 (forms.ModelForm):
    class Meta :
        model= Usuario
        fields= '__all__'
    
class ClubesFormularioedit(forms.ModelForm):
    class Meta:
        model = Clubes
        fields = ['Nombre', 'Ciudad', 'Provincia', 'Categoria', 'avatar']

class ClubesFormulariocreate(forms.ModelForm):
    class Meta:
        model = Clubes
        fields = ['Nombre', 'Ciudad', 'Provincia', 'Categoria', 'avatar']
    #Categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())
    
   # Nombre = forms.CharField ()
   # Ciudad = forms.CharField ()
   # Provincia = forms.CharField()
   # Categoria = forms.CharField()
   
class UserEditForm(UserChangeForm):
    
    password= forms.CharField(help_text="", widget=forms.HiddenInput(), required=False)
    
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    class Meta:
        model= User
        fields= ["email", "first_name", "last_name", "password1", "password2"]
        
    def clean_password2(self):
        
        password1=self.cleaned_data["password1"]
        password2=self.cleaned_data["password2"]
        
        if password1 != password2:
            raise forms.ValidationError ("Las Contraseñas no coinciden!")
        return password2
    
class AvatarFormulario(forms.ModelForm):
    
    class Meta:
        model = Avatar
        fields= ["imagen"]