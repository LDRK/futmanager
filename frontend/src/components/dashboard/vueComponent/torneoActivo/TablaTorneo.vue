<template>
  <div>
    <h2 class="text-2xl font-bold mb-6">Tabla de Posiciones</h2>
    <div class="overflow-x-auto">
      <table class="w-full">
        <thead>
          <tr class="text-left border-b border-slate-600">
            <th class="pb-3 px-4 text-purple-400 font-semibold">#</th>
            <th class="pb-3 px-4 text-purple-400 font-semibold">Equipo</th>
            <th class="pb-3 px-4 text-center text-purple-400 font-semibold">PJ</th>
            <th class="pb-3 px-4 text-center text-purple-400 font-semibold">PG</th>
            <th class="pb-3 px-4 text-center text-purple-400 font-semibold">PE</th>
            <th class="pb-3 px-4 text-center text-purple-400 font-semibold">PP</th>
            <th class="pb-3 px-4 text-center text-purple-400 font-semibold">GF</th>
            <th class="pb-3 px-4 text-center text-purple-400 font-semibold">GC</th>
            <th class="pb-3 px-4 text-center text-purple-400 font-semibold">DG</th>
            <th class="pb-3 px-4 text-center text-purple-400 font-semibold">PTS</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="team in standings"
            :key="team.pos"
            class="border-b border-slate-700 hover:bg-slate-700/50 transition-colors duration-200"
          >
            <td class="py-4 px-4">
              <span 
                :class="[
                  'inline-flex items-center justify-center w-8 h-8 rounded-lg font-bold',
                  getPositionClass(team.pos)
                ]"
              >
                {{ team.pos }}
              </span>
            </td>
            <td class="py-4 px-4 font-semibold">{{ team.team }}</td>
            <td class="py-4 px-4 text-center">{{ team.pj }}</td>
            <td class="py-4 px-4 text-center">{{ team.pg }}</td>
            <td class="py-4 px-4 text-center">{{ team.pe }}</td>
            <td class="py-4 px-4 text-center">{{ team.pp }}</td>
            <td class="py-4 px-4 text-center">{{ team.gf }}</td>
            <td class="py-4 px-4 text-center">{{ team.gc }}</td>
            <td class="py-4 px-4 text-center">
              <span :class="getDifferenceClass(team.dg)">
                {{ team.dg > 0 ? '+' : '' }}{{ team.dg }}
              </span>
            </td>
            <td class="py-4 px-4 text-center font-bold text-lg">{{ team.pts }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Leyenda -->
    <div class="mt-6 flex gap-4 flex-wrap text-sm">
      <div class="flex items-center gap-2">
        <span class="w-4 h-4 bg-green-500 rounded"></span>
        <span class="text-gray-400">Clasificación directa</span>
      </div>
      <div class="flex items-center gap-2">
        <span class="w-4 h-4 bg-yellow-500 rounded"></span>
        <span class="text-gray-400">Repechaje</span>
      </div>
      <div class="flex items-center gap-2">
        <span class="w-4 h-4 bg-red-500 rounded"></span>
        <span class="text-gray-400">Descenso</span>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  standings: {
    type: Array,
    required: true
  }
})

const getPositionClass = (position) => {
  if (position <= 3) return 'bg-green-500 text-white'
  if (position <= 6) return 'bg-yellow-500 text-white'
  return 'bg-slate-600 text-gray-300'
}

const getDifferenceClass = (difference) => {
  if (difference > 0) return 'text-green-400'
  if (difference < 0) return 'text-red-400'
  return 'text-gray-400'
}
</script>