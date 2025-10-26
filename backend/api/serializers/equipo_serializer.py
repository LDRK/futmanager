from rest_framework import serializers
from api.models.equipo import Equipo

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'
        
    def to_representation(self, instance):
        return {
            'nombre': instance.nombre,
            'fecha_inscripcion': instance.fecha_inscripcion,
        }