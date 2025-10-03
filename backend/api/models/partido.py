from django.db import models
from django.core.exceptions import ValidationError

# Modelo Partido
class Partido(models.Model):
    ESTADOS = [
        ('en juego', 'En juego'),
        ('finalizado', 'Finalizado'),
        ('programado', 'Programado'),  
    ]
    
    torneo = models.ForeignKey('api.Torneo', on_delete=models.CASCADE)
    equipo_local = models.ForeignKey('api.EquipoTorneo', related_name='partidos_local', on_delete=models.CASCADE)
    equipo_visitante = models.ForeignKey('api.EquipoTorneo', related_name='partidos_visitante', on_delete=models.CASCADE)
    fecha_partido = models.DateTimeField()
    lugar_partido = models.TextField()
    marcador_local = models.PositiveIntegerField(default=0)
    marcador_visitante = models.PositiveIntegerField(default=0)
    estado = models.CharField(max_length=15, choices=ESTADOS, default='programado')
    
    class Meta:
        db_table = 'partido'
        verbose_name = 'Partido'
        verbose_name_plural = 'Partidos'
        ordering = ['fecha_partido']
    
    def __str__(self):
        if self.estado == 'finalizado':
            return f"{self.equipo_local.nombre} {self.marcador_local}-{self.marcador_visitante} {self.equipo_visitante.nombre}"
        return f"{self.equipo_local.nombre} vs {self.equipo_visitante.nombre}"
    
    def clean(self):
        if self.equipo_local == self.equipo_visitante:
            raise ValidationError('Un equipo no puede jugar contra sí mismo.')
        if self.equipo_local.id_torneo != self.torneo or self.equipo_visitante.id_torneo != self.torneo:
            raise ValidationError('Ambos equipos deben pertenecer al mismo torneo.')
