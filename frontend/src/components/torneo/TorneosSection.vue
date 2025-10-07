<script setup>
import { ref, onMounted } from "vue";

const torneos = ref([]);
const loading = ref(true);
const error = ref(null);

onMounted(async () => {
  try {
    const res = await fetch("http://127.0.0.1:8000/api/torneos/");
    if (!res.ok) throw new Error(`Error HTTP: ${res.status}`);
    const data = await res.json();
    console.log("Datos recibidos:", data); // 👈 mira consola
    torneos.value = data;
  } catch (err) {
    console.error("Error al traer torneos:", err);
    error.value = err.message;
  } finally {
    loading.value = false;
  }
});
</script>

<template>
  <section class="bg-slate-50 dark:bg-gray-800 py-12">
    <div class="max-w-6xl mx-auto px-4">
      <h2 class="text-4xl text-orange-600 mb-10 text-center dark:text-orange-500">
        Torneos
      </h2>

      <!-- Estados -->
      <p v-if="loading" class="text-center text-gray-500">Cargando torneos...</p>
      <p v-else-if="error" class="text-center text-red-500">Error: {{ error }}</p>
      <p v-else-if="torneos.length === 0" class="text-center text-gray-500">
        No hay torneos disponibles
      </p>

      <!-- Cards -->
      <div
        v-else
        class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 2xl:grid-cols-4 gap-6"
      >
        <div
          v-for="torneo in torneos"
          :key="torneo.id"
          class="relative flex flex-col rounded-xl bg-white bg-clip-border text-gray-700 shadow-md dark:bg-gray-900"
        >
          <div
            class="relative h-40 overflow-hidden rounded-t-xl bg-gradient-to-r from-gray-700 to-gray-800 shadow-lg 
                   dark:bg-gradient-to-r dark:from-blue-700 dark:to-blue-800"
          >
            <img
              v-if="torneo.imagen"
              :src="torneo.imagen"
              alt="Imagen torneo"
              class="h-full w-full object-cover"
            />
          </div>
          <div class="p-6">
            <h5 class="mb-2 text-xl font-semibold text-gray-900 dark:text-white">
              {{ torneo.nombre }}
            </h5>
            <p class="text-base font-light leading-relaxed text-gray-600 dark:text-gray-300">
              {{ torneo.descripcion }}
            </p>
          </div>
          <div class="p-6 pt-0">
            <button
              type="button"
              class="w-full rounded-lg bg-orange-600 py-3 px-6 text-xs font-bold uppercase text-white shadow-md transition-all hover:shadow-lg hover:bg-orange-700 focus:opacity-85 active:opacity-85 dark:bg-orange-500 dark:hover:bg-orange-600"
            >
              Más información
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
