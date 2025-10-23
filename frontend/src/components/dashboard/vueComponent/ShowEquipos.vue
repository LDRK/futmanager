<script setup>
import { ref, onMounted } from "vue";
const equipos = ref([]);
const loading = ref(true);
const error = ref(null);

onMounted(async () => {
  try {
    const res = await fetch("http://127.0.0.1:8000/api/equipo/");
    if (!res.ok) throw new Error(`Error HTTP: ${res.status}`);
    const data = await res.json();
    equipos.value = data;
  } catch (err) {
    console.error("Error al traer los equipos:", err);
    error.value = err.message;
  } finally {
    loading.value = false;
  }
});

</script>
<template>
    <!-- Estados -->
      <p v-if="loading" class="text-center text-gray-500">Cargando equipos...</p>
      <p v-else-if="error" class="text-center text-red-500">Error: {{ error }}</p>
      <p v-else-if="equipos.length === 0" class="text-center text-gray-500">
        No hay equipos disponibles
      </p>
      <div class="bg-white/60 rounded-2xl mb-5 shadow-md 
         dark:bg-[rgba(30,41,59,0.5)] 
         backdrop-blur-[10px] 
         border border-[rgba(148,163,184,0.1)] 
         p-6">
         <div class="flex justify-between ">
            <h2 class="text-gray-800 dark:text-white text-[20px] mb-5 font-semibold">
          Lista de equipos
        </h2>
        <button @click="showModal = true" class="flex bg-purple-600 text-white px-2 py-2 ml-3 mb-2 rounded-lg shadow dark:bg-orange-600 dark:hover:bg-orange-700">
            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e3e3e3"><path d="M440-440H200v-80h240v-240h80v240h240v80H520v240h-80v-240Z"/></svg>
            <span class="ml-1"> Registrar Equipos</span>
            
          </button>
         </div>
        

        <table class="w-full text-left border-collapse">
          <thead class="bg-white/60 text-gray-700 
             dark:bg-[rgba(99,102,241,0.1)]">
            <tr>
              <th class="p-4 text-purple-600 font-semibold text-sm uppercase tracking-wide">Nombre</th>
              <th class="p-4 text-purple-600 font-semibold text-sm uppercase tracking-wide">Capitan</th>
              <th class="p-4 text-purple-600 font-semibold text-sm uppercase tracking-wide">Fecha Inscripcion</th>
              
            </tr>
          </thead>

          <tbody>
            <tr v-for="equipo in equipos" :key="equipo.id" class="border-t border-[rgba(148,163,184,0.1)] 
               hover:bg-[rgba(99,102,241,0.05)] 
               transition-colors duration-200">
              <td class="text-gray-900 dark:text-slate-300 p-4">{{ equipo.nombre }}</td>
              <td class="text-gray-900 dark:text-slate-300 p-4">{{ equipo.capitan }}</td>
              <td class="text-gray-900 dark:text-slate-300 p-4">{{ equipo.fecha_inscripcion }}</td>
            </tr>
          </tbody>
        </table>


      </div>
</template>
