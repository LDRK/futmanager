    <script setup>
        defineProps({
        torneoSeleccionado: {
            type: Object,
            required: true
        }
        })
    </script>
    <template>
        <div class="bg-gradient-to-r from-blue-900/40 to-purple-900/40 backdrop-blur-sm rounded-xl p-6 mb-8 border border-blue-500/30 shadow-2xl">
            <div class="flex items-center justify-between mb-4">
            <div class="flex items-center">
                <div class="w-8 h-8 mr-3">
                    <svg class="text-slate-50"  viewBox="0 0 512 512">
                    <path fill="currentColor" d="M144.3 0l224 0c26.5 0 48.1 21.8 47.1 48.2-.2 5.3-.4 
                    10.6-.7 15.8l49.6 0c26.1 0 49.1 21.6 47.1 49.8-7.5 103.7-60.5 
                    160.7-118 190.5-15.8 8.2-31.9 14.3-47.2 18.8-20.2 28.6-41.2 
                    43.7-57.9 51.8l0 73.1 64 0c17.7 0 32 14.3 32 32s-14.3 
                    32-32 32l-192 0c-17.7 0-32-14.3-32-32s14.3-32 32-32l64 
                    0 0-73.1c-16-7.7-35.9-22-55.3-48.3-18.4-4.8-38.4-12.1-57.9-23.1-54.1-30.3-102.9-87.4-109.9-189.9-1.9-28.1 
                    21-49.7 47.1-49.7l49.6 0c-.3-5.2-.5-10.4-.7-15.8-1-26.5 20.6-48.2 47.1-48.2zM101.5 112l-52.4 0c6.2 84.7 45.1 
                    127.1 85.2 149.6-14.4-37.3-26.3-86-32.8-149.6zM380 256.8c40.5-23.8 77.1-66.1 83.3-144.8L411 112c-6.2 60.9-17.4 
                    108.2-31 144.8z"/>
                </svg>
                </div>
                <h2 class="text-2xl font-bold">{{ torneoSeleccionado.nombre }}</h2>
            </div>
            <span class="bg-green-500/20 text-green-400 px-4 py-2 rounded-full text-sm font-semibold border border-green-500/30">
                En Progreso
            </span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
            <div>
                <p class="text-slate-400 text-sm mb-1">Fase Actual</p>
                <p class="text-lg font-semibold">Fase de Grupos</p>
            </div>
            <div>
                <p class="text-slate-400 text-sm mb-1">Jornada</p>
                <p class="text-lg font-semibold">8 de 10</p>
            </div>
            <div>
                <p class="text-slate-400 text-sm mb-1">Partidos Restantes</p>
                <p class="text-lg font-semibold">6 partidos</p>
            </div>
            </div>
            <div class="bg-slate-800/50 rounded-full h-3 overflow-hidden">
            <div class="bg-gradient-to-r from-blue-500 to-purple-500 h-full rounded-full" style="width: 80%" ></div>
            </div>
            <p class="text-sm text-slate-400 mt-2">80% completado</p>
        </div>

    </template> 