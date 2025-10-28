from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


#Models Jugador
# class Jugador(models.Model):
#     jugador = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jugadores_asociados")
#     equipo = models.ForeignKey('api.Equipo', on_delete=models.CASCADE)
#     numero_camisa = models.PositiveSmallIntegerField()
#     posicion = models.CharField(max_length=50)

class Jugador(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )  # Puede estar vacío
    equipo = models.ForeignKey('api.Equipo', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True)
    posicion = models.CharField(max_length=50, blank=True)
    numero_camiseta = models.PositiveIntegerField(null=True, blank=True)
    fecha_registro = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    