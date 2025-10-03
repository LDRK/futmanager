from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from api.models.estadisticas import EstadisticaJugador, EstadisticaEquipo
from api.serializers.estadisticas_serializers import EstadisticasJugadorSerializer, EstadisticasEquipoSerializer


# Flujo de estadisticas para jugadores

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
            statsJugador_serializer = EstadisticasJugadorSerializer(estadisticaJugador_id, data=request.data)
            if statsJugador_serializer.is_valid():
                statsJugador_serializer.save()
                return Response({'message':'Registro actualizado correctamente'}, status = status.HTTP_201_CREATED)
            return Response(statsJugador_serializer.errors)
        

# Flujo de estadisticas para equipos

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
            statsEquipo_serializer = EstadisticasEquipoSerializer(estadisticaEquipo_id, data=request.data)
            if  statsEquipo_serializer.is_valid():
                statsEquipo_serializer.save()
                return Response({'message':'Registro actualizado correctamente'}, status = status.HTTP_201_CREATED)
            return Response( statsEquipo_serializer.errors)