<script setup>
import { ref } from "vue";
import ShowEquipos from "./ShowEquipos.vue";
import ShowJugadores from "./ShowJugadores.vue";
import CardsFormatoTorneo from "./CardsFormatoTorneo.vue";

// Recibe el torneo seleccionado del padre
const props = defineProps({
  torneoSeleccionado: {
    type: Object,
    required: true
  }
});

// Controla el paso actual dentro del torneo
const paso = ref("equipos"); // valor por defecto

</script>

<template>
    <!-- Menú de pasos -->
      <div class="flex space-x-3 mb-5">
        <button @click="paso = 'equipos'" :class="[
          'px-4 py-2 rounded-lg',
          paso === 'equipos' ? 'bg-blue-600 text-white' : 'bg-gray-200 dark:bg-gray-700 text-gray-800 dark:text-gray-200'
        ]">
          Equipos
        </button>
        <!-- <button @click="paso = 'jugadores'" :class="[
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
        </button> -->
      </div>

      <!-- Vistas dinámicas -->
      <div class="bg-white dark:bg-slate-800 p-6 rounded-xl shadow-md">
        <div v-if="paso === 'equipos'">
          <ShowEquipos :torneo-id="torneoSeleccionado.id" />
        </div>

        <!-- <div v-else-if="paso === 'jugadores'">
          <ShowJugadores :torneo-id="torneoSeleccionado" />
        </div>

        <div v-else-if="paso === 'formato'">
          <CardsFormatoTorneo :torneo-id="torneoSeleccionado" />
        </div> -->
      </div>
</template>