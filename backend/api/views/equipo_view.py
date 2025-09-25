from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from api.models.equipo import Equipo,EquipoTorneo
from api.models.torneo import Torneo
from api.serializers.equipo_serializer import EquipoSerializer

@api_view(['GET', 'POST'])
def equipo_api_view(request):
    """Vista API para listar todos los equipos (GET) y crear nuevos vinculados a torneos (POST)"""
    
    if request.method == 'GET':
        # Obtener todos los equipos y serializarlos
        equipo = Equipo.objects.all()
        equipo_serializers = EquipoSerializer(equipo, many=True)
        return Response(equipo_serializers.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        # Extraer el ID del torneo de los datos recibidos
        torneo_id = request.data.get('torneo_id')

        # Validar que se envíe el torneo_id
        if not torneo_id:
            return Response({'error': 'Debe enviar el torneo_id'}, status=status.HTTP_400_BAD_REQUEST)

        # Verificar que el torneo existe en la base de datos
        try:
            torneo = Torneo.objects.get(id=torneo_id)
        except Torneo.DoesNotExist:
            return Response({'error': 'Torneo no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        # Crear el equipo con validación
        equipo_serializers = EquipoSerializer(data=request.data)
        if equipo_serializers.is_valid():
            equipo = equipo_serializers.save()

            # Crear la relación muchos a muchos entre equipo y torneo
            EquipoTorneo.objects.create(equipo=equipo, torneo=torneo)

            return Response({'message': f'Equipo registrado correctamente y vinculado al torneo {torneo.nombre}'}, status=status.HTTP_201_CREATED)

        return Response(equipo_serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def equipo_details_view(request,pk=None):
    """Vista API para operaciones específicas de un equipo por ID"""
    
    equipo_id = Equipo.objects.filter(id = pk).first()
    
    if equipo_id:
          
        if request.method == 'GET':
            # Obtener detalles del equipo específico
            equipo_serizers = EquipoSerializer(equipo_id)
            return Response(equipo_serizers.data, status = status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            # Actualizar equipo existente
            equipo_serizers = EquipoSerializer(equipo_id, data = request.data)
            if equipo_serizers.is_valid():
                equipo_serizers.save()
                return Response({'message':'Registro actualizado correctamente'}, status = status.HTTP_201_CREATED)
            return Response(equipo_serizers.errors)
        
        elif request.method == 'DELETE':
            # Eliminar equipo
            equipo_id.delete()
            return Response({'message':'Registro eliminado correctamente'})
    else:
        # Equipo no encontrado
        return Response({'Error':'Pagina no encontrada'}, status=status.HTTP_404_NOT_FOUND)