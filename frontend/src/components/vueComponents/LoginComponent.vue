<script setup>
import { ref } from 'vue'
import axios from 'axios'

const formLogin = ref({
  username: '',
  password: '',
})

const loading = ref(false)
const errorMessage = ref('')

const loginUser = async () => {
  loading.value = true
  errorMessage.value = ''

  try {
    const response = await axios.post('http://127.0.0.1:8000/auth/login/', formLogin.value)

    // Guardamos el token en localStorage
    localStorage.setItem('token', response.data.access)
    localStorage.setItem('refresh', response.data.refresh)

    // Redirigir al dashboard
    window.location.href = '/dashboard'
  } catch (error) {
    console.error(error)
    errorMessage.value = 'Credenciales incorrectas o error de conexión.'
  } finally {
    loading.value = false
  }
}
</script>
<template>
    <div class="w-full max-w-sm p-4 bg-white border border-gray-200 rounded-lg shadow-sm sm:p-6 md:p-8 dark:bg-gray-800 dark:border-gray-700">
                <form @submit.prevent="loginUser"  class="space-y-6" method="post">
                    <h5 class="text-xl text-center font-medium text-gray-900 dark:text-white">Entrar</h5>
                    <div>
                        <label for="username" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Usuario</label>
                        <input v-model="formLogin.username" type="text" name="username" id="username" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" placeholder="Usuario" required />
                    </div>
                    <div>
                        <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Contraseña</label>
                        <input v-model="formLogin.password" type="password" name="password" id="password" placeholder="••••••••" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white" required />
                    </div>
                    
                    <div class="flex items-start">
                        <a href="/register" class="text-sm text-blue-700 hover:underline dark:text-blue-500">Not account?</a>
                        <a href="#" class="ms-auto text-sm text-blue-700 hover:underline dark:text-blue-500">Lost Password?</a>
                    </div>
                    <button type="submit" :disabled="loading" class="w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                        {{ loading ? "Ingresando..." : "Iniciar Sesión" }}
                    </button>

                    <!-- Mensaje de error -->
                    <p v-if="errorMessage" class="text-red-600 text-sm text-center mt-2">
                        {{ errorMessage }}
                    </p>
                    
                </form>
            </div>
</template>