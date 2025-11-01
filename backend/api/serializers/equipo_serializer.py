from rest_framework import serializers
from api.models.equipo import Equipo

class EquipoSerializer(serializers.ModelSerializer):
    fecha_inscripcion = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = Equipo
        fields = ['id','nombre', 'fecha_inscripcion']

        
    