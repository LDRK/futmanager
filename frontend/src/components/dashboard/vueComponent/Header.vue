<template>
     <header class="bg-white/60 shadow-md rounded-2xl p-5 flex justify-between items-center  dark:bg-[rgba(30,41,59,0.5)]
         backdrop-blur-[10px]">
      <h1 class="text-xl font-bold text-purple-700 dark:text-slate-50">Dashboard</h1>
      <div class="flex items-center gap-4">
          <button @click="showModal = true" class="flex bg-purple-600 text-white px-2 py-2 ml-3 rounded-lg shadow dark:bg-orange-600 dark:hover:bg-orange-700">
            <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e3e3e3"><path d="M440-440H200v-80h240v-240h80v240h240v80H520v240h-80v-240Z"/></svg>
            <span class="ml-1"> Crear Torneo </span>
            
          </button>
          <input type="text" placeholder="Search..." class=" bg-gray-100 text-gray-700 px-4 py-2 border rounded-lg">
        <div class="w-10 h-10 rounded-full bg-purple-500 flex items-center justify-center text-white font-bold dark:bg-orange-600">SR</div>
      </div>
    </header>

     <!-- Componente Modal -->
    <ModalCreateTorneo
      :visible="showModal"
      @close="showModal = false"
    />


</template>
<script setup>
import { ref } from 'vue'
import ModalCreateTorneo from './modals/ModalCreateTorneo.vue';

const showModal = ref(false)


</script>