from rest_framework import serializers
from api.models.estadisticas import EstadisticaJugador, EstadisticaEquipo

class EstadisticasJugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadisticaJugador
        exclude = ('created_at')
        
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'goles': instance.goles,
            'asistencias': instance.asistencias,
            'amarillas': instance.amarillas,
            'rojas': instance.rojas,
            'minutos_jugados': instance.minutos_jugados,
            'partido': instance.partido.id,
            'jugador': instance.jugador.nombre,
            
        }


class EstadisticasEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadisticaEquipo
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'partidos_jugados': instance.partidos_jugados,
            'partidos_ganados': instance.partidos_ganados,
            'partidos_empatados': instance.partidos_empatados,
            'partidos_perdidos': instance.partidos_perdidos,
            'goles_a_favor': instance.goles_a_favor,
            'goles_en_contra': instance.goles_en_contra,
            'diferencia_goles': instance.diferencia_goles,
            'puntos': instance.puntos,
            'torneo': instance.torneo.nombre,
            'equipo': instance.equipo.nombre,
            
        }