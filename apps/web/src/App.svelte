<script lang="ts">
  import { onMount } from 'svelte';
  import Hero from './components/Hero.svelte';
  import Experience from './components/Experience.svelte';
  import Projects from './components/Projects.svelte';
  import Education from './components/Education.svelte';
  import Certifications from './components/Certifications.svelte';
  import Skills from './components/Skills.svelte';
  import HowItWorks from './components/HowItWorks.svelte';
  import Footer from './components/Footer.svelte';
  import { ChatWidget } from '@emmil/chat-widget';

  const chatApiUrl = import.meta.env.VITE_CHAT_URL ?? '';
  const THEME_KEY = 'profolio-theme';

  let mobileMenuOpen = $state(false);

  const navLinks = [
    { href: '#work',           label: 'Work' },
    { href: '#projects',       label: 'Projects' },
    { href: '#education',      label: 'Education' },
    { href: '#certifications', label: 'Certs' },
    { href: '#stack',          label: 'Stack' },
    { href: '#how',            label: 'How it works' },
  ];

  onMount(() => {
    try {
      const saved = localStorage.getItem(THEME_KEY);
      if (saved === 'light') document.documentElement.setAttribute('data-theme', 'light');
    } catch (_) {}
  });

  function toggleTheme() {
    const root = document.documentElement;
    const isLight = root.getAttribute('data-theme') === 'light';
    if (isLight) root.removeAttribute('data-theme');
    else root.setAttribute('data-theme', 'light');
    try { localStorage.setItem(THEME_KEY, isLight ? 'dark' : 'light'); } catch (_) {}
  }

  function closeMobileMenu() {
    mobileMenuOpen = false;
  }
</script>

<nav class="site-nav">
  <div class="container nav-inner">
    <a href="#hero" class="nav-brand">
      <span class="brand-glyph">E</span>
      <span class="brand-text">emmilcheung<span class="brand-accent">.dev</span></span>
    </a>

    <div class="nav-links">
      {#each navLinks as link}
        <a href={link.href}>{link.label}</a>
      {/each}
    </div>

    <div class="nav-right">
      <span class="pill live nav-available">Available</span>
      <button class="theme-toggle" onclick={toggleTheme} aria-label="Toggle theme">
        <svg class="icon moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
        <svg class="icon sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg>
      </button>
      <!-- <a class="btn nav-resume" href="mailto:">Contact me</a> -->
      <button
        class="hamburger"
        onclick={() => (mobileMenuOpen = !mobileMenuOpen)}
        aria-label={mobileMenuOpen ? 'Close menu' : 'Open menu'}
        aria-expanded={mobileMenuOpen}
      >
        {#if mobileMenuOpen}
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M18 6 6 18M6 6l12 12"/></svg>
        {:else}
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M3 12h18M3 6h18M3 18h18"/></svg>
        {/if}
      </button>
    </div>
  </div>

  {#if mobileMenuOpen}
    <div class="mobile-menu">
      {#each navLinks as link}
        <a href={link.href} onclick={closeMobileMenu}>{link.label}</a>
      {/each}
      <div class="mobile-menu-footer">
        <span class="pill live">Available</span>
      </div>
    </div>
  {/if}
</nav>

<main>
  <Hero />
  <Experience />
  <Projects />
  <Education />
  <Certifications />
  <Skills />
  <HowItWorks />
  <Footer />
</main>

{#if chatApiUrl}
  <ChatWidget
    apiUrl={chatApiUrl}
    title="Ask about Emmil"
    placeholder="Ask about my experience, skills, projects..."
  />
{/if}

<style>
  .site-nav {
    position: sticky; top: 0; z-index: 50;
    background: var(--nav-bg);
    backdrop-filter: blur(14px);
    border-bottom: 1px solid var(--border-soft);
  }
  .nav-inner {
    display: flex; align-items: center; justify-content: space-between;
    height: 60px;
  }
  .nav-brand {
    display: flex; align-items: center; gap: 10px;
    font-family: 'JetBrains Mono', monospace; font-size: 13px;
    color: var(--text); flex-shrink: 0;
  }
  .brand-glyph {
    width: 26px; height: 26px; border-radius: 7px;
    background: linear-gradient(135deg, var(--accent), var(--violet));
    color: var(--on-accent);
    display: grid; place-items: center;
    font-weight: 800; font-size: 14px;
    font-family: 'Inter', sans-serif;
    box-shadow: 0 0 18px var(--accent-glow);
  }
  .brand-accent { color: var(--accent); }

  .nav-links {
    display: flex; gap: 24px;
    font-size: 13px; color: var(--text-dim);
  }
  .nav-links a { transition: color 160ms; white-space: nowrap; }
  .nav-links a:hover { color: var(--text); }

  .nav-right { display: flex; align-items: center; gap: 10px; flex-shrink: 0; }
  .nav-resume { font-size: 13px; padding: 8px 14px; }

  .hamburger {
    display: none;
    width: 34px; height: 34px;
    background: none; border: none; cursor: pointer;
    color: var(--text-dim);
    align-items: center; justify-content: center;
    border-radius: 6px; padding: 5px;
    transition: color 160ms, background 160ms;
  }
  .hamburger svg { width: 18px; height: 18px; }
  .hamburger:hover { color: var(--text); background: var(--surface); }

  /* Mobile dropdown */
  .mobile-menu {
    display: flex; flex-direction: column;
    border-top: 1px solid var(--border-soft);
    background: var(--nav-bg);
    backdrop-filter: blur(14px);
    padding: 8px 0 16px;
    animation: menuDown 180ms cubic-bezier(0.2, 0.7, 0.2, 1);
  }
  @keyframes menuDown {
    from { opacity: 0; transform: translateY(-6px); }
    to   { opacity: 1; transform: none; }
  }
  .mobile-menu a {
    padding: 12px var(--container-px, 24px);
    font-size: 15px; color: var(--text-dim);
    transition: color 160ms, background 160ms;
  }
  .mobile-menu a:hover { color: var(--text); background: var(--surface); }
  .mobile-menu-footer {
    padding: 10px var(--container-px, 24px) 0;
    margin-top: 4px;
    border-top: 1px solid var(--border-soft);
  }

  @media (max-width: 900px) {
    .nav-links { gap: 18px; }
  }

  @media (max-width: 768px) {
    .nav-links, .nav-available { display: none !important; }
    .hamburger { display: flex; }
    .nav-inner { height: 56px; }
    .brand-text { font-size: 12px; }
  }

  @media (max-width: 400px) {
    .nav-resume { display: none; }
  }
</style>
