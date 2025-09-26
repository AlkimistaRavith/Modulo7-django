from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

### FORMULARIO DE REGION
class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ["nro_region", "nombre"]

### FORMULARIO DE COMUNA
class ComunaForm(forms.ModelForm):
    class Meta:
        model = Comuna
        fields = ["region", "nombre"]

### FORMULARIO DE INMUEBLE
class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = [
            "nombre",
            "descripcion",
            "imagen",
            "m2_construido",
            "m2_total",
            "estacionamientos",
            "habitaciones",
            "banos",
            "direccion",
            "comuna",
            "arriendo_mensual",
            "tipo_inmueble",
        ]

### FORMULARIO DE SOLICITUDES DE ARRIENDO
class SolicitudArriendoForm(forms.ModelForm):
    class Meta:
        model = SolicitudArriendo
        fields = [
            "inmueble",
            "mensaje",
        ]

### FORMULARIO DE TIPO DE USUARIO (PERFIL ARRENDADOR O ARRENDATARIO)
class PerfilUserForm(forms.ModelForm):
    class Meta:
        model = PerfilUser
        fields = ["tipo_usuario", "rut", "imagen"]

### FORMULARIO DE REGISTRO
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = PerfilUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "rut",
            "imagen",
            "tipo_usuario",
            "password1",
            "password2",
        ]

### FORMULARIO DE LOGIN (DE AUTHENTICATION FORM DJANGO)
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

class ContactDataForm(forms.Form):
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(label='Mensaje', widget=forms.Textarea)