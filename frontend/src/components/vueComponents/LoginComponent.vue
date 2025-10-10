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
  <div class="min-h-screen  text-gray-800 flex justify-center dark:text-slate-50">
    <div class="max-w-screen-xl m-0 sm:m-10 bg-white shadow sm:rounded-lg flex justify-center flex-1">
      <div class="lg:w-1/2 xl:w-5/12 p-6 sm:p-12 dark:bg-gray-800">
        <div class="mx-auto w-fit">
          <Logo />
        </div>
        <div class="mt-12 flex flex-col items-center">
          <h1 class="text-2xl xl:text-3xl font-extrabold">
            Iniciar Sesion
          </h1>
          <div class="w-full flex-1 mt-8">
            <div class="flex flex-col items-center">
              <button
                class="w-full max-w-xs font-bold shadow-sm rounded-lg py-3 bg-indigo-100
                    text-gray-800 flex items-center justify-center transition-all duration-300 
                      ease-in-out focus:outline-none hover:shadow focus:shadow-sm focus:shadow-outline dark:bg-gray-300">
                <div class="bg-white p-2 rounded-full">
                  <svg class="w-4" viewBox="0 0 533.5 544.3">
                    <path
                      d="M533.5 278.4c0-18.5-1.5-37.1-4.7-55.3H272.1v104.8h147c-6.1 33.8-25.7 63.7-54.4 82.7v68h87.7c51.5-47.4 81.1-117.4 81.1-200.2z"
                      fill="#4285f4" />
                    <path
                      d="M272.1 544.3c73.4 0 135.3-24.1 180.4-65.7l-87.7-68c-24.4 16.6-55.9 26-92.6 26-71 0-131.2-47.9-152.8-112.3H28.9v70.1c46.2 91.9 140.3 149.9 243.2 149.9z"
                      fill="#34a853" />
                    <path
                      d="M119.3 324.3c-11.4-33.8-11.4-70.4 0-104.2V150H28.9c-38.6 76.9-38.6 167.5 0 244.4l90.4-70.1z"
                      fill="#fbbc04" />
                    <path
                      d="M272.1 107.7c38.8-.6 76.3 14 104.4 40.8l77.7-77.7C405 24.6 339.7-.8 272.1 0 169.2 0 75.1 58 28.9 150l90.4 70.1c21.5-64.5 81.8-112.4 152.8-112.4z"
                      fill="#ea4335" />
                  </svg>
                </div>
                <span class="ml-4">
                  Login with Google
                </span>
              </button>

            </div>

            <div class="my-12 border-b text-center">
              <div
                class="leading-none px-2 inline-block text-sm text-gray-600 tracking-wide font-medium bg-white transform translate-y-1/2 dark:bg-gray-800 dark:text-slate-50">
                Ingresa con Correo y Contraseña
              </div>
            </div>

            <form @submit.prevent="loginUser" class="mx-auto max-w-xs">
              <div class="space-y-1">
                <!-- username -->
                <input v-model="formLogin.username" 
                  class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white  dark:text-gray-800"
                  type="text" placeholder="Correo o Usuario" required />
                <!-- contraseña -->
                <input v-model="formLogin.password"
                  class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-3  dark:text-gray-800"
                  type="password" placeholder="Contraseña" required />
                 <div class="flex items-start">
                        <a href="/register" class="text-sm text-blue-700 hover:underline dark:text-blue-500">Not account?</a>
                        <a href="#" class="ms-auto text-sm text-blue-700 hover:underline dark:text-blue-500">Lost Password?</a>
                  </div>

                <!-- Boton Continuar -->
                <button :disabled="loading"
                  class="mt-5 tracking-wide font-semibold bg-gray-800 text-gray-100 w-full py-4 rounded-lg
                   hover:bg-gray-700 transition-all duration-300 ease-in-out flex items-center justify-center 
                   focus:shadow-outline focus:outline-none  dark:bg-orange-600 dark:hover:bg-orange-700">
                  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e3e3e3"><path d="M480-120v-80h280v-560H480v-80h280q33 0 56.5 23.5T840-760v560q0 33-23.5 56.5T760-120H480Zm-80-160-55-58 102-102H120v-80h327L345-622l55-58 200 200-200 200Z"/></svg>
                  <span class="ml-3">
                    {{ loading ? "Ingresando..." : "Iniciar Sesión" }}
                  </span>
                </button>
                <p class="mt-6 text-xs text-slate-50 text-center">
                  I agree to abide by templatana's
                  <a href="#" class="border-b border-gray-500 border-dotted">
                    Terms of Service
                  </a>
                  and its
                  <a href="#" class="border-b border-gray-500 border-dotted">
                    Privacy Policy
                  </a>
                </p>
              </div>
            </form>
          </div>
        </div>
      </div>
      <div class="flex-1 bg-indigo-100 text-center hidden lg:flex dark:bg-white">
        <div class="m-12 xl:m-16 w-full bg-contain bg-center bg-no-repeat"
          style="background-image: url('/img-torneo2.png');">
        </div>
      </div>
    </div>
  </div>
</template>


<!-- <template>
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
                    <!-- <p v-if="errorMessage" class="text-red-600 text-sm text-center mt-2">
                        {{ errorMessage }}
                    </p>
                    
                </form> -->
            <!-- </div> -->
<!-- </template> --> 
