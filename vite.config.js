// vite.config.js
import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  root: resolve('./src/static'),

  // Onde os arquivos estarão acessíveis no navegador
  base: '/static/dist/',

  build: {
    // Onde salvar o build final.
    outDir: resolve(__dirname, 'src/static/dist'),
    
    manifest: true,
    emptyOutDir: true, // Limpa 'src/static/dist' antes de buildar
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'src/static/src/main.js'),
      },
    },
  },

  server: {
    host: 'localhost',
    port: 5173,
    open: false,
    origin: 'http://localhost:5173',
    watch: {
      usePolling: true,
    }
  },
});