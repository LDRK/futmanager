from django.db import models

class EstadisticaJugador(models.Model):
    partido = models.ForeignKey('api.Partido', on_delete=models.CASCADE, related_name="estadisticas")
    jugador = models.ForeignKey('api.Jugador', on_delete=models.CASCADE, related_name="estadisticas")

    goles = models.PositiveIntegerField(default=0)
    asistencias = models.PositiveIntegerField(default=0)
    amarillas = models.PositiveIntegerField(default=0)
    rojas = models.PositiveIntegerField(default=0)
    minutos_jugados = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("partido", "jugador")  # Evitamos duplicados
        verbose_name = "Estadística"
        verbose_name_plural = "Estadísticas"

    def __str__(self):
        return f"{self.jugador} - {self.partido}"


class EstadisticaEquipo(models.Model):
    torneo = models.ForeignKey('api.Torneo', on_delete=models.CASCADE, related_name="estadisticas_equipos")
    equipo = models.ForeignKey('api.Equipo', on_delete=models.CASCADE, related_name="estadisticas_torneo")

    partidos_jugados = models.PositiveIntegerField(default=0)
    partidos_ganados = models.PositiveIntegerField(default=0)
    partidos_empatados = models.PositiveIntegerField(default=0)
    partidos_perdidos = models.PositiveIntegerField(default=0)

    goles_a_favor = models.PositiveIntegerField(default=0)
    goles_en_contra = models.PositiveIntegerField(default=0)
    diferencia_goles = models.IntegerField(default=0)
    puntos = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("torneo", "equipo") # Evitamos duplicados

    def __str__(self):
        return f"{self.equipo} en {self.torneo}"
