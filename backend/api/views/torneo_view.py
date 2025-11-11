from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from api.models.torneo import Torneo
from api.serializers.torneo_serializer import TorneoSerializer
from api.models.torneo import generar_fixture
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# LISTAR Y CREAR TORNEOS

@swagger_auto_schema(
    method='get',
    operation_summary="Listar Torneos",
    operation_description="Obtiene la lista completa de torneos registrados en el sistema.",
    responses={200: TorneoSerializer(many=True)},
    tags=['Torneos']
)
@swagger_auto_schema(
    method='post',
    operation_summary="Registrar un nuevo Torneo",
    operation_description="Crea un nuevo torneo con la información enviada en el cuerpo de la solicitud.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'nombre': openapi.Schema(type=openapi.TYPE_STRING, example='Champions League'),
            'descripcion': openapi.Schema(type=openapi.TYPE_STRING, example='Torneo de clubes europeos'),
            'fecha_inicio': openapi.Schema(type=openapi.TYPE_STRING, example='2025-09-25'),
            'fecha_fin': openapi.Schema(type=openapi.TYPE_STRING, example='2025-12-25'),
            'organizador': openapi.Schema(type=openapi.TYPE_STRING, example='1'),  # ID del usuario organizador
        },
        required=['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin', 'organizador'],
    ),
    responses={
        201: openapi.Response(
            description="Torneo creado correctamente",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
                    'nombre': openapi.Schema(type=openapi.TYPE_STRING, example='Copa Montería 2025'),
                    'descripcion': openapi.Schema(type=openapi.TYPE_STRING, example='Torneo de clubes europeos'),
                    'fecha_inicio': openapi.Schema(type=openapi.TYPE_STRING, example='2025-09-25'),
                    'fecha_fin': openapi.Schema(type=openapi.TYPE_STRING, example='2025-12-25'),
                    'organizador': openapi.Schema(type=openapi.TYPE_STRING, example='Leonardo'),
                    'activo': openapi.Schema(type=openapi.TYPE_BOOLEAN, example=True),
                    'estado': openapi.Schema(type=openapi.TYPE_STRING, example='activo'),
                    'formato': openapi.Schema(type=openapi.TYPE_STRING, example='eliminacion'),
                }
            ),
            examples={
                "application/json": {
                    "id": 1,
                    "nombre": "Copa Montería 2025",
                    "descripcion": "Torneo de clubes europeos",
                    "fecha_inicio": "2025-09-25",
                    "fecha_fin": "2025-12-25",
                    "organizador": "Leonardo",
                    "activo": True,
                    "estado": "activo",
                    "formato": "eliminacion"
                }
            }
        ),
        400: openapi.Response(
            description="Error en los datos enviados",
            examples={
                "application/json": {
                    "error": "El campo 'nombre' es obligatorio."
                }
            }
        )
    },
    tags=['Torneos']
)

@api_view(['GET', 'POST'])
def torneo_view(request):
    """
    **Vista API** para:
    - `GET`: Listar todos los torneos registrados.
    - `POST`: Crear un nuevo torneo.
    """
    if request.method == 'GET':
        torneos = Torneo.objects.all()
        serializer = TorneoSerializer(torneos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = TorneoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Torneo creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# DETALLE, ACTUALIZACIÓN Y ELIMINACIÓN DE TORNEOS

@swagger_auto_schema(
    method='get',
    operation_summary="Consultar Torneo por ID",
    operation_description="Obtiene la información detallada de un torneo existente, especificando su ID en la URL.",
    responses={
        200: openapi.Response("Torneo encontrado", TorneoSerializer),
        404: "Torneo no encontrado"
    },
    manual_parameters=[
        openapi.Parameter(
            'pk',
            openapi.IN_PATH,
            description="ID del torneo a consultar",
            type=openapi.TYPE_INTEGER
        )
    ],
    tags=['Torneos']
)
@swagger_auto_schema(
    method='put',
    operation_summary="Actualizar Torneo (PUT)",
    operation_description="Actualiza completamente la información de un torneo existente.",
    request_body=TorneoSerializer,
    responses={
        200: "Torneo actualizado correctamente",
        400: "Error en los datos enviados",
        404: "Torneo no encontrado"
    },
    tags=['Torneos']
)
@swagger_auto_schema(
    method='patch',
    operation_summary="Actualizar parcialmente Torneo (PATCH)",
    operation_description="Actualiza algunos campos del torneo especificado.",
    request_body=TorneoSerializer,
    responses={
        200: "Torneo actualizado parcialmente",
        400: "Error en los datos enviados",
        404: "Torneo no encontrado"
    },
    tags=['Torneos']
)
@swagger_auto_schema(
    method='delete',
    operation_summary="Eliminar Torneo",
    operation_description="Elimina un torneo existente identificado por su ID.",
    responses={
        200: "Torneo eliminado correctamente",
        404: "Torneo no encontrado"
    },
    tags=['Torneos']
)
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def torneo_detail(request, pk=None):
    """
    **Vista API** para operaciones específicas sobre un Torneo.

    - **GET**: Obtiene el detalle de un torneo específico.  
    - **PUT**: Actualiza completamente la información de un torneo.  
    - **PATCH**: Modifica parcialmente los campos de un torneo.  
    - **DELETE**: Elimina un torneo existente.  
    """
    try:
        torneo = Torneo.objects.get(id=pk)
    except Torneo.DoesNotExist:
        return Response({'error': 'Torneo no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TorneoSerializer(torneo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method in ['PUT', 'PATCH']:
        serializer = TorneoSerializer(torneo, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registro actualizado correctamente'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        torneo.delete()
        return Response({'message': 'Registro eliminado correctamente'}, status=status.HTTP_200_OK)



# GENERAR FIXTURE DEL TORNEO

@swagger_auto_schema(
    method='post',
    operation_summary="Generar Fixture del Torneo",
    operation_description=(
        "Genera automáticamente el fixture (programación de partidos) "
        "para el torneo especificado. Si el fixture ya existe, se devuelve un error."
    ),
    manual_parameters=[
        openapi.Parameter(
            'pk',
            openapi.IN_PATH,
            description="ID del torneo para el cual se generará el fixture",
            type=openapi.TYPE_INTEGER
        )
    ],
    responses={
        200: "Fixture generado correctamente",
        400: "El fixture ya fue generado",
        404: "Torneo no encontrado"
    },
    tags=['Torneos']
)
@api_view(['POST'])
def generar_fixture_view(request, pk=None):
    """
    **Vista API** para generar el fixture (partidos) de un torneo existente.
    """
    try:
        torneo = Torneo.objects.get(pk=pk)
    except Torneo.DoesNotExist:
        return Response({'error': 'Torneo no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

    if torneo.partido_set.exists():
        return Response({'error': 'El fixture ya fue generado.'}, status=status.HTTP_400_BAD_REQUEST)

    generar_fixture(torneo)
    return Response({'message': 'Fixture generado correctamente.'}, status=status.HTTP_200_OK)
