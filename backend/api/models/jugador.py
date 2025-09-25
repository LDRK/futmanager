from django.db import models
from django.contrib.auth.models import User


# Models Jugador
class Jugador(models.Model):
    jugador = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jugadores_asociados")
    equipo = models.ForeignKey('api.Equipo', on_delete=models.CASCADE)
    numero_camisa = models.PositiveSmallIntegerField()
    posicion = models.CharField(max_length=50)

    