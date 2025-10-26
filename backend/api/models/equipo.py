from django.db import models
# from django.contrib.auth.models import User


# Modelo Equipo
class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    # capitan = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    

# Modelo Equipo_Torneo
class EquipoTorneo(models.Model):
    equipo = models.ForeignKey('api.Equipo', on_delete=models.CASCADE)
    torneo = models.ForeignKey('api.Torneo', on_delete=models.CASCADE)