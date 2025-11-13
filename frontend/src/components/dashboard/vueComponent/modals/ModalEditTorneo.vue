<script setup>
import { ref, watch } from 'vue';
import Swal from 'sweetalert2';

const props = defineProps({
  visible: Boolean,
  equipo: Object
})

const emit = defineEmits(['close', 'equipoEditado'])

const nombre = ref('')
const fecha_inscripcion = ref('')

// Cargar datos del equipo cuando se abre el modal
watch(() => props.equipo, (nuevoEquipo) => {
  if (nuevoEquipo) {
    nombre.value = nuevoEquipo.nombre;
    fecha_inscripcion.value = nuevoEquipo.fecha_inscripcion;
  }
}, { immediate: true });

const editarEquipo = async () => {
  if (!nombre.value.trim()) {
    Swal.fire('Error', 'El nombre del equipo es requerido', 'error');
    Swal.fire('Error', 'La fecha de inscripcion del equipo es requerido', 'error');
    return;
  }

  try {
    const res = await fetch(`http://127.0.0.1:8000/api/equipo/${props.equipo.id}/`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        nombre: nombre.value,
        fecha_inscripcion: fecha_inscripcion.value,
        torneo: props.equipo.torneo
      })
    });

    if (!res.ok) throw new Error('Error al editar el equipo');

    const equipoActualizado = await res.json();
    
    Swal.fire('Éxito', 'Equipo editado correctamente', 'success');
    emit('equipoEditado', equipoActualizado);
    emit('close');
  } catch (error) {
    console.error(error);
    Swal.fire('Error', 'No se pudo editar el equipo', 'error');
  }
};
</script>

<template>
  <div v-if="visible" class="fixed inset-0 z-50 flex items-center justify-center bg-black/50">
    <div class="bg-white dark:bg-slate-800 rounded-lg p-6 w-full max-w-md">
      <h2 class="text-xl font-bold mb-4 text-gray-800 dark:text-white">Editar Equipo</h2>
      
      <form @submit.prevent="editarEquipo">
        <div class="mb-4">
          <label class="block text-gray-700 dark:text-gray-300 mb-2">Nombre del Equipo</label>
          <input 
            v-model="nombre"
            type="text" 
            class="w-full px-3 py-2 border rounded-lg dark:bg-slate-700 dark:text-white"
            placeholder="Nombre del equipo"
          />
        </div>
        <div class="mb-4">
          <label class="block text-gray-700 dark:text-gray-300 mb-2">Fecha de Inscripcion</label>
          <input 
            v-model="fecha_inscripcion"
            type="text" 
            class="w-full px-3 py-2 border rounded-lg dark:bg-slate-700 dark:text-white"
            placeholder="Fecha de Inscripcion"
          />
        </div>

        <div class="flex gap-2 justify-end">
          <button 
            type="button"
            @click="emit('close')"
            class="px-4 py-2 bg-gray-500 text-white rounded-lg hover:bg-gray-600"
          >
            Cancelar
          </button>
          <button 
            type="submit"
            class="px-4 py-2 bg-orange-500 text-white rounded-lg hover:bg-orange-600"
          >
            Guardar Cambios
          </button>
        </div>
      </form>
    </div>
  </div>
</template>