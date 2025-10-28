from rest_framework import serializers
from api.models.jugador import Jugador

class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        exclude = ('fecha_registro',)
    
    def to_representation(self, instance):
        return {
            'usuario': instance.usuario,
            'equipo': instance.equipo.nombre,
            'nombre': instance.nombre,
            'apellido': instance.apellido,
            'posicion': instance.posicion,
            'numero_camiseta': instance.numero_camiseta,
        }
        
    def validate(self, data):
        """
        Valida que haya al menos un identificador (usuario o nombre).
        """
        if not data.get('usuario') and not data.get('nombre'):
            raise serializers.ValidationError(
                {"detalle": "Debe ingresar el nombre del jugador o asociar un usuario existente."}
            )
        return data

    