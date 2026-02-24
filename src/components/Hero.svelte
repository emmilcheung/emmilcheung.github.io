<script lang="ts">
  import { onMount } from 'svelte';
  
  let visible = false;
  
  onMount(() => {
    setTimeout(() => visible = true, 100);
  });
</script>

<section id="hero" class="relative min-h-screen flex items-center justify-center px-4 py-20 overflow-hidden">
  <!-- Organic background blobs -->
  <div class="absolute inset-0 bg-gradient-to-br from-amber-50 via-orange-50 to-rose-50 dark:from-slate-900 dark:via-slate-800 dark:to-slate-900 -z-10"></div>
  <div class="absolute top-20 right-10 w-96 h-96 bg-amber-200/30 dark:bg-amber-900/20 blob animate-pulse" style="animation-duration: 4s;"></div>
  <div class="absolute bottom-20 left-10 w-80 h-80 bg-rose-200/30 dark:bg-rose-900/20 blob-2 animate-pulse" style="animation-duration: 5s; animation-delay: 1s;"></div>
  
  <div class="max-w-5xl mx-auto text-center relative z-10" class:opacity-100={visible} class:opacity-0={!visible}>
    <!-- Handwritten accent -->
    <div class="handwriting text-3xl md:text-4xl text-amber-600 dark:text-amber-400 mb-2 transform -rotate-2">
      Hey, I'm
    </div>
    <h1 class="text-5xl md:text-7xl font-bold mb-4 text-slate-800 dark:text-slate-100 tracking-tight">
      Emmil Cheung
    </h1>
    <div class="inline-block px-4 py-1 bg-amber-100 dark:bg-amber-900/30 rounded-full mb-8 transform rotate-1">
      <p class="text-lg md:text-xl text-slate-700 dark:text-slate-300 font-medium">
        Full Stack Developer · Cloud Native Enthusiast
      </p>
    </div>
    
    <div class="flex flex-wrap justify-center gap-6 mb-12 text-slate-600 dark:text-slate-400">
      <div class="flex items-center gap-2 px-3 py-1.5 bg-white/60 dark:bg-slate-800/60 rounded-lg backdrop-blur-sm">
        <svg class="w-4 h-4 text-amber-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
        </svg>
        <span class="text-sm">Sha Tin, Hong Kong</span>
      </div>
      
      <div class="flex items-center gap-2 px-3 py-1.5 bg-white/60 dark:bg-slate-800/60 rounded-lg backdrop-blur-sm">
        <svg class="w-4 h-4 text-amber-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
        </svg>
        <a href="mailto:emmilcheung2005@gmail.com" class="hover:text-amber-600 transition-colors text-sm">
          emmilcheung2005@gmail.com
        </a>
      </div>
      
      <!-- <div class="flex items-center gap-2 px-3 py-1.5 bg-white/60 dark:bg-slate-800/60 rounded-lg backdrop-blur-sm">
        <span class="text-amber-600">📱</span>
        <span class="text-sm">+852 51651223</span>
      </div> -->
    </div>
    
    <div class="flex justify-center gap-4">
      <a 
        href="https://github.com/emmilcheung" 
        target="_blank"
        rel="noopener noreferrer"
        class="flex items-center gap-2 px-6 py-3 bg-slate-800 dark:bg-slate-700 text-white rounded-2xl hover:bg-slate-700 dark:hover:bg-slate-600 transition-all hover:-translate-y-1 shadow-md hover:shadow-xl transform rotate-1"
      >
        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
          <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
        </svg>
        <span class="font-medium">GitHub</span>
      </a>
      
      <a 
        href="https://www.linkedin.com/in/emmil-cheung/" 
        target="_blank"
        rel="noopener noreferrer"
        class="flex items-center gap-2 px-6 py-3 bg-amber-500 dark:bg-amber-600 text-white rounded-2xl hover:bg-amber-600 dark:hover:bg-amber-700 transition-all hover:-translate-y-1 shadow-md hover:shadow-xl transform -rotate-1"
      >
        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
          <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
        </svg>
        <span class="font-medium">LinkedIn</span>
      </a>
    </div>
    
    <div class="mt-20">
      <div class="handwriting text-xl text-amber-600 dark:text-amber-400 mb-3 animate-bounce">
        Scroll to see more ↓
      </div>
    </div>
  </div>
</section>

<style>
  .opacity-0 {
    opacity: 0;
    transform: translateY(30px);
  }
  
  .opacity-100 {
    opacity: 1;
    transform: translateY(0);
    transition: all 1s cubic-bezier(0.34, 1.56, 0.64, 1);
  }
</style>
