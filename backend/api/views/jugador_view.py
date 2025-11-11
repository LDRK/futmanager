from rest_framework import status
from rest_framework.response import Response
from api.models.jugador import Jugador
from rest_framework.decorators import api_view
from api.serializers.jugador_serializer import JugadorSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# LISTAR Y CREAR EQUIPOS

@swagger_auto_schema(
    method='get',
    operation_summary="Listar Juadores",
    operation_description="Obtiene la lista completa de jugadores registrados en el sistema.",
    responses={200: JugadorSerializer(many=True)},
    tags=['Jugador']
)
@swagger_auto_schema(
    method='post',
    operation_summary="Registrar un nuevo jugador",
    operation_description="Crea un nuevo jugador con la información enviada en el cuerpo de la solicitud.",
    request_body=JugadorSerializer,
    responses={
        201: openapi.Response("Jugador creado correctamente", JugadorSerializer),
        400: "Error en los datos enviados"
    },
    tags=['Jugador']
)
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


# DETALLE, ACTUALIZACIÓN Y ELIMINACIÓN DE JUGADOR

@swagger_auto_schema(
    methods=['get'],
    operation_summary="Consultar Jugador por ID",
    operation_description="Obtiene la información detallada de un jugador existente, especificando su ID en la URL.",
    responses={
        200: openapi.Response("Jugador encontrado", JugadorSerializer),
        404: "Jugador no encontrado"
    },
    manual_parameters=[
        openapi.Parameter(
            'pk',
            openapi.IN_PATH,
            description="ID del jugador a consultar",
            type=openapi.TYPE_INTEGER
        )
    ],
    tags=['Jugador']
)
@swagger_auto_schema(
    methods=['put'],
    operation_summary="Actualizar Jugador (PUT)",
    operation_description="Actualiza completamente la información de un jugador existente.",
    request_body=JugadorSerializer,
    responses={
        200: "Jugador actualizado correctamente",
        400: "Error en los datos enviados",
        404: "Jugador no encontrado"
    },
    tags=['Jugador']
)
@swagger_auto_schema(
    methods=['delete'],
    operation_summary="Eliminar Jugador",
    operation_description="Elimina un jugador existente identificado por su ID.",
    responses={
        200: "Jugador eliminado correctamente",
        404: "Jugador no encontrado"
    },
    tags=['Jugador']
)
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
    
# Listamos los jugadores por su equipo
@swagger_auto_schema(
    methods=['get'],
    operation_summary="Listar Jugadores por equipo",
    operation_description="Obtiene la información detallada de los jugadores existente de cada equipo, especificando el ID del equipo en la URL.",
    responses={
        200: openapi.Response("Jugadores encontrados", JugadorSerializer),
        404: "Jugadores no encontrados"
    },
    manual_parameters=[
        openapi.Parameter(
            'pk',
            openapi.IN_PATH,
            description="ID del equipo a consultar",
            type=openapi.TYPE_INTEGER
        )
    ],
    tags=['Jugador']
)
@api_view(['GET'])
def jugadores_por_equipo(request, pk=None):
    """Lista los Jugadores asociados a un Equipo específico"""
    
    if request.method == 'GET':
        jugadores = Jugador.objects.filter(equipo_id=pk)
        serializer = JugadorSerializer(jugadores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'Error':'Pagina no encontrada'}, status=status.HTTP_404_NOT_FOUND)
