<script setup>
import ShowEquipos from "./ShowEquipos.vue";

const props = defineProps({
  torneoSeleccionado: {
    type: Object,
    required: true,
  },
});


</script>

<template>
  <!-- Botón de cambio de estado -->
  <div class="flex space-x-3 mb-5">
    
  </div>

  <!-- Vista de contenido -->
  <div class="bg-white dark:bg-slate-800 p-6 rounded-xl shadow-md">
    <!-- <h1 class="text-xl text-slate-50 font-bold mb-4">Registro de equipos</h1> -->
    <div>
      <ShowEquipos :torneo-id="props.torneoSeleccionado.id" />
    </div>
  </div>
</template>
