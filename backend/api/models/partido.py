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
    
    # Aquí se relacionan con EquipoTorneo (no directamente con Equipo)
    equipo_local = models.ForeignKey('api.EquipoTorneo', related_name='partidos_local', on_delete=models.CASCADE)
    equipo_visitante = models.ForeignKey('api.EquipoTorneo', related_name='partidos_visitante', on_delete=models.CASCADE)
    
    fecha_partido = models.DateTimeField(null=True, blank=True)
    lugar_partido = models.TextField(null=True, blank=True)
    marcador_local = models.PositiveIntegerField(default=0)
    marcador_visitante = models.PositiveIntegerField(default=0)
    estado = models.CharField(max_length=15, choices=ESTADOS, default='programado')
    jornada = models.PositiveIntegerField(null=True, blank=True)
    ronda = models.PositiveIntegerField(null=True, blank=True)
    grupo = models.CharField(max_length=20, null=True, blank=True)
    
    class Meta:
        db_table = 'partido'
        verbose_name = 'Partido'
        verbose_name_plural = 'Partidos'
        ordering = ['fecha_partido', 'jornada', 'ronda']
    
    def __str__(self):
        local = self.equipo_local.equipo.nombre
        visitante = self.equipo_visitante.equipo.nombre

        if self.estado == 'finalizado':
            return f"{local} {self.marcador_local} - {self.marcador_visitante} {visitante}"
        return f"{local} vs {visitante}"

    def clean(self):
        # Validar que no se enfrente el mismo equipo
        if self.equipo_local == self.equipo_visitante:
            raise ValidationError('Un equipo no puede jugar contra sí mismo.')

        # Validar que ambos equipos pertenezcan al mismo torneo
        if self.equipo_local.torneo != self.torneo or self.equipo_visitante.torneo != self.torneo:
            raise ValidationError('Ambos equipos deben pertenecer al mismo torneo.')
