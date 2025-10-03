from rest_framework import serializers
from api.models.estadisticas import EstadisticaJugador, EstadisticaEquipo

class EstadisticasJugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadisticaJugador
        fields = '__all__'

class EstadisticasEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadisticaEquipo
        fields = '__all__'