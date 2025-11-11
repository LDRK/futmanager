from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from api.models.estadisticas import EstadisticaJugador, EstadisticaEquipo
from api.serializers.estadisticas_serializers import EstadisticasJugadorSerializer, EstadisticasEquipoSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# LISTAR Y CREAR ESTADISTICAS DE LOS JUGADORES

@swagger_auto_schema(
    method='get',
    operation_summary="Listar Estadisticas",
    operation_description="Obtiene la lista completa de las estadisticas registradas en el sistema.",
    responses={200: EstadisticasJugadorSerializer(many=True)},
    tags=['Estadisticas']
)
@swagger_auto_schema(
    method='post',
    operation_summary="Registrar una nueva estadistica",
    operation_description="Crea una nueva estafistica al jugador con la información enviada en el cuerpo de la solicitud.",
    request_body=EstadisticasJugadorSerializer,
    responses={
        201: openapi.Response("Estadistica creada correctamente", EstadisticasJugadorSerializer),
        400: "Error en los datos enviados"
    },
    tags=['Estadisticas']
)

@api_view(['GET','POST'])
def estadisticas_jugador_list(request):
    """ Vista API para listar todas las estadisticas (GET) y las registramos (POST)"""
    
    if request.method == 'GET':
        # Obtenemos todos las estadisticas serializadas
        statsJugador = EstadisticaJugador.objects.all()
        statsJugador_serializer = EstadisticasJugadorSerializer(statsJugador, many=True)
        return Response(statsJugador_serializer.data, status=status.HTTP_200_OK)
    
    # Registramos las estadisticas del jugador
    elif request.method == 'POST':
        statsJugador_serializer = EstadisticasJugadorSerializer(data=request.data)
        if statsJugador_serializer.is_valid():
            statsJugador_serializer.save()
            return Response({'message': 'Estadistica creada correctamente'}, status=status.HTTP_201_CREATED)
        return Response(statsJugador_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# DETALLE, ACTUALIZACIÓN DE LAS ESTADISTICA DEL JUGADOR

@swagger_auto_schema(
    methods=['get'],
    operation_summary="Listamos las estadisticas del jugador por ID",
    operation_description="Obtiene la información detallada de las estadisticas del jugador, especificando su ID en la URL.",
    responses={
        200: openapi.Response("Estadistica encontrado", EstadisticasJugadorSerializer),
        404: "Estadistica no encontrado"
    },
    manual_parameters=[
        openapi.Parameter(
            'pk',
            openapi.IN_PATH,
            description="ID del jugador a consultar",
            type=openapi.TYPE_INTEGER
        )
    ],
    tags=['Estadisticas']
)
@swagger_auto_schema(
    methods=['patch'],
    operation_summary="Actualizar parcialmente Estadistica (PATCH)",
    operation_description="Actualiza algunos campos de las estadisticas especificado.",
    request_body=EstadisticasJugadorSerializer,
    responses={
        200: "Estaditica actualizada parcialmente",
        400: "Error en los datos enviados",
        404: "Estadistica no encontrada"
    },
    tags=['Estadisticas']
)
@api_view(['GET','PATCH'])
def estadisticas_jugador_details(request,pk=None):
    """ Vista API para operaciones especificas de las estadisticas por ID"""
    
    estadisticaJugador_id = EstadisticaJugador.objects.filter(id = pk).first()
    
    if estadisticaJugador_id:   
        if request.method == 'GET':
            # Obtenemos el id del jugador especifico
            statsJugador_serializer = EstadisticasJugadorSerializer(estadisticaJugador_id)
            return Response(statsJugador_serializer.data, status=status.HTTP_200_OK)
        
        elif request.method == 'PATCH':
            # Actualizamos la estadistica del jugador
            statsJugador_serializer = EstadisticasJugadorSerializer(estadisticaJugador_id, data=request.data, partial=True)
            if statsJugador_serializer.is_valid():
                statsJugador_serializer.save()
                return Response({'message':'Registro actualizado correctamente'}, status = status.HTTP_201_CREATED)
            return Response(statsJugador_serializer.errors)
        

# LISTAR Y CREAR ESTADISTICAS DE LOS EQUIPOS

@swagger_auto_schema(
    method='get',
    operation_summary="Listar Estadisticas",
    operation_description="Obtiene la lista completa de las estadisticas registradas en el sistema.",
    responses={200: EstadisticasEquipoSerializer(many=True)},
    tags=['Estadisticas']
)
@swagger_auto_schema(
    method='post',
    operation_summary="Registrar una nueva estadistica",
    operation_description="Crea una nueva estadistica al equipo con la información enviada en el cuerpo de la solicitud.",
    request_body=EstadisticasEquipoSerializer,
    responses={
        201: openapi.Response("Estadistica creada correctamente", EstadisticasJugadorSerializer),
        400: "Error en los datos enviados"
    },
    tags=['Estadisticas']
)

@api_view(['GET','POST'])
def estadisticas_equipo_list(request):
    """ Vista API para listar todas las estadisticas (GET) y las registramos (POST)"""

    if request.method == 'GET':
        # Obtenemos todos las estadisticas serializadas
        statsEquipo = EstadisticaEquipo.objects.all()
        statsEquipo_serializer = EstadisticasEquipoSerializer(statsEquipo, many=True)
        return Response( statsEquipo_serializer.data, status=status.HTTP_200_OK)
    
    # Registramos las estadisticas del jugador
    elif request.method == 'POST':
        statsEquipo_serializer = EstadisticasEquipoSerializer(data=request.data)
        if statsEquipo_serializer.is_valid():
            statsEquipo_serializer.save()
            return Response({'message': 'Estadistica creada correctamente'}, status=status.HTTP_201_CREATED)
        return Response(  statsEquipo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# LISTAR Y CREAR ESTADISTICAS DE LOS EQUIPOS

@swagger_auto_schema(
    method='get',
    operation_summary="Listar Estadisticas",
    operation_description="Obtiene la lista completa de las estadisticas registradas en el sistema.",
    responses={200: EstadisticasEquipoSerializer(many=True)},
    tags=['Estadisticas']
)
@swagger_auto_schema(
    method='patch',
    operation_summary="Actualizar parcialmente la estadistica (PATCH)",
    operation_description="Actualiza algunos campos de la estadistica especificada.",
    request_body=EstadisticasEquipoSerializer,
    responses={
        200: "Estadistica actualizada parcialmente",
        400: "Error en los datos enviados",
        404: "Estadistica no encontrado"
    },
    tags=['Estadisticas']
)
@api_view(['GET','PATCH'])
def estadisticas_equipo_details(request,pk=None):
    """ Vista API para operaciones especificas de las estadisticas por ID"""
    
    estadisticaEquipo_id = EstadisticaEquipo.objects.filter(id = pk).first()
    
    if estadisticaEquipo_id:   
        if request.method == 'GET':
            # Obtenemos el id del Equipo especifico
            statsEquipo_serializer = EstadisticasEquipoSerializer(estadisticaEquipo_id)
            return Response( statsEquipo_serializer.data, status=status.HTTP_200_OK)
        
        elif request.method == 'PATCH':
            # Actualizamos la estadistica del equipo
            statsEquipo_serializer = EstadisticasEquipoSerializer(estadisticaEquipo_id, data=request.data, partial=True)
            if  statsEquipo_serializer.is_valid():
                statsEquipo_serializer.save()
                return Response({'message':'Registro actualizado correctamente'}, status = status.HTTP_201_CREATED)
            return Response( statsEquipo_serializer.errors)