<script setup>
import { ref, onMounted, computed } from 'vue';

const props = defineProps({
  torneoId: {
    type: Number,
    required: true
  }
});

const goleadores = ref([]);
const estadisticasJugadores = ref([]);
const estadisticasEquipos = ref([]);
const loading = ref(true);
const error = ref(null);

onMounted(async () => {
  await cargarEstadisticas();
});

const cargarEstadisticas = async () => {
  try {
    const res = await fetch(`http://127.0.0.1:8000/api/estadisticas-torneo/torneo/${props.torneoId}/`);
    if (!res.ok) throw new Error(`Error HTTP: ${res.status}`);
    const data = await res.json();
    
    console.log('Estadísticas recibidas:', data);
    
    // Guardar datos
    estadisticasJugadores.value = data.estadisticas_jugadores || [];
    estadisticasEquipos.value = data.estadisticas_equipos || [];
    
    // Procesar goleadores (ordenar por goles descendente, mostrar top 5)
    goleadores.value = [...estadisticasJugadores.value]
      .sort((a, b) => b.goles - a.goles)
      .slice(0, 5)
      .filter(j => j.goles > 0); // Solo mostrar jugadores con al menos 1 gol
    
  } catch (err) {
    console.error('Error al cargar estadísticas:', err);
    error.value = err.message;
  } finally {
    loading.value = false;
  }
};

// Computed properties para las estadísticas generales
const totalGoles = computed(() => {
  return estadisticasEquipos.value.reduce((sum, equipo) => sum + equipo.goles_a_favor, 0);
});

const totalPartidos = computed(() => {
  // Suma todos los partidos jugados y divide entre 2 (porque cada partido cuenta 2 veces)
  const suma = estadisticasEquipos.value.reduce((sum, equipo) => sum + equipo.partidos_jugados, 0);
  return Math.floor(suma / 2);
});

const promedioGoles = computed(() => {
  if (totalPartidos.value === 0) return '0.0';
  return (totalGoles.value / totalPartidos.value).toFixed(1);
});

const totalAmarillas = computed(() => {
  return estadisticasJugadores.value.reduce((sum, jugador) => sum + jugador.amarillas, 0);
});

const totalRojas = computed(() => {
  return estadisticasJugadores.value.reduce((sum, jugador) => sum + jugador.rojas, 0);
});

// Exponer función para recargar
defineExpose({
  cargarEstadisticas
});
</script>
<template>
  <div>
    <h2 class="text-2xl font-bold mb-6 text-gray-800 dark:text-white">Estadísticas del Torneo</h2>
    
    <!-- Estados de carga -->
    <div v-if="loading" class="text-center py-8">
      <p class="text-gray-500 dark:text-gray-400">Cargando estadísticas...</p>
    </div>
    
    <div v-else-if="error" class="text-center py-8">
      <p class="text-red-500">Error: {{ error }}</p>
    </div>
    
    <div v-else class="grid grid-cols-1 lg:grid-cols-2 gap-6">
      <!-- Goleadores -->
      <div class="bg-white/60 dark:bg-slate-700/50 rounded-xl p-6 shadow-md">
        <h3 class="text-xl font-bold mb-4 flex items-center gap-2 text-gray-800 dark:text-white">
          ⚽ Máximos Goleadores
        </h3>
        <div v-if="goleadores.length === 0" class="text-center py-4">
          <p class="text-gray-500 dark:text-gray-400">No hay goleadores registrados</p>
        </div>
        <div v-else class="space-y-3">
          <div
            v-for="(jugador, index) in goleadores"
            :key="jugador.id"
            class="flex items-center justify-between p-3 bg-slate-100 dark:bg-slate-800 rounded-lg hover:bg-slate-200 dark:hover:bg-slate-750 transition-colors duration-200"
          >
            <div class="flex items-center gap-3">
              <span 
                :class="[
                  'text-2xl font-bold',
                  index === 0 ? 'text-yellow-500' : index === 1 ? 'text-gray-400' : index === 2 ? 'text-orange-600' : 'text-gray-500'
                ]"
              >
                {{ index + 1 }}
              </span>
              <div>
                <p class="font-semibold text-gray-900 dark:text-white">{{ jugador.jugador }}</p>
                <p class="text-sm text-gray-600 dark:text-gray-400">{{ jugador.equipo }}</p>
              </div>
            </div>
            <span class="text-2xl font-bold text-orange-500">{{ jugador.goles }}</span>
          </div>
        </div>
      </div>

      <!-- Stats Generales -->
      <div class="bg-white/60 dark:bg-slate-700/50 rounded-xl p-6 shadow-md">
        <h3 class="text-xl font-bold mb-4 text-gray-800 dark:text-white">📊 Estadísticas Generales</h3>
        <div class="space-y-4">
          <div class="p-4 bg-slate-100 dark:bg-slate-800 rounded-lg hover:bg-slate-200 dark:hover:bg-slate-750 transition-colors duration-200">
            <p class="text-gray-600 dark:text-gray-400 text-sm mb-1">Promedio de goles por partido</p>
            <p class="text-3xl font-bold text-green-500">{{ promedioGoles }}</p>
          </div>
          <div class="p-4 bg-slate-100 dark:bg-slate-800 rounded-lg hover:bg-slate-200 dark:hover:bg-slate-750 transition-colors duration-200">
            <p class="text-gray-600 dark:text-gray-400 text-sm mb-1">Total de goles</p>
            <p class="text-3xl font-bold text-blue-500">{{ totalGoles }}</p>
          </div>
          <div class="flex gap-4">
            <div class="flex-1 p-4 bg-slate-100 dark:bg-slate-800 rounded-lg hover:bg-slate-200 dark:hover:bg-slate-750 transition-colors duration-200">
              <p class="text-gray-600 dark:text-gray-400 text-sm mb-1">🟨 Amarillas</p>
              <p class="text-2xl font-bold text-gray-900 dark:text-white">{{ totalAmarillas }}</p>
            </div>
            <div class="flex-1 p-4 bg-slate-100 dark:bg-slate-800 rounded-lg hover:bg-slate-200 dark:hover:bg-slate-750 transition-colors duration-200">
              <p class="text-gray-600 dark:text-gray-400 text-sm mb-1">🟥 Rojas</p>
              <p class="text-2xl font-bold text-gray-900 dark:text-white">{{ totalRojas }}</p>
            </div>
          </div>
          <div class="p-4 bg-slate-100 dark:bg-slate-800 rounded-lg hover:bg-slate-200 dark:hover:bg-slate-750 transition-colors duration-200">
            <p class="text-gray-600 dark:text-gray-400 text-sm mb-1">Total de partidos jugados</p>
            <p class="text-3xl font-bold text-purple-500">{{ totalPartidos }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

