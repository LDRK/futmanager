from django.urls import path
from api.views.torneo_view import torneo_view, torneo_detail, generar_fixture_view
from api.views.equipo_view import equipo_api_view, equipo_details_view, equipos_por_torneo
from api.views.jugador_view import jugador_api_view, jugador_details_view, jugadores_por_equipo
from api.views.partido_view import partido_api_view, partido_details_view, partidos_por_torneo
from api.views.estadisticas_view import estadisticas_jugador_list, estadisticas_jugador_details, estadisticas_equipo_list, estadisticas_equipo_details, estadisticas_por_torneo


urlpatterns = [
    # Torneo
    path('torneos/', torneo_view, name='torneo-list'),
    path('torneos/<int:pk>/', torneo_detail, name='torneo-detail'),
    path('torneos/<int:pk>/generar_fixture/', generar_fixture_view, name='generar_fixture'),
    
    # Equipo
    path('equipo/', equipo_api_view, name='equipo_api'),
    path('equipo/<int:pk>/', equipo_details_view, name='equipo_api_details'),
    path('equipo/torneo/<int:pk>/', equipos_por_torneo, name='equipos_por_torneo'),
    
    # Jugador
    path('jugador/', jugador_api_view, name='jugador_api'),
    path('jugador/<int:pk>/', jugador_details_view, name='jugador_api_details'),
    path('jugador/equipo/<int:pk>/', jugadores_por_equipo, name='jugadores_por_equipo'),
    
    # Partido
    path('partidos/', partido_api_view, name='partido-list'),
    path('partidos/<int:pk>/', partido_details_view, name='partido-details'),
    path('partidos/torneo/<int:pk>/', partidos_por_torneo, name='partidos_por_torneo'),

    
    # Estadisticas Jugador
    path('estadisticas-jugador/', estadisticas_jugador_list, name='estadisticasJugador-list'),
    path('estadisticas-jugador/<int:pk>/', estadisticas_jugador_details, name='estadisticasJugador-details'),
    
    
    
    # Estadisticas Equipo
    path('estadisticas-equipo/', estadisticas_equipo_list, name='estadisticasEquipo-list'),
    path('estadisticas-equipo/<int:pk>/', estadisticas_equipo_details, name='estadisticasEquipo-details'),
    
    # Estadisticas por torneo jugadores y equipo
    path('estadisticas-torneo/torneo/<int:pk>/', estadisticas_por_torneo, name='estadisticas-torneo')
]
