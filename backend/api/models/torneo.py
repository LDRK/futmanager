from django.db import models
from django.contrib.auth.models import User


# Modelo Torneo 
class Torneo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    organizador = models.ForeignKey(User, on_delete=models.CASCADE, related_name="organizador")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        """
        Cada vez que guardamos el torneo, revisamos si ya pasó la fecha de fin.
        Si ya terminó, se marca inactivo automáticamente.
        """
        from django.utils.timezone import now

        if self.fecha_fin < now().date():
            self.is_active = False

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre
    

# Modelo Estadisticas_torneo_equipo
class Estadistica_torneo_equipo(models.Model):
    equipo = models.ForeignKey('api.Equipo', on_delete=models.CASCADE)
    torneo = models.ForeignKey('api.Torneo', on_delete=models.CASCADE)
    partidos_jugados = models.PositiveIntegerField()
    partidos_ganados = models.PositiveIntegerField()
    partidos_empatados = models.PositiveIntegerField()
    partidos_perdidos = models.PositiveIntegerField()
    goles_favor = models.PositiveIntegerField()
    goles_contra = models.PositiveIntegerField()
    goles_diferencia = models.IntegerField()
    
    def __str__(self):
        return f'Estadísticas de {self.equipo.nombre} en {self.torneo.nombre}'