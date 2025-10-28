from rest_framework import serializers  
from api.models.torneo import Torneo, Estadistica_torneo_equipo

class TorneoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Torneo
        exclude = ('created_at','updated_at')
        
    # Reescribimos la representación del modelo serializado (to_representation)
    # para mostrar datos legibles en campos con relaciones (ejemplo: organizador),
    # en lugar de solo el ID numérico de la relación.
     
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'nombre': instance.nombre,
            'descripcion': instance.descripcion,
            'fecha_inicio': instance.fecha_inicio,
            'fecha_fin': instance.fecha_fin,
            'organizador': instance.organizador.profile.nombre,
            'activo': instance.is_active,
            'estado': instance.estado,
            
        }


class EstadisticasEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadistica_torneo_equipo
        fields = '__all__'