from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from api.models.partido import Partido
from api.serializers.partido_serializer import PartidoSerializer
from rest_framework.pagination import PageNumberPagination
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# LISTAR Y CREAR PARTIDOS

@swagger_auto_schema(
    method='get',
    operation_summary="Listar Partidos",
    operation_description="Obtiene la lista completa de los partidos registrados en el sistema.",
    responses={200: PartidoSerializer(many=True)},
    tags=['Partidos']
)
@swagger_auto_schema(
    method='post',
    operation_summary="Registrar un nuevo equipos",
    operation_description="Crea un nuevo equipos con la información enviada en el cuerpo de la solicitud.",
    request_body=PartidoSerializer,
    responses={
        201: openapi.Response("Equipo creado correctamente", PartidoSerializer),
        400: "Error en los datos enviados"
    },
    tags=['Partidos']
)
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

# DETALLE, ACTUALIZACIÓN Y ELIMINACIÓN DE EQUIPOS

@swagger_auto_schema(
    methods=['get'],
    operation_summary="Consultar partido por ID",
    operation_description="Obtiene la información detallada de un partido existente, especificando su ID en la URL.",
    responses={
        200: openapi.Response("Partido encontrado", PartidoSerializer),
        404: "Partido no encontrado"
    },
    manual_parameters=[
        openapi.Parameter(
            'pk',
            openapi.IN_PATH,
            description="ID del Partido a consultar",
            type=openapi.TYPE_INTEGER
        )
    ],
    tags=['Partidos']
)
@swagger_auto_schema(
    methods=['patch'],
    operation_summary="Actualizar parcialmente Partido (PATCH)",
    operation_description="Actualiza algunos campos del partido especificado.",
    request_body=PartidoSerializer,
    responses={
        200: "Partido actualizado parcialmente",
        400: "Error en los datos enviados",
        404: "Partido no encontrado"
    },
    tags=['Partidos']
)
@swagger_auto_schema(
    methods=['delete'],
    operation_summary="Eliminar Partido",
    operation_description="Elimina un partido existente identificado por su ID.",
    responses={
        200: "Partido eliminado correctamente",
        404: "Partido no encontrado"
    },
    tags=['Partidos']
)
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

# Listar los partidos por torneo
@swagger_auto_schema(
    methods=['get'],
    operation_summary="Listar Partidos por Torneo",
    operation_description="Obtiene la información detallada de los partidos existente de cada torneo, especificando el ID del torneo en la URL.",
    responses={
        200: openapi.Response("Partidos encontrados", PartidoSerializer),
        404: "Partidos no encontrados"
    },
    manual_parameters=[
        openapi.Parameter(
            'pk',
            openapi.IN_PATH,
            description="ID del torneo a consultar",
            type=openapi.TYPE_INTEGER
        )
    ],
    tags=['Partidos']
)
@api_view(['GET'])
def partidos_por_torneo(request, pk):
    
    partidos = Partido.objects.filter(torneo_id=pk).order_by('id')
    
    # Creamos la instacion para la paginacion
    pagination_class = PageNumberPagination()
    pagination_class.page_size = 5
    
    # Aplicamos paginacion al queryset
    result_page = pagination_class.paginate_queryset(partidos, request)
    # serializer = PartidoSerializer(partidos, many=True)
    serializer = PartidoSerializer(result_page, many=True)
    
    
    return pagination_class.get_paginated_response(serializer.data)



        
    


















