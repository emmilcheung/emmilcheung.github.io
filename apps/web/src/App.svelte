<script lang="ts">
  import Hero from './components/Hero.svelte';
  import Experience from './components/Experience.svelte';
  import Projects from './components/Projects.svelte';
  import Education from './components/Education.svelte';
  import Certifications from './components/Certifications.svelte';
  import Skills from './components/Skills.svelte';
  import Footer from './components/Footer.svelte';
  import { ChatWidget } from '@emmil/chat-widget';

  const chatApiUrl = import.meta.env.VITE_CHAT_URL ?? '';
</script>

<main class="min-h-screen">
  <Hero />
  <Experience />
  <Projects />
  <Education />
  <Certifications />
  <Skills />
  <Footer />
</main>

{#if chatApiUrl}
  <ChatWidget
    apiUrl={chatApiUrl}
    title="Ask about Emmil"
    placeholder="Ask about my experience, skills, projects..."
  />
{/if}
