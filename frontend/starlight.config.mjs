import { defineConfig } from 'astro/config';

export default defineConfig({
  title: 'FutManager',
  sidebar: [
    {
      label: 'Introducción',
      items: [{ label: 'Bienvenido', slug: 'introduccion/welcome' }],
    },
    {
      label: 'Guía de Inicio',
      items: [
        { label: 'Comenzar', slug: 'guia_init/getting-started' },
        { label: 'Autenticación', slug: 'guia_init/authentication' },
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
  social: [
    {
      icon: 'github',
      label: 'GitHub',
      href: 'https://github.com/LDRK/futmanager',
    },
  ],
});
