from rest_framework import serializers
from api.models.jugador import Jugador

class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            'numero_camisa': instance.numero_camisa,
            'posicion': instance.posicion,
            'jugador': instance.jugador.profile.nombre,
            'equipo': instance.equipo.nombre
        }
    