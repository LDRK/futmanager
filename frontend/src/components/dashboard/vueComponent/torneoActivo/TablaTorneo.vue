<script setup>
import { ref, onMounted } from 'vue';

const props = defineProps({
  torneoId: {
    type: Number,
    required: true
  }
});

const estadisticas = ref([]);
const torneoNombre = ref('');
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
    
    console.log('Data recibida:', data);
    
    // Extraer el nombre del torneo y las estadísticas
    torneoNombre.value = data.torneo || '';
    
    // Las estadísticas están en "estadisticas_equipos"
    const stats = data.estadisticas_equipos || [];
    
    if (stats.length === 0) {
      console.warn('⚠️ No hay estadísticas para este torneo');
      estadisticas.value = [];
      return;
    }
    
    console.log('📊 Estadísticas encontradas:', stats.length);
    
    // Ordenar por puntos, diferencia de goles y goles a favor
    estadisticas.value = stats.sort((a, b) => {
      if (b.puntos !== a.puntos) return b.puntos - a.puntos;
      if (b.diferencia_goles !== a.diferencia_goles) return b.diferencia_goles - a.diferencia_goles;
      return b.goles_a_favor - a.goles_a_favor;
    });
    
  } catch (err) {
    console.error('Error al cargar estadísticas:', err);
    error.value = err.message;
  } finally {
    loading.value = false;
  }
};

const getPositionClass = (position) => {
  if (position <= 3) return 'bg-green-500 text-white';
  if (position <= 6) return 'bg-yellow-500 text-white';
  if (position >= estadisticas.value.length - 2 && estadisticas.value.length > 8) {
    return 'bg-red-500 text-white';
  }
  return 'bg-slate-600 text-gray-300';
};

const getDifferenceClass = (difference) => {
  if (difference > 0) return 'text-green-400';
  if (difference < 0) return 'text-red-400';
  return 'text-gray-400';
};

// Exponer función para recargar
defineExpose({
  cargarEstadisticas
});
</script>

<template>
  <div>
    <div class="flex items-center justify-between mb-6">
      <h2 class="text-2xl font-bold text-gray-800 dark:text-white">
        Tabla de Posiciones
        <span v-if="torneoNombre" class="text-purple-600 dark:text-purple-400"> - {{ torneoNombre }}</span>
      </h2>
    </div>
    
    <!-- Estados de carga -->
    <div v-if="loading" class="text-center py-8">
      <p class="text-gray-500 dark:text-gray-400">Cargando estadísticas...</p>
    </div>
    
    <div v-else-if="error" class="text-center py-8">
      <p class="text-red-500">Error: {{ error }}</p>
    </div>
    
    <div v-else-if="estadisticas.length === 0" class="text-center py-8">
      <p class="text-gray-500 dark:text-gray-400">No hay estadísticas disponibles para este torneo</p>
    </div>
    
    <div v-else class="overflow-x-auto bg-white/60 dark:bg-slate-800/50 rounded-lg shadow-md">
      <table class="w-full">
        <thead>
          <tr class="text-left border-b border-slate-300 dark:border-slate-600">
            <th class="pb-3 px-4 text-purple-600 dark:text-purple-400 font-semibold">#</th>
            <th class="pb-3 px-4 text-purple-600 dark:text-purple-400 font-semibold">Equipo</th>
            <th class="pb-3 px-4 text-center text-purple-600 dark:text-purple-400 font-semibold">PJ</th>
            <th class="pb-3 px-4 text-center text-purple-600 dark:text-purple-400 font-semibold">PG</th>
            <th class="pb-3 px-4 text-center text-purple-600 dark:text-purple-400 font-semibold">PE</th>
            <th class="pb-3 px-4 text-center text-purple-600 dark:text-purple-400 font-semibold">PP</th>
            <th class="pb-3 px-4 text-center text-purple-600 dark:text-purple-400 font-semibold">GF</th>
            <th class="pb-3 px-4 text-center text-purple-600 dark:text-purple-400 font-semibold">GC</th>
            <th class="pb-3 px-4 text-center text-purple-600 dark:text-purple-400 font-semibold">DG</th>
            <th class="pb-3 px-4 text-center text-purple-600 dark:text-purple-400 font-semibold">PTS</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="(team, index) in estadisticas"
            :key="team.id"
            class="border-b border-slate-300 dark:border-slate-700 hover:bg-purple-50 dark:hover:bg-slate-700/50 transition-colors duration-200"
          >
            <td class="py-4 px-4">
              <span 
                :class="[
                  'inline-flex items-center justify-center w-8 h-8 rounded-lg font-bold',
                  getPositionClass(index + 1)
                ]"
              >
                {{ index + 1 }}
              </span>
            </td>
            <td class="py-4 px-4 font-semibold text-gray-900 dark:text-white">
              {{ team.equipo || 'Sin nombre' }}
            </td>
            <td class="py-4 px-4 text-center text-gray-700 dark:text-gray-300">{{ team.partidos_jugados }}</td>
            <td class="py-4 px-4 text-center text-gray-700 dark:text-gray-300">{{ team.partidos_ganados }}</td>
            <td class="py-4 px-4 text-center text-gray-700 dark:text-gray-300">{{ team.partidos_empatados }}</td>
            <td class="py-4 px-4 text-center text-gray-700 dark:text-gray-300">{{ team.partidos_perdidos }}</td>
            <td class="py-4 px-4 text-center text-gray-700 dark:text-gray-300">{{ team.goles_a_favor }}</td>
            <td class="py-4 px-4 text-center text-gray-700 dark:text-gray-300">{{ team.goles_en_contra }}</td>
            <td class="py-4 px-4 text-center">
              <span :class="getDifferenceClass(team.diferencia_goles)">
                {{ team.diferencia_goles > 0 ? '+' : '' }}{{ team.diferencia_goles }}
              </span>
            </td>
            <td class="py-4 px-4 text-center font-bold text-lg text-gray-900 dark:text-white">
              {{ team.puntos }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Leyenda -->
    <div class="mt-6 flex gap-4 flex-wrap text-sm">
      <div class="flex items-center gap-2">
        <span class="w-4 h-4 bg-green-500 rounded"></span>
        <span class="text-gray-600 dark:text-gray-400">Clasificación directa (Top 3)</span>
      </div>
      <div class="flex items-center gap-2">
        <span class="w-4 h-4 bg-yellow-500 rounded"></span>
        <span class="text-gray-600 dark:text-gray-400">Repechaje (4-6)</span>
      </div>
      <div class="flex items-center gap-2">
        <span class="w-4 h-4 bg-red-500 rounded"></span>
        <span class="text-gray-600 dark:text-gray-400">Zona de descenso</span>
      </div>
    </div>
  </div>
</template>