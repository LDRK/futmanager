import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import tailwindcss from '@tailwindcss/vite';
import vue from '@astrojs/vue';


export default defineConfig({
  integrations: [starlight({
    title: 'FutManager',
   
    social: [
      { icon: 'github', label: 'GitHub', href: 'https://github.com/LDRK/futmanager' }
    ],
    sidebar: [
      {
        label: 'Introducción',
        items: [
          { label: 'Bienvenido', slug: 'introduccion/welcome' },
        ],
      },
      {
        label: 'Guia de Inicio',
        items: [
          { label: 'Comenzar', slug: 'guia_init/getting-started' },
          { label: 'Autenticacion', slug: 'guia_init/authentication' },
          { label: 'Errores', slug: 'guia_init/errors' },
          { label: 'Ejemplos', slug: 'guia_init/examples' },
        ],
      },
      {
        label: 'Endpoints',
        items: [
          { label: 'Usuarios', slug: 'endpoints/users' },
          { label: 'Torneos', slug: 'endpoints/tournaments' },
          { label: 'Partidos', slug: 'endpoints/matches' },
          { label: 'Estadísticas', slug: 'endpoints/stats' },
        ],
      },
    ],
  }), vue()],

  vite: {
    plugins: [tailwindcss()],
  },
});