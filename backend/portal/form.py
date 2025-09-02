from django import forms
from .models import *

# clase 01/09/25
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ["nro_region", "nombre"]

class ComunaForm(forms.ModelForm):
    class Meta:
        model = Comuna
        fields = ["region", "nombre"]


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

class SolicitudArriendoForm(forms.ModelForm):
    class Meta:
        model = SolicitudArriendo
        fields = [
            "inmueble",
            "arrendatario",
            "mensaje",
        ]

class PerfilUserForm(forms.ModelForm):
    class Meta:
        model = PerfilUser
        fields = ["tipo_usuario", "rut"]

# clase 01/09/2025
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
            "tipo_usuario",
            "password1",
            "password2",
        ]
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)