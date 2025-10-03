from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from api.models.partido import Partido
from api.serializers.partido_serializer import PartidoSerializer


# LISTAR PARTIDOS
@api_view(['GET','POST'])
def partido_api_view(request):
    """Vista API para listar todos los Partidos (GET) y crear nuevos (POST)"""
    
    if request.method == 'GET':
        # Obtenemos todos los partidos serializados
        partido = Partido.objects.all()
        partido_serizers = PartidoSerializer(partido, many=True)
        return Response(partido_serizers.data, status=status.HTTP_200_OK)
    
    # Creamos los torneos
    elif request.method == 'POST':
        partido_serizers = PartidoSerializer(data=request.data)
        if partido_serizers.is_valid():
            partido_serizers.save()
            return Response({'message': 'Partido creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(partido_serizers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PATCH','DELETE'])
def partido_details_view(request, pk=None):
    """Vista API para operaciones específicas de un partido por ID"""
    
    partido_id = Partido.objects.filter(id = pk).first()
    
    if partido_id:
        if request.method == 'GET':
            # Obtenemos el id del Partido especifico
            partido_serizers = PartidoSerializer(partido_id)
            return Response(partido_serizers.data,status=status.HTTP_200_OK)
        
        elif request.method == 'PATCH':
            # Actualizamos el Partido
            partido_serizers = PartidoSerializer(partido_id, data = request.data)
            if partido_serizers.is_valid():
                partido_serizers.save()
                return Response({'message':'Registro actualizado correctamente'}, status = status.HTTP_201_CREATED)
            return Response(partido_serizers.errors)
        
        elif request.method == 'DELETE':
            # Eliminar Partido
            partido_id.delete()
            return Response({'message':'Registro eliminado correctamente'})
    else:
        # Partidoneo no encontrado
        return Response({'Error':'Pagina no encontrada'}, status=status.HTTP_404_NOT_FOUND)



        
    


















