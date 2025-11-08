import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import starlightConfig from './starlight.config.mjs';
import tailwindcss from '@tailwindcss/vite';
import vue from '@astrojs/vue';


export default defineConfig({
  integrations: [starlight(starlightConfig), 
    vue()],
  vite: {
    plugins: [tailwindcss()],
  },
});