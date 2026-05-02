<script lang="ts">
  // Editorial hero — no runtime state required.
  const today = new Date().toLocaleDateString('en-GB', { day: '2-digit', month: 'long', year: 'numeric' });
</script>

<section id="hero" class="relative min-h-screen px-6 md:px-10 pt-24 pb-20 overflow-hidden">
  <div class="max-w-[1400px] mx-auto h-full">

    <!-- Top meta strip: a printed-paper "issue" line -->
    <div class="rule-thick pt-3 mb-10 flex flex-wrap items-baseline justify-between gap-4 text-xs font-mono uppercase tracking-[0.18em] text-ink-soft">
      <span>Vol. I — Issue 03</span>
      <span class="text-muted hidden sm:inline">A field record of cloud-native engineering</span>
      <span>{today}</span>
    </div>

    <!-- Asymmetric grid: large name on left, columned intro on right -->
    <div class="grid grid-cols-12 gap-6 md:gap-10">

      <!-- Decorative running header -->
      <div class="col-span-12 mb-2 reveal">
        <div class="label">— Folio Personnel · CV / Portfolio</div>
      </div>

      <!-- Massive serif name, breaking the grid -->
      <div class="col-span-12 reveal" style="transition-delay: 80ms;">
        <h1 class="hero-name text-[15vw] md:text-[13.5vw] leading-[0.86]">
          <span class="block">Emmil</span>
          <span class="block">
            <span class="ital">Cheung</span><span class="text-accent">.</span>
          </span>
        </h1>
      </div>

      <!-- Sub-headline + columns -->
      <div class="col-span-12 grid grid-cols-12 gap-6 md:gap-10 mt-12 md:mt-16">

        <!-- Lede column with drop cap -->
        <div class="col-span-12 md:col-span-6 lg:col-span-5 reveal" style="transition-delay: 160ms;">
          <p class="dropcap font-serif-body text-[1.15rem] md:text-[1.18rem] leading-[1.55] text-ink">
            Full-stack engineer working at the seams of distributed systems, cloud infrastructure, and the parts of the web that quietly hold a company together. Four years building and maintaining production services in Hong Kong — Node, Java, Go, AWS — across event-driven platforms, internal tools, and the occasional AI side-quest.
          </p>
          <div class="mt-8 flex flex-wrap items-center gap-x-6 gap-y-3">
            <a class="arrow-link font-mono text-sm" href="https://github.com/emmilcheung" target="_blank" rel="noopener noreferrer">
              <span>GitHub</span><span class="arrow">→</span>
            </a>
            <a class="arrow-link font-mono text-sm" href="https://www.linkedin.com/in/emmil-cheung/" target="_blank" rel="noopener noreferrer">
              <span>LinkedIn</span><span class="arrow">→</span>
            </a>
            <a class="arrow-link font-mono text-sm" href="mailto:emmilcheung2005@gmail.com">
              <span>Mail</span><span class="arrow">→</span>
            </a>
          </div>
        </div>

        <!-- Specifications column — like a printed product sheet -->
        <div class="col-span-12 md:col-span-5 md:col-start-8 reveal" style="transition-delay: 240ms;">
          <div class="label mb-3">Specifications</div>
          <div>
            <div class="spec-row">
              <span class="label">Role</span>
              <span class="font-serif-body text-[1.02rem]">Full-stack Developer · Cloud Native</span>
            </div>
            <div class="spec-row">
              <span class="label">Located</span>
              <span class="font-serif-body text-[1.02rem]">Sha Tin, Hong Kong</span>
            </div>
            <div class="spec-row">
              <span class="label">Years</span>
              <span class="font-serif-body text-[1.02rem]">2021 — present</span>
            </div>
            <div class="spec-row">
              <span class="label">Stack</span>
              <span class="font-serif-body text-[1.02rem]">Node · Java · Go · TS · AWS · K8s</span>
            </div>
            <div class="spec-row">
              <span class="label">Status</span>
              <span class="font-serif-body text-[1.02rem]">
                <span class="inline-block w-2 h-2 bg-accent rounded-full mr-2 align-middle" aria-hidden></span>Open to opportunities
              </span>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- Bottom marker — page folio + scroll cue -->
    <div class="mt-20 md:mt-28 flex items-end justify-between text-xs font-mono uppercase tracking-[0.18em] text-muted reveal" style="transition-delay: 320ms;">
      <div class="flex items-center gap-3">
        <span class="inline-block w-10 h-px bg-ink"></span>
        <span>Page 01 / 06</span>
      </div>
      <a href="#work" class="arrow-link" aria-label="Scroll to work">
        <span>Continue</span><span class="arrow">↓</span>
      </a>
    </div>
  </div>
</section>
