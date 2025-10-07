<script setup>
import { ref } from 'vue'
import axios from 'axios'
import Logo from '../../icons/Logo.vue'

const step = ref(1)
const error = ref('')
const success = ref(false)

const formRegister = ref({
  username: '',
  email: '',
  password: '',
  confirmPassword: '',
  first_name: '',
  last_name: '',
  phone: '',
  role: ''
})

// Ir al siguiente paso
const nextStep = () => {
  error.value = ''
  if (!formRegister.value.username || !formRegister.value.email || !formRegister.value.password) {
    error.value = 'Completa todos los campos.'
    return
  }
  if (formRegister.value.password !== formRegister.value.confirmPassword) {
    error.value = 'Las contraseñas no coinciden.'
    return
  }
  step.value = 2
}

// Regresar
const prevStep = () => {
  step.value = 1
}

// Enviar al backend
const handleSubmit = async () => {
  error.value = ''
  try {
    const response = await axios.post('http://127.0.0.1:8000/auth/users/', {
      username: formRegister.value.username,
      email: formRegister.value.email,
      password: formRegister.value.password,
      profile: {
        nombre: formRegister.value.first_name,
        apellido: formRegister.value.last_name,
        telefono: formRegister.value.phone,
        role: formRegister.value.role
      }
    })

    console.log('✅ Registro exitoso:', response.data)
    success.value = true
    step.value = 1
    Object.keys(formRegister.value).forEach(key => (formRegister.value[key] = ''))
  } catch (err) {
    console.error(err)
    error.value = 'Error al registrar. Intenta nuevamente.'
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
            {{ step === 1 ? 'Crear cuenta' : 'Completar perfil' }}
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
                  Sign Up with Google
                </span>
              </button>

            </div>

            <div class="my-12 border-b text-center">
              <div
                class="leading-none px-2 inline-block text-sm text-gray-600 tracking-wide font-medium bg-white transform translate-y-1/2 dark:bg-gray-800 dark:text-slate-50">
                Registrate con Correo y Contraseña
              </div>
            </div>

            <form @submit.prevent="handleSubmit" class="mx-auto max-w-xs">
              <div v-if="step === 1" class="space-y-1">
                <!-- username -->
                <input v-model="formRegister.username"
                  class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white  dark:text-gray-800"
                  type="username" placeholder="Usuario" required />
                <!-- correo -->
                <input v-model="formRegister.email"
                  class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-3  dark:text-gray-800"
                  type="email" placeholder="Correo" required />
                <!-- contraseña -->
                <input v-model="formRegister.password"
                  class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-3  dark:text-gray-800"
                  type="password" placeholder="Contraseña" required />
                <!-- confirmar contraseña -->
                <input v-model="formRegister.confirmPassword"
                  class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-3  dark:text-gray-800"
                  type="password" placeholder="Confirmar Contraseña" required />

                <!-- Boton Continuar -->
                <button @click="nextStep"
                  class="mt-5 tracking-wide font-semibold bg-gray-800 text-gray-100 w-full py-4 rounded-lg
                   hover:bg-gray-700 transition-all duration-300 ease-in-out flex items-center justify-center 
                   focus:shadow-outline focus:outline-none  dark:bg-orange-600 dark:hover:bg-orange-700">
                  <svg class="w-6 h-6 -ml-2" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                    stroke-linejoin="round">
                    <path d="M16 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2" />
                    <circle cx="8.5" cy="7" r="4" />
                    <path d="M20 8v6M23 11h-6" />
                  </svg>
                  <span class="ml-3">
                    Continuar
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

              <!-- Paso 2 -->
              <div v-else class="space-y-4">
                <!-- Nombre -->
                <input v-model="formRegister.first_name"
                  class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white dark:text-gray-800"
                  type="text" placeholder="Nombre" required />
                <!-- Apellido -->
                <input v-model="formRegister.last_name"
                  class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white dark:text-gray-800"
                  type="text" placeholder="Apellido" required />
                <!-- Telefono -->
                <input v-model="formRegister.phone"
                  class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white dark:text-gray-800"
                  type="tel" placeholder="Telefono" required />
                <!-- Rol -->
                <div>
                  <select v-model="formRegister.role"
                    class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white dark:text-gray-800"
                    required>
                    <option value="">Rol</option>
                    <option class="" value="player">Jugador</option>
                    <option value="admin">Organizador</option>
                  </select>
                </div>

                <div class="flex-col justify-between mt-4">
                  <button type="button" @click="prevStep"
                    class="mt-4 tracking-wide font-semibold bg-gray-800 text-gray-100 w-full py-4 rounded-lg hover:bg-gray-700 transition-all duration-300 ease-in-out flex items-center justify-center focus:shadow-outline focus:outline-none dark:bg-orange-600 dark:hover:bg-orange-700">
                    Atrás
                  </button>
                  <button type="submit"
                    class="mt-4 tracking-wide font-semibold bg-gray-800 text-gray-100 w-full py-4 rounded-lg hover:bg-gray-700 transition-all duration-300 ease-in-out flex items-center justify-center focus:shadow-outline focus:outline-none dark:bg-orange-600 dark:hover:bg-orange-700">
                    Registrar
                  </button>
                </div>
              </div>

            </form>
            <!-- Mensajes -->
            <p v-if="error" class="text-red-600 text-center mt-4">{{ error }}</p>
            <p v-if="success" class="text-green-600 text-center mt-4">
              ¡Registro exitoso! 🎉
            </p>
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
