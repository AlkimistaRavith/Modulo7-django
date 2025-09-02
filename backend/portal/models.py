from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
import uuid
from django.conf import settings

# Create your models here.

#MODELO DE REGION
class Region(models.Model):
    nro_region = models.CharField(max_length=5)
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.nro_region} región)"

#MODELO DE COMUNA
class Comuna(models.Model):
    nombre = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="comunas")

    def __str__(self):
        return f"{self.nombre}, de la {self.region}"

#MODELO DE INMUEBLE
class Inmueble(models.Model):
    class Tipo_Inmueble(models.TextChoices):
        CASA = "Casa", _("Casa")
        DEPARTAMENTO = "Departamento", _("Departamento")
        PARCELA = "Parcela", _("Parcela")
    
    propietario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="inmuebles", null=True, blank=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(default="sin_imagen")
    m2_construido = models.FloatField(default=0)
    m2_total = models.FloatField(default=0)
    estacionamientos = models.PositiveSmallIntegerField(default=0)
    habitaciones = models.PositiveSmallIntegerField(default=0)
    banos = models.PositiveSmallIntegerField(default=0)
    direccion = models.CharField(max_length=100)
    comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT, related_name="inmuebles")
    arriendo_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    tipo_inmueble = models.CharField(max_length=20, choices=Tipo_Inmueble.choices)

    def __str__(self):
            return f"{self.nombre} ( {self.arriendo_mensual} )"

#MODELO DE SOLICITUD ARRIENDO
class SolicitudArriendo(models.Model):
    class EstadoSolicitud(models.TextChoices):
        PENDIENTE = "Pendiente", _("Pendiente")
        ACEPTADO = "Aceptado", _("Aceptada")
        RECHAZADO = "Rechazado", _("Rechazada")
    
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, related_name="solicitudes")
    arrendatario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="solicitudes_enviadas", null=True, blank=True)
    mensaje = models.TextField(null=True, blank=True)
    estado = models.CharField(max_length=10, choices=EstadoSolicitud.choices, default=EstadoSolicitud.PENDIENTE)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)    
    
    def __str__(self):
        return f"{self.uuid} - {self.inmueble} - {self.estado}"


#MODELO PERFIL USUARIO
class PerfilUser(AbstractUser):
    class TipoUsuario(models.TextChoices):
        ARRENDATARIO = "arrendatario", _("Arrendatario")
        ARRENDADOR = "arrendador", _("Arrendador")
        
    tipo_usuario = models.CharField(max_length=13, choices=TipoUsuario.choices, default=TipoUsuario.ARRENDATARIO)
    rut = models.CharField(max_length=50, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.get_full_name()} | {self.tipo_usuario}"

