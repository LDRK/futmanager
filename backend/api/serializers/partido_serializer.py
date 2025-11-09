from rest_framework import serializers
from api.models.partido import Partido

class PartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partido
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            'id':instance.id,
            'fecha_partido': instance.fecha_partido,
            'lugar_partido': instance.lugar_partido,
            'marcador_local': instance.marcador_local,
            'marcador_visitante': instance.marcador_visitante,
            'estado': instance.estado,
            'jornada': instance.jornada,
            'ronda': instance.ronda,
            'grupo': instance.grupo,
            'torneo': 1,
            'equipo_local': instance.equipo_local.equipo.nombre,
            'equipo_visitante': instance.equipo_visitante.equipo.nombre,
            
        }