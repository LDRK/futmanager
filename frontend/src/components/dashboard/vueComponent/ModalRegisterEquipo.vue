<template>
    <transition name="fade">
    <div
      v-if="visible"

      class="fixed inset-0 bg-gray-900/50 backdrop-blur-sm flex items-center justify-center z-50"
    >
      <div
        class="bg-white/60 0 p-6 rounded-xl w-full max-w-lg shadow-xl relative dark:bg-gray-800"
      >
        <h2 class="text-xl font-bold mb-4 text-center text-gray-800 dark:text-slate-50">
          Registrar Equipo
        </h2>

        <form @submit.prevent="registrarEquipo">
          <input
            v-model="form.nombre"
            placeholder="Nombre del torneo"
            class="block w-full rounded-md bg-white/5 px-3 py-3 mb-2 text-base text-white outline-1 -outline-offset-1 outline-white/10 placeholder:text-gray-500 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-500 sm:text-sm/6"
            required
          />
          <input
            type="date"
            v-model="form.fecha_inscripcion"
            class="block w-full rounded-md bg-white/5 px-3 py-3 mb-2 text-base text-white outline-1 -outline-offset-1 outline-white/10 placeholder:text-gray-500 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-500 sm:text-sm/6"
            required
          />

          <div class="flex justify-end mt-4 gap-2">
            <button
              type="button"
              @click="cerrar"
              class="bg-gray-400 hover:bg-gray-500 text-white px-4 py-2 rounded-lg"
            >
              Cancelar
            </button>
            <button
              type="submit"
              class="bg-gray-800 hover:bg-gray-700  dark:bg-blue-800 dark:hover:bg-blue-700 text-white px-4 py-2 rounded-lg"
            >
              Guardar
            </button>
          </div>
        </form>

        <button
          @click="cerrar"
          class="absolute top-3 right-4 "
        >
          <span class="text-gray-400 hover:text-red-600 text-2xl font-bold">X</span>
        </button>
      </div>
    </div>
  </transition>
</template>
<script setup>
import { ref, watch, defineEmits, defineProps } from 'vue'
import axios from 'axios'
import Swal from 'sweetalert2'

// Props y emits
const props = defineProps({ visible: Boolean })
const emit = defineEmits(['close', 'success'])

// Formulario
const form = ref({
  nombre: '',
  fecha_inscripcion: '',
  torneo_id: 1
  })

// Cerrar modal
const cerrar = () => emit('close')

// Registrar torneo
const registrarEquipo = async () => {
  try {
    await axios.post('http://127.0.0.1:8000/api/equipo/', form.value)
    Swal.fire('Torneo creado', '', 'success')
    emit('success') // notifica al padre que se registró correctamente
    cerrar()
  } catch (error) {
    console.error(error)
    Swal.fire('Error', 'No se pudo registrar el torneo', 'error')
  }
}
</script>