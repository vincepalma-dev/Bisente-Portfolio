import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  site: 'https://markvincentpalma.vercel.app',
  // Jarvis.AI was rebuilt as JULI
  redirects: { '/projects/jarvis-ai': '/projects/juli' },
});
