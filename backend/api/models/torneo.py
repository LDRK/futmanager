from django.db import models
from django.contrib.auth.models import User
from .equipo import EquipoTorneo
from .partido import Partido
from ..utils.fixture import fixture_eliminacion,fixture_por_grupos,fixture_todos_contra_todos

# Modelo Torneo 
class Torneo(models.Model):
    # Los estados en que el torneo puede estar
    ESTADOS_TORNEO = [
        ('registro', 'Registro'),
        ('activo', 'En curso'),
        ('finalizado', 'Finalizado')
    ]
    
    # La modalidad del formato que tendra el torneo
    FORMATO_TORNEO = [
        ('todos', 'Todos contra todos'),
        ('eliminacion', 'Eliminación directa'),
        ('grupos', 'Por grupos'),
    ]
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    organizador = models.ForeignKey(User, on_delete=models.CASCADE, related_name="torneos_organizados")
    is_active = models.BooleanField(default=True)
    estado = models.CharField(max_length=20, choices=ESTADOS_TORNEO, default='registro')
    formato = models.CharField(max_length=20,choices=FORMATO_TORNEO, default='eliminacion')
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
    
    # Aquí se genera automáticamente el fixture cuando se llama el método
def generar_fixture(torneo):
    # Obtenemos los equipos inscritos en este torneo
    equipos_torneo = list(EquipoTorneo.objects.filter(torneo=torneo))
    formato = torneo.formato

    if len(equipos_torneo) < 2:
        raise ValueError("Debe haber al menos dos equipos inscritos para generar el fixture.")

    if formato == "todos":
        jornadas = fixture_todos_contra_todos(equipos_torneo)
        for i, jornada in enumerate(jornadas, start=1):
            for local, visitante in jornada:
                Partido.objects.create(
                    torneo=torneo,
                    equipo_local=local,
                    equipo_visitante=visitante,
                    fecha_partido=None,
                    lugar_partido="Por definir",
                )

    elif formato == "eliminacion":
        rondas = fixture_eliminacion(equipos_torneo)
        for ronda, enfrentamientos in enumerate(rondas, start=1):
            for local, visitante in enfrentamientos:
                Partido.objects.create(
                    torneo=torneo,
                    equipo_local=local,
                    equipo_visitante=visitante,
                    fecha_partido=None,
                    lugar_partido="Por definir",
                )

    elif formato == "grupos":
        grupos = fixture_por_grupos(equipos_torneo)
        for nombre, jornadas in grupos.items():
            for i, jornada in enumerate(jornadas, start=1):
                for local, visitante in jornada:
                    Partido.objects.create(
                        torneo=torneo,
                        equipo_local=local,
                        equipo_visitante=visitante,
                        fecha_partido=None,
                        lugar_partido="Por definir",
                    )

    torneo.estado = "activo"
    torneo.save()
    return "Fixture generado correctamente."




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