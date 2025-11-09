<script setup>
import { ref, onMounted } from "vue";
import Swal from "sweetalert2";

const partidos = ref([]);
const loading = ref(true);
const error = ref(null);
const next = ref(null);
const previous = ref(null);
const currentPage = ref(1);
const totalPages = ref(1);
const pageSize = 4; // igual al backend

const props = defineProps({
  torneoId: {
    type: Number,
    required: true,
  },
});

const getPartidos = async (page = 1) => {
  loading.value = true;
  try {
    const res = await fetch(
      `http://127.0.0.1:8000/api/partidos/torneo/${props.torneoId}/?page=${page}`
    );
    if (!res.ok) throw new Error(`Error HTTP: ${res.status}`);
    const data = await res.json();

    partidos.value = data.results || [];
    next.value = data.next;
    previous.value = data.previous;
    totalPages.value = Math.ceil(data.count / pageSize);
    currentPage.value = page;
  } catch (err) {
    console.error("Error al traer los partidos:", err);
    error.value = err.message;
  } finally {
    loading.value = false;
  }
};

const goToPage = (page) => {
  if (page < 1 || page > totalPages.value) return;
  getPartidos(page);
};

onMounted(() => {
  getPartidos();
});
</script>

<template>
  <div class="bg-slate-800/30 backdrop-blur-sm rounded-xl p-6">
    <div>
      <div class="flex justify-between items-center mb-6">
        <h2 class="text-2xl font-bold">Calendario de Partidos</h2>
        <button
          class="bg-orange-500 hover:bg-orange-600 text-white px-4 py-2 rounded-lg font-semibold flex items-center gap-2 transition"
        >
          Registrar Resultado
        </button>
      </div>

      <div class="flex gap-3 mb-6">
        <button
          class="px-4 py-2 bg-slate-700 hover:bg-slate-600 rounded-lg text-sm transition"
        >
          Todos
        </button>
        <button
          class="px-4 py-2 bg-slate-700 hover:bg-slate-600 rounded-lg text-sm transition"
        >
          Pendientes
        </button>
        <button
          class="px-4 py-2 bg-slate-700 hover:bg-slate-600 rounded-lg text-sm transition"
        >
          Finalizados
        </button>
      </div>

      <div v-if="loading" class="text-gray-400 text-center py-6">
        Cargando partidos...
      </div>

      <div v-else-if="error" class="text-red-400 text-center py-6">
        {{ error }}
      </div>

      <div v-else class="space-y-4">
        <div
          v-for="partido in partidos"
          :key="partido.id"
          class="bg-slate-700/50 rounded-xl p-6 hover:bg-slate-700 transition"
        >
          <div class="flex items-center justify-between mb-4">
            <div>
              <span class="text-purple-400 font-semibold">Jornada</span>
              <span class="text-gray-400 ml-4">14/11/2025 • 15:00</span>
            </div>
            <span class="px-3 py-1 rounded-full text-xs font-semibold">
              {{ partido.estado }}
            </span>
          </div>

          <div class="flex items-center justify-center gap-8">
            <div class="text-right flex-1">
              <p class="text-xl font-bold">{{ partido.equipo_local }}</p>
            </div>
            <div class="bg-slate-800 px-6 py-3 rounded-lg">
              <p class="text-3xl font-bold">0-0</p>
            </div>
            <div class="text-left flex-1">
              <p class="text-xl font-bold">{{ partido.equipo_visitante }}</p>
            </div>
          </div>

          <p class="text-center text-gray-400 text-sm mt-4">
            {{ partido.lugar_partido || "Por definir" }}
          </p>
        </div>

        <!-- PAGINACIÓN -->
        <div class="flex justify-center items-center gap-3 mt-6">
          <button
            @click="goToPage(currentPage - 1)"
            :disabled="!previous"
            class="px-4 py-2 rounded-lg border border-gray-500 text-sm text-gray-300 disabled:opacity-50 hover:bg-slate-600"
          >
            ◀ Anterior
          </button>

          <span class="text-gray-400 text-sm">
            Página {{ currentPage }} / {{ totalPages }}
          </span>

          <button
            @click="goToPage(currentPage + 1)"
            :disabled="!next"
            class="px-4 py-2 rounded-lg border border-gray-500 text-sm text-gray-300 disabled:opacity-50 hover:bg-slate-600"
          >
            Siguiente ▶
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
