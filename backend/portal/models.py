from django.db import models


# Create your models here.


class Region(models.Model):
    nro_region = models.CharField(max_length=5)
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.nro_region} región)"

class Comuna(models.Model):
    nombre = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="comunas")

    def __str__(self):
        return f"{self.nombre}, de la región {self.region}"

class Inmueble(models.Model):
    class Tipo_Inmueble(models.TextChoices):
        casa = "CASA", _("Casa")
        departamento = "DPTO", _("Departamento")
        parcela = "PARC", _("Parcela")
    
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    m2_construido = models.FloatField(default=0)
    m2_total = models.FloatField(default=0)
    estacionamientos = models.PositiveSmallIntegerField(default=0)
    habitaciones = models.PositiveSmallIntegerField(default=0)
    baños = models.PositiveSmallIntegerField(default=0)
    direccion = models.CharField(max_length=100)
    comuna = models.ForeignKey(Comuna, on_delete=models.PROTECT, related_name="inmuebles")
    arriendo_mensual = models.DecimalField(max_digits=8, decimal_places=2)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    tipo_inmueble = models.CharField(max_length=20, choices=Tipo_Inmueble.choices)