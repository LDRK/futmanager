from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from api.models.torneo import Torneo, Estadistica_torneo_equipo
from api.serializers.torneo_serializer import TorneoSerializer, EstadisticasEquipoSerializer
from api.models.torneo import generar_fixture



# LISTAR TORNEOS
@api_view(['GET','POST'])
def torneo_view(request):
    """Vista API para listar todos los Torneos (GET) y crear nuevos (POST)"""
    
    if request.method == 'GET':
        # Obtenemos todos los torneos serializados
        torneos = Torneo.objects.all()
        torneo_serizers = TorneoSerializer(torneos, many=True)
        return Response(torneo_serizers.data, status=status.HTTP_200_OK)
    
    # Creamos los torneos
    elif request.method == 'POST':
        torneo_serizers = TorneoSerializer(data=request.data)
        if torneo_serizers.is_valid():
            torneo_serizers.save()
            return Response({'message': 'Torneo creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(torneo_serizers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','PATCH','DELETE'])
def torneo_detail(request, pk=None):
    """Vista API para operaciones específicas de un docente por ID"""
    
    torneo_id = Torneo.objects.filter(id = pk).first()
    
    if torneo_id:
        if request.method == 'GET':
            # Obtenemos el id del torneo especifico
            torneo_serizers = TorneoSerializer(torneo_id)
            return Response(torneo_serizers.data,status=status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            # Actualizamod el torneo
            torneo_serizers = TorneoSerializer(torneo_id, data = request.data)
            if torneo_serizers.is_valid():
                torneo_serizers.save()
                return Response({'message':'Registro actualizado correctamente'}, status = status.HTTP_201_CREATED)
            return Response(torneo_serizers.errors)
        
        elif request.method == 'PATCH':
            # Actualizamos un campo especifico del torneo
            torneo_serizers = TorneoSerializer(torneo_id, data = request.data)
            if torneo_serizers.is_valid():
                torneo_serizers.save()
                return Response({'message':'Registro actualizado correctamente'}, status = status.HTTP_201_CREATED)
            return Response(torneo_serizers.errors)
        
        elif request.method == 'DELETE':
            # Eliminar Torneo
            torneo_id.delete()
            return Response({'message':'Registro eliminado correctamente'})
    else:
        # Torneo no encontrado
        return Response({'Error':'Pagina no encontrada'}, status=status.HTTP_404_NOT_FOUND)


# Vista para generar el fixture del torneo
@api_view(['POST'])
def generar_fixture_view(request, pk=None):
    if request.method == "POST":
        try:
            torneo = Torneo.objects.get(pk=pk)
            print(torneo)

            # Evitar generar fixture si ya existe
            if torneo.partido_set.exists():
                return Response({'error': 'El fixture ya fue generado.'}, status=status.HTTP_400_BAD_REQUEST)

            # Ejecutar el algoritmo
            generar_fixture(torneo)
          

            return Response({'success': True, 'message': 'Fixture generado correctamente.'}, status=status.HTTP_200_OK)

        except Torneo.DoesNotExist:
            return Response({'error': 'Torneo no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        
    


















