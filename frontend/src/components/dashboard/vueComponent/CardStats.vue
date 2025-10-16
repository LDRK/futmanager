<script setup>
import { ref, onMounted, computed } from "vue";

const torneos = ref([]);
const loading = ref(true);
const error = ref(null);

onMounted(async () => {
  try {
    const res = await fetch("http://127.0.0.1:8000/api/torneos/");
    if (!res.ok) throw new Error(`Error HTTP: ${res.status}`);
    const data = await res.json();
    // console.log("Datos recibidos:", data); 
    torneos.value = data;
  } catch (err) {
    console.error("Error al traer torneos:", err);
    error.value = err.message;
  } finally {
    loading.value = false;
  }

  
    
});
//  Computed con campo 'activo' booleano
const totalTorneos = computed(() => torneos.value.length);

const torneosActivos = computed(() =>
  torneos.value.filter(t => t.activo === true).length
);

const torneosPendientes = computed(() =>
  torneos.value.filter(t => t.activo === false).length
);



// // Depuración (solo para ver valores)
// console.log("Total torneos:", totalTorneos.value);
// console.log("Activos:", torneosActivos.value);
// console.log("Pendientes:", torneosPendientes.value);


</script>
<template>
    <section>
        <!-- Estados -->
        <p v-if="loading" class="text-center text-gray-500">Cargando Datos...</p>
        <p v-else-if="error" class="text-center text-red-500">Error: {{ error }}</p>
        <p v-else-if="torneos.length === 0" class="text-center text-gray-500">
            No hay torneos disponibles
        </p>

        <!-- Cards -->
        <div 
            v-else 
            class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-4">

        <div class="bg-white p-6 rounded-lg shadow-md dark:bg-slate-600">
            <p class="text-sm text-gray-500 dark:text-slate-50">Total Torneos</p>
            <h2 class="text-3xl font-bold text-purple-700 mt-2 dark:text-orange-500">{{ totalTorneos }}</h2>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-md dark:bg-slate-600">
            <p class="text-sm text-gray-500 dark:text-slate-50">Total de Equipos</p>
            <h2 class="text-3xl font-bold text-green-600 mt-2 dark:text-orange-500">$24,500</h2>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-md dark:bg-slate-600">
            <p class="text-sm text-gray-500 dark:text-slate-50">Torneos Activos</p>
            <h2 class="text-3xl font-bold text-blue-600 mt-2 dark:text-orange-500">{{ torneosActivos }}</h2>
        </div>
        <div class="bg-white p-6 rounded-lg shadow-md dark:bg-slate-600">
            <p class="text-sm text-gray-500 dark:text-slate-50">Torneos Pendientes</p>
            <h2 class="text-3xl font-bold text-red-500 mt-2 dark:text-orange-500">{{ torneosPendientes }}</h2>
        </div>
    </div>
    </section>
    
</template>