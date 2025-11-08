import random
import math
 
# 🔹 --- ALGORITMOS DE GENERACIÓN DE FIXTURE --- 🔹

def fixture_todos_contra_todos(equipos):
    """
    Genera un fixture todos contra todos.
    Retorna una lista de jornadas, donde cada jornada es una lista de tuplas (local, visitante).
    """
    equipos = list(equipos)
    if len(equipos) % 2 != 0:
        equipos.append(None)  # Si hay número impar, agregamos un "bye"

    n = len(equipos)
    fixture = []

    for i in range(n - 1):
        jornada = []
        for j in range(n // 2):
            local = equipos[j]
            visitante = equipos[n - 1 - j]
            if local and visitante:  # Evitamos Nones
                jornada.append((local, visitante))
        fixture.append(jornada)
        equipos.insert(1, equipos.pop())  # Rotamos los equipos

    return fixture


def fixture_eliminacion(equipos):
    """Empareja equipos de forma aleatoria tipo knockout"""
    random.shuffle(equipos)
    rondas = []
    total = len(equipos)
    prox_potencia = 2 ** math.ceil(math.log2(total))
    byes = prox_potencia - total

    primera_ronda = []
    i = 0
    while i < len(equipos):
        if byes > 0:
            primera_ronda.append((equipos[i], None))
            byes -= 1
            i += 1
        else:
            primera_ronda.append((equipos[i], equipos[i + 1]))
            i += 2
    rondas.append(primera_ronda)
    return rondas


def fixture_por_grupos(equipos, num_grupos=2):
    """Divide equipos en grupos y genera fixture interno"""
    grupos = {f"Grupo {chr(65 + i)}": [] for i in range(num_grupos)}

    for i, equipo in enumerate(equipos):
        grupos[f"Grupo {chr(65 + (i % num_grupos))}"].append(equipo)

    fixture_grupos = {}
    for nombre, lista in grupos.items():
        fixture_grupos[nombre] = fixture_todos_contra_todos(lista)

    return fixture_grupos