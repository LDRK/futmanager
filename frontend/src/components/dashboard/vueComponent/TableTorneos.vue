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
  <section class="mb-4">
    <!-- Estados -->
    <p v-if="loading" class="text-center text-gray-500">Cargando torneos...</p>
    <p v-else-if="error" class="text-center text-red-500">Error: {{ error }}</p>
    <p v-else-if="torneos.length === 0" class="text-center text-gray-500">
      No hay torneos disponibles
    </p>

    <div v-else class="bg-white rounded-lg shadow-md">
      <div class="bg-purple-700 text-white font-bold  p-4 dark:bg-slate-600">Lista de Torneos</div>

      <table class="w-full text-left">
        <thead class="bg-purple-100 text-gray-700 dark:bg-slate-300">
          <tr>
            <th class="p-4">Nombre</th>
            <th class="p-4">Descripción</th>
            <th class="p-4">Fecha de Inicio</th>
            <th class="p-4">Fecha de Finalización</th>
            <th class="p-4">Organizador</th>
            <th class="p-4">Estado</th>
          </tr>
        </thead>

        <tbody>
          <tr
            v-for="torneo in torneos"
            :key="torneo.id"
            class="border-t hover:bg-gray-50 transition"
          >
            <td class="text-black p-4">{{ torneo.nombre }}</td>
            <td class="text-black p-4">{{ torneo.descripcion }}</td>
            <td class="text-black p-4">{{ torneo.fecha_inicio }}</td>
            <td class="text-black p-4">{{ torneo.fecha_fin }}</td>
            <td class="text-black p-4">{{ torneo.organizador }}</td>
            <td
              class="p-4 font-bold"
              :class="torneo.activo ? 'text-green-600' : 'text-red-600'"
            >
              {{ torneo.activo ? 'Activo' : 'Inactivo' }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
</template>
