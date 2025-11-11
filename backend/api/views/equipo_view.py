from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from api.models.equipo import Equipo,EquipoTorneo
from api.models.torneo import Torneo
from api.serializers.equipo_serializer import EquipoSerializer
from rest_framework.pagination import PageNumberPagination
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# LISTAR Y CREAR EQUIPOS

@swagger_auto_schema(
    method='get',
    operation_summary="Listar Equipos",
    operation_description="Obtiene la lista completa de equipos registrados en el sistema.",
    responses={200: EquipoSerializer(many=True)},
    tags=['Equipo']
)
@swagger_auto_schema(
    method='post',
    operation_summary="Registrar un nuevo equipos",
    operation_description="Crea un nuevo equipos con la información enviada en el cuerpo de la solicitud.",
    request_body=EquipoSerializer,
    responses={
        201: openapi.Response("Equipo creado correctamente", EquipoSerializer),
        400: "Error en los datos enviados"
    },
    tags=['Equipo']
)
@api_view(['GET', 'POST'])
def equipo_api_view(request):
    """Vista API para listar todos los equipos (GET) y crear nuevos vinculados a torneos (POST)"""
    
    if request.method == 'GET':
        # Obtener todos los equipos y serializarlos
        equipo = Equipo.objects.all()
        equipo_serializers = EquipoSerializer(equipo, many=True)
        pagination_class = PageNumberPagination
        pagination_class.page_size = 2
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



# DETALLE, ACTUALIZACIÓN Y ELIMINACIÓN DE EQUIPOS

@swagger_auto_schema(
    methods=['get'],
    operation_summary="Consultar Equipo por ID",
    operation_description="Obtiene la información detallada de un equipo existente, especificando su ID en la URL.",
    responses={
        200: openapi.Response("Equipo encontrado", EquipoSerializer),
        404: "Equipo no encontrado"
    },
    manual_parameters=[
        openapi.Parameter(
            'pk',
            openapi.IN_PATH,
            description="ID del equipo a consultar",
            type=openapi.TYPE_INTEGER
        )
    ],
    tags=['Equipo']
)
@swagger_auto_schema(
    methods=['put'],
    operation_summary="Actualizar Equipo (PUT)",
    operation_description="Actualiza completamente la información de un equipo existente.",
    request_body=EquipoSerializer,
    responses={
        200: "Equipo actualizado correctamente",
        400: "Error en los datos enviados",
        404: "Equipo no encontrado"
    },
    tags=['Equipo']
)
@swagger_auto_schema(
    methods=['delete'],
    operation_summary="Eliminar Equipo",
    operation_description="Elimina un equipo existente identificado por su ID.",
    responses={
        200: "Equipo eliminado correctamente",
        404: "Equipo no encontrado"
    },
    tags=['Equipo']
)
@api_view(['GET','PUT','DELETE'])
def equipo_details_view(request,pk=None):
    """
    **Vista API** para operaciones específicas sobre un Equipo.

    - **GET**: Obtiene el detalle de un torneo específico.  
    - **PUT**: Actualiza completamente la información de un torneo.  
    - **PATCH**: Modifica parcialmente los campos de un torneo.  
    - **DELETE**: Elimina un torneo existente.  
    """
    
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


    
# Listamos los equipos por su torneo

@swagger_auto_schema(
    method='get',
    operation_summary="Listar los equipos de un torneo especifico",
    operation_description="Obtiene la información detallada de los equipos existente en ese torneo, especificando el ID del torneo en la URL.",
    responses={
        200: openapi.Response("Equipos encontrados", EquipoSerializer),
        404: "Equipos no encontrados"
    },
    manual_parameters=[
        openapi.Parameter(
            'pk',
            openapi.IN_PATH,
            description="ID del torneo a consultar",
            type=openapi.TYPE_INTEGER
        )
    ],
    tags=['Equipo']
)
@api_view(['GET'])
def equipos_por_torneo(request, pk=None):
    """Lista los equipos asociados a un torneo específico"""
    
    if request.method == 'GET':
        try:
            # Verificamos que el torneo exista
            torneo = Torneo.objects.get(id=pk)
        except Torneo.DoesNotExist:
            return Response({'error': 'Torneo no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        # Obtenemos las relaciones equipo-torneo
        equipos_relacionados = EquipoTorneo.objects.filter(torneo=torneo).select_related('equipo')
        
        # Extraemos los equipos directamente
        equipos = [rel.equipo for rel in equipos_relacionados]
        
        # Serializamos los equipos
        serializer = EquipoSerializer(equipos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'Error':'Pagina no encontrada'}, status=status.HTTP_404_NOT_FOUND)
