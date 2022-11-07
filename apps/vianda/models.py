from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TipoPlato(models.Model):
    descripcion = models.CharField(max_length=20,blank=True)
    estado_activo = models.BooleanField(default=True)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.descripcion)

class Vianda(models.Model):
    FRECUENCIA_VIANDA = (
        ('semanal','Semanal'),
        ('quincenal','Quincenal')
    )
    TIPO_MENU = (
        ('normal','Normal'),
        ('diabetico','Diabetico'),
        ('vegetariano','Vegetariano')
    )
    ESTADO_VIANDA=(
        ('pendiente','Pendiente'),
        ('confirmado','Confirmado'),
        ('cancelado','Cancelado')
    )
    frecuencia = models.CharField(max_length=11, choices=FRECUENCIA_VIANDA)
    tipo_menu= models.CharField(choices=TIPO_MENU, max_length=11)
    fecha_vianda = models.DateField()
    cantidad = models.IntegerField()
    estado = models.CharField(max_length=11, choices=ESTADO_VIANDA)
    tipo_plato = models.ManyToManyField(TipoPlato)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True,unique=True)

