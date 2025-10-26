<script setup>
import { ref, onMounted } from "vue";
import ShowEquipos from "./ShowEquipos.vue";
import ShowJugadores from "./ShowJugadores.vue";


const torneos = ref([]);
const equipos = ref([]);
const loading = ref(true);
const error = ref(null);

onMounted(async () => {
  try {
    const res = await fetch("http://127.0.0.1:8000/api/torneos/");
    if (!res.ok) throw new Error(`Error HTTP: ${res.status}`);
    const data = await res.json();
    torneos.value = data;
  } catch (err) {
    console.error("Error al traer torneos:", err);
    error.value = err.message;
  } finally {
    loading.value = false;
  }
});

const torneoSeleccionado = ref(null)
const paso = equipos // vista por defecto

function seleccionarTorneo(torneo) {
  torneoSeleccionado.value = torneo
}

</script>

<template>
  <section class="mb-4">
    <!-- Si no hay torneo seleccionado mostramos la tabla -->
    <div v-if="!torneoSeleccionado">
      <!-- Estados -->
      <p v-if="loading" class="text-center text-gray-500">Cargando torneos...</p>
      <p v-else-if="error" class="text-center text-red-500">Error: {{ error }}</p>
      <p v-else-if="torneos.length === 0" class="text-center text-gray-500">
        No hay torneos disponibles
      </p>
      <div class="bg-white/60 rounded-2xl mb-5 shadow-md 
         dark:bg-[rgba(30,41,59,0.5)] 
         backdrop-blur-[10px] 
         border border-[rgba(148,163,184,0.1)] 
         p-6">
        <h2 class="text-gray-800 dark:text-white text-[20px] mb-5 font-semibold">
          Lista de Torneos
        </h2>

        <table class="w-full text-left border-collapse">
          <thead class="bg-white/60 text-gray-700 
             dark:bg-[rgba(99,102,241,0.1)]">
            <tr>
              <th class="p-4 text-purple-600 font-semibold text-sm uppercase tracking-wide">Nombre</th>
              <th class="p-4 text-purple-600 font-semibold text-sm uppercase tracking-wide">Descripción</th>
              <th class="p-4 text-purple-600 font-semibold text-sm uppercase tracking-wide">Fecha Inicio</th>
              <th class="p-4 text-purple-600 font-semibold text-sm uppercase tracking-wide">Fecha Fin</th>
              <th class="p-4 text-purple-600 font-semibold text-sm uppercase tracking-wide">Organizador</th>
              <th class="p-4 text-purple-600 font-semibold text-sm uppercase tracking-wide">Estado</th>
            </tr>
          </thead>

          <tbody>
            <tr v-for="torneo in torneos" :key="torneo.id" class="border-t border-[rgba(148,163,184,0.1)] 
               hover:bg-[rgba(99,102,241,0.05)] 
               transition-colors duration-200">
              <td class="text-gray-900 dark:text-slate-300 p-4"><a @click="seleccionarTorneo(torneo)">{{ torneo.nombre
              }}</a></td>
              <td class="text-gray-900 dark:text-slate-300 p-4">{{ torneo.descripcion }}</td>
              <td class="text-gray-900 dark:text-slate-300 p-4">{{ torneo.fecha_inicio }}</td>
              <td class="text-gray-900 dark:text-slate-300 p-4">{{ torneo.fecha_fin }}</td>
              <td class="text-gray-900 dark:text-slate-300 p-4">{{ torneo.organizador }}</td>
              <td class="p-4 font-bold" :class="torneo.activo ? 'text-green-500' : 'text-red-500'">
                {{ torneo.activo ? 'Activo' : 'Inactivo' }}
              </td>
            </tr>
          </tbody>
        </table>


      </div>
    </div>

    <!-- Si hay torneo seleccionado, muestra su gestión -->
    <div v-else>
      <button @click="torneoSeleccionado = null" class="bg-gray-500 text-white px-3 py-1 rounded mb-4">
        ← Volver a torneos
      </button>

      <h2 class="text-2xl font-semibold mb-4">
        Gestionando: {{ torneoSeleccionado.nombre }}
      </h2>

      <!-- Menú de pasos -->
      <div class="flex space-x-3 mb-5">
        <button @click="paso = 'equipos'" :class="[
          'px-4 py-2 rounded-lg',
          paso === 'equipos' ? 'bg-blue-600 text-white' : 'bg-gray-200 dark:bg-gray-700 text-gray-800 dark:text-gray-200'
        ]">
          Equipos
        </button>
        <button @click="paso = 'jugadores'" :class="[
          'px-4 py-2 rounded-lg',
          paso === 'jugadores' ? 'bg-blue-600 text-white' : 'bg-gray-200 dark:bg-gray-700 text-gray-200'
        ]">
          Jugadores
        </button>
        <button @click="paso = 'formato'" :class="[
          'px-4 py-2 rounded-lg',
          paso === 'formato' ? 'bg-blue-600 text-white' : 'bg-gray-200 dark:bg-gray-700 text-gray-200'
        ]">
          Formato
        </button>
      </div>

      <!-- Vistas dinámicas -->
      <div class="bg-white dark:bg-slate-800 p-6 rounded-xl shadow-md">
        <div v-if="paso === 'equipos'">
          <ShowEquipos :torneo-id="torneoSeleccionado.id" />
        </div>

        <div v-else-if="paso === 'jugadores'">
          <ShowJugadores :torneo-id="torneoSeleccionado" />
        </div>

        <div v-else-if="paso === 'formato'">
          <p>Aquí irá la configuración del formato del torneo.</p>
        </div>
      </div>
    </div>


  </section>
 
</template>
