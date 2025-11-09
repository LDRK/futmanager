<script setup>
import {ref} from "vue"
import PartidosComponent from './torneoActivo/PartidosComponent.vue';
import TablaTorneo from "./torneoActivo/TablaTorneo.vue";
import EstadisticasTorneo from "./torneoActivo/EstadisticasTorneo.vue";

const props = defineProps({
  torneoSeleccionado: {
    type: Object,
    required: true,
  },
});


const paso = ref('partidos')
</script>
<template>
    <section>
        <div class="bg-slate-800/50 backdrop-blur-sm rounded-xl p-2 mb-6 flex gap-2 overflow-x-auto">
            <button @click="paso = 'partidos'"
              class="flex items-center gap-2 px-6 py-3 rounded-lg font-semibold transition whitespace-nowrap
              text-white shadow-lg
             hover:text-white hover:bg-slate-700/50"
            >
            Partidos
            </button>
            <button @click="paso = 'tabla'"
              class="flex items-center gap-2 px-6 py-3 rounded-lg font-semibold transition whitespace-nowrap
               text-white shadow-lg
             hover:text-white hover:bg-slate-700/50"
            >
            Tabla
            </button>
            <button 
              class="flex items-center gap-2 px-6 py-3 rounded-lg font-semibold transition whitespace-nowrap
               text-white shadow-lg
             hover:text-white hover:bg-slate-700/50"
            >
            Equipos
            </button>
            <button @click="paso = 'estadisticas'"
              class="flex items-center gap-2 px-6 py-3 rounded-lg font-semibold transition whitespace-nowrap
               text-white shadow-lg
             hover:text-white hover:bg-slate-700/50"
            >
            Estadisticas
            </button>
      </div>

    <div class="col-span-2 bg-slate-800/50 p-6 rounded-lg shadow">
          <!-- Renderiza el paso seleccionado -->
          <div v-if="paso === 'partidos'">
            <PartidosComponent :torneo-id="torneoSeleccionado.id"/>
          </div>
          <div v-else-if="paso === 'tabla'">
            <TablaTorneo/>
          </div>
          <div v-else-if="paso === 'estadisticas'">
            <EstadisticasTorneo/>
          </div>
          <div v-else>
            <p>Selecciona una opción para continuar.</p>
          </div>
    </div>


    </section>
</template>