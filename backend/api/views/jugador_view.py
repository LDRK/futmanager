from rest_framework import status
from rest_framework.response import Response
from api.models.jugador import Jugador
from rest_framework.decorators import api_view
# from rest_framework.views import APIView
from api.serializers.jugador_serializer import JugadorSerializer

@api_view(['GET','POST'])
def jugador_api_view(request):
    """Vista API para listar todos los jugadores (GET) y crear nuevos (POST)"""
    
    if request.method == 'GET':
        # Obtener todos los jugadores y serializarlos
        jugador = Jugador.objects.all()
        jugador_serizers = JugadorSerializer(jugador,many = True)
        return Response(jugador_serizers.data, status = status.HTTP_200_OK)
    
    elif request.method == 'POST':
        # Crear nuevo jugador con validación
        jugador_serizers = JugadorSerializer(data = request.data)
        if jugador_serizers.is_valid():
            jugador_serizers.save()
            return Response({'message':'Jugador registrado correctamente'}, status = status.HTTP_201_CREATED)
        return Response(jugador_serizers.errors)

@api_view(['GET','PUT','DELETE'])
def jugador_details_view(request,pk=None):
    """Vista API para operaciones específicas de un jugador por ID"""
    
    # Buscar jugador por ID
    jugador_id = Jugador.objects.filter(id = pk).first()
    
    if jugador_id:
    
        if request.method == 'GET':
            # Obtener detalles del jugador específico
            jugador_serizers = JugadorSerializer(jugador_id)
            return Response(jugador_serizers.data, status = status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            # Actualizar jugador existente
            jugador_serizers = JugadorSerializer(jugador_id, data = request.data)
            if jugador_serizers.is_valid():
                jugador_serizers.save()
                return Response({'message':'Registro actualizado correctamente'}, status = status.HTTP_201_CREATED)
            return Response(jugador_serizers.errors)
        
        elif request.method == 'DELETE':
            # Eliminar jugador
            jugador_id.delete()
            return Response({'message':'Registro eliminado correctamente'})
    else:
        # Jugador no encontrado
        return Response({'Error':'Pagina no encontrada'}, status=status.HTTP_404_NOT_FOUND)