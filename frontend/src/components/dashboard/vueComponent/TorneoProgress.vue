<script setup>
import { ref } from "vue";
import Swal from "sweetalert2";
import axios from "axios";
defineProps({
    torneoSeleccionado: {
        type: Object,
        required: true
    }
})

const emit = defineEmits(["estadoActualizado"]);

async function cambiarEstadoTorneo() {
    const confirmar = await Swal.fire({
        title: "¿Finalizar registro del torneo?",
        text: "Una vez finalizado, no podrás registrar más equipos ni jugadores (aunque luego puedes reabrirlo).",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Sí, finalizar",
        cancelButtonText: "Cancelar",
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
    });

    if (!confirmar.isConfirmed) return;

    try {
        // Construimos el JSON completo con los datos del torneo
        const torneoActualizado = {
            nombre: props.torneoSeleccionado.nombre,
            descripcion: props.torneoSeleccionado.descripcion,
            fecha_inicio: props.torneoSeleccionado.fecha_inicio,
            fecha_fin: props.torneoSeleccionado.fecha_fin,
            // organizador: props.torneoSeleccionado.organizador,
            organizador: 1, // Id del usuario fijo, no esta disponible los tokens de acceso, con roles diferenciados. 
            estado: "activo", // el nuevo estado del torneo
        };

        // Enviamos la actualización al backend
        const response = await axios.patch(
            `http://127.0.0.1:8000/api/torneos/${props.torneoSeleccionado.id}/`,
            torneoActualizado
        );

        Swal.fire("Torneo actualizado", "El estado se cambió correctamente", "success");
        emit("estadoActualizado", response.data);
    } catch (error) {
        console.error("Error al cambiar el estado:", error);
        Swal.fire("Error", "No se pudo cambiar el estado del torneo", "error");
    }
}
</script>
<template>
    <div
        class="bg-gradient-to-r from-blue-900/40 to-purple-900/40 backdrop-blur-sm rounded-xl p-6 mb-8 border border-blue-500/30 shadow-2xl">
        <div class="flex items-center justify-between mb-4">
            <div class="flex items-center">
                <div class="size-10 mr-3">
                    <svg class="text-slate-50" viewBox="0 0 512 512">
                        <path fill="currentColor" d="M144.3 0l224 0c26.5 0 48.1 21.8 47.1 48.2-.2 5.3-.4 
                    10.6-.7 15.8l49.6 0c26.1 0 49.1 21.6 47.1 49.8-7.5 103.7-60.5 
                    160.7-118 190.5-15.8 8.2-31.9 14.3-47.2 18.8-20.2 28.6-41.2 
                    43.7-57.9 51.8l0 73.1 64 0c17.7 0 32 14.3 32 32s-14.3 
                    32-32 32l-192 0c-17.7 0-32-14.3-32-32s14.3-32 32-32l64 
                    0 0-73.1c-16-7.7-35.9-22-55.3-48.3-18.4-4.8-38.4-12.1-57.9-23.1-54.1-30.3-102.9-87.4-109.9-189.9-1.9-28.1 
                    21-49.7 47.1-49.7l49.6 0c-.3-5.2-.5-10.4-.7-15.8-1-26.5 20.6-48.2 47.1-48.2zM101.5 112l-52.4 0c6.2 84.7 45.1 
                    127.1 85.2 149.6-14.4-37.3-26.3-86-32.8-149.6zM380 256.8c40.5-23.8 77.1-66.1 83.3-144.8L411 112c-6.2 60.9-17.4 
                    108.2-31 144.8z" />
                    </svg>
                </div>
                <div class="flex-col">
                    <h2 class="text-2xl font-bold">{{ torneoSeleccionado.nombre }}</h2>
                <p class="mt-1">{{ torneoSeleccionado.descripcion }}</p>
                </div>
                
            </div>
            <div class="flex gap-3">
                <span
                    class="bg-green-500/20 text-green-400 px-4 py-2 rounded-full text-sm font-semibold border border-green-500/30">
                    En Progreso
                </span>
                <button @click="cambiarEstadoTorneo"
                    class="flex bg-purple-600 text-white px-2 py-2 rounded-lg shadow dark:bg-orange-600 dark:hover:bg-orange-700">
                    Finalizar Registro
                </button>
            </div>

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
            <div class="bg-gradient-to-r from-blue-500 to-purple-500 h-full rounded-full" style="width: 80%"></div>
        </div>
        <p class="text-sm text-slate-400 mt-2">80% completado</p>
    </div>

</template>