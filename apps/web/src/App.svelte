<script lang="ts">
  import { onMount } from 'svelte';
  import Hero from './components/Hero.svelte';
  import Experience from './components/Experience.svelte';
  import Projects from './components/Projects.svelte';
  import Education from './components/Education.svelte';
  import Certifications from './components/Certifications.svelte';
  import Skills from './components/Skills.svelte';
  import Footer from './components/Footer.svelte';
  import { ChatWidget } from '@emmil/chat-widget';

  const chatApiUrl = import.meta.env.VITE_CHAT_URL ?? '';

  onMount(() => {
    if (typeof IntersectionObserver === 'undefined') {
      document.querySelectorAll('.reveal').forEach(el => el.classList.add('in'));
      return;
    }
    const io = new IntersectionObserver((entries) => {
      for (const e of entries) {
        if (e.isIntersecting) {
          e.target.classList.add('in');
          io.unobserve(e.target);
        }
      }
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0.05 });
    document.querySelectorAll('.reveal').forEach(el => io.observe(el));
  });
</script>

<!-- Top masthead — fixed on top of paper -->
<header class="fixed top-0 inset-x-0 z-30 pointer-events-none">
  <div class="max-w-[1400px] mx-auto px-6 md:px-10 pt-5 flex items-baseline justify-between text-[0.7rem] font-mono uppercase tracking-[0.18em] text-ink-soft">
    <div class="flex items-baseline gap-3 pointer-events-auto">
      <span class="inline-block w-2 h-2 bg-accent rounded-full" aria-hidden></span>
      <span>Emmil Cheung</span>
      <span class="hidden sm:inline text-muted">— Folio MMXXVI</span>
    </div>
    <nav class="hidden md:flex items-baseline gap-6 pointer-events-auto">
      <a href="#work" class="hover:text-accent transition-colors">Work</a>
      <a href="#projects" class="hover:text-accent transition-colors">Projects</a>
      <a href="#education" class="hover:text-accent transition-colors">Education</a>
      <a href="#skills" class="hover:text-accent transition-colors">Skills</a>
      <a href="#contact" class="hover:text-accent transition-colors">Contact</a>
    </nav>
    <div class="pointer-events-auto text-muted">HKT · 22.38°N</div>
  </div>
</header>

<main class="min-h-screen pt-16">
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
