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
          Registrar Jugador
        </h2>

        <form @submit.prevent="registrarJugador">
          <input
            type="text"
            v-model="form.nombre"
            placeholder="Nombre del Jugador"
            class="block w-full rounded-md bg-white/5 px-3 py-3 mb-2 text-base text-white outline-1 -outline-offset-1 outline-white/10 placeholder:text-gray-500 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-500 sm:text-sm/6"
            required
          />
          <input
            type="text"
            v-model="form.apellido"
            placeholder="Apellido del Jugador"
            class="block w-full rounded-md bg-white/5 px-3 py-3 mb-2 text-base text-white outline-1 -outline-offset-1 outline-white/10 placeholder:text-gray-500 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-500 sm:text-sm/6"
            required
          />
          <input
            type="text"
            v-model="form.posicion"
            placeholder="Posicion del Jugador"
            class="block w-full rounded-md bg-white/5 px-3 py-3 mb-2 text-base text-white outline-1 -outline-offset-1 outline-white/10 placeholder:text-gray-500 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-500 sm:text-sm/6"
            required
          />
          <input
            type="number"
            v-model="form.nCamiseta"
            placeholder="Numero de la Camiseta"
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
  apellido: '',
  posicion: '',
  nCamiseta: '',
  equipo: 1
  })

// Cerrar modal
const cerrar = () => emit('close')

// Registrar Jugador
const registrarJugador = async () => {
  try {
    await axios.post('http://127.0.0.1:8000/api/jugador/', form.value)
    Swal.fire('Jugador Registrado', '', 'success')
    emit('success') // notificamos al padre que se registró correctamente
    cerrar()
  } catch (error) {
    console.error(error)
    Swal.fire('Error', 'No se pudo registrar el jugador', 'error')
  }
}
</script>