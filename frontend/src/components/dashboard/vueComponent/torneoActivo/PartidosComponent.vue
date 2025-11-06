<script setup>

</script>
<template>
    <div class="bg-slate-800/30 backdrop-blur-sm rounded-xl p-6">
          <div>
            <div class="flex justify-between items-center mb-6">
              <h2 class="text-2xl font-bold">Calendario de Partidos</h2>
              <button class="bg-orange-500 hover:bg-orange-600 text-white px-4 py-2 rounded-lg font-semibold flex items-center gap-2 transition">
                Registrar Resultado
              </button>
            </div>

            <div class="flex gap-3 mb-6">
                <button class="px-4 py-2 bg-slate-700 hover:bg-slate-600 rounded-lg text-sm transition">
                 Todos
                </button>
                <button class="px-4 py-2 bg-slate-700 hover:bg-slate-600 rounded-lg text-sm transition">
                 Pendientes
                </button>
                <button class="px-4 py-2 bg-slate-700 hover:bg-slate-600 rounded-lg text-sm transition">
                 Finalizados
                </button>
            </div>

            <div class="space-y-4">
                <div class="bg-slate-700/50 rounded-xl p-6 hover:bg-slate-700 transition">
                  <div class="flex items-center justify-between mb-4">
                    <div>
                      <span class="text-purple-400 font-semibold">Jornada</span>
                      <span class="text-gray-400 ml-4">14/11/2025 • 15:00</span>
                    </div>
                    <span class="px-3 py-1 rounded-full text-xs font-semibold">
                      Estado del partido
                    </span>
                  </div>
                  
                  <div class="flex items-center justify-center gap-8">
                    <div class="text-right flex-1">
                      <p class="text-xl font-bold">Equipo 1</p>
                    </div>
                    <div class="bg-slate-800 px-6 py-3 rounded-lg">
                      <p class="text-3xl font-bold">
                       0-0
                      </p>
                    </div>
                    <div class="text-left flex-1">
                      <p class="text-xl font-bold">Equipo 2</p>
                    </div>
                  </div>

                  <p class="text-center text-gray-400 text-sm mt-4">Lugar del partido</p>
                </div>
            </div>
          </div>
        </div>

</template>