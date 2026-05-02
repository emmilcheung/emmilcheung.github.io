<script lang="ts">
  const currentYear: number = new Date().getFullYear();
</script>

<footer id="contact" class="px-6 md:px-10 pt-24 pb-10 bg-ink text-paper relative overflow-hidden">
  <div class="max-w-[1400px] mx-auto relative">

    <!-- Section header — inverted -->
    <div class="grid grid-cols-12 gap-6 md:gap-10 mb-16 md:mb-24">
      <div class="col-span-12 md:col-span-3">
        <div class="folio" style="color: var(--accent);">§06</div>
      </div>
      <div class="col-span-12 md:col-span-9">
        <div class="pt-3" style="border-top: 2px solid var(--paper);">
          <div class="font-mono text-[0.68rem] uppercase tracking-[0.18em]" style="color: var(--paper-deep); opacity: 0.7;">Section Six — Colophon</div>
          <h2 class="font-display text-[2.5rem] md:text-[5rem] leading-[1] tracking-[-0.025em] mt-2" style="font-variation-settings: 'opsz' 144, 'SOFT' 40, 'wght' 360;">
            Let's <span style="font-style: italic;">talk.</span>
          </h2>
        </div>
      </div>
    </div>

    <!-- Big email -->
    <div class="grid grid-cols-12 gap-6 md:gap-10 mb-20">
      <div class="col-span-12 md:col-span-9 md:col-start-4">
        <a href="mailto:emmilcheung2005@gmail.com" class="group block">
          <div class="font-mono text-[0.68rem] uppercase tracking-[0.18em] mb-3" style="color: var(--paper-deep); opacity: 0.7;">Write to me</div>
          <div class="font-display text-[1.75rem] md:text-[3.25rem] leading-[1.05] break-all md:break-normal transition-colors" style="font-variation-settings: 'opsz' 144, 'SOFT' 30, 'wght' 360;">
            <span class="border-b border-paper/40 group-hover:border-accent group-hover:text-accent transition-colors">
              emmilcheung2005<span style="font-style: italic;">@</span>gmail.com
            </span>
          </div>
        </a>
      </div>
    </div>

    <!-- Three-column elsewhere block -->
    <div class="grid grid-cols-12 gap-6 md:gap-10 mb-20">
      <div class="col-span-12 md:col-span-3"></div>
      <div class="col-span-12 md:col-span-9 grid grid-cols-12 gap-6">

        <div class="col-span-6 md:col-span-4">
          <div class="font-mono text-[0.68rem] uppercase tracking-[0.18em]" style="color: var(--paper-deep); opacity: 0.7;">Code</div>
          <a href="https://github.com/emmilcheung" target="_blank" rel="noopener noreferrer" class="font-display text-[1.5rem] mt-2 block hover:text-accent transition-colors" style="font-variation-settings: 'opsz' 96, 'SOFT' 30, 'wght' 380;">
            GitHub <span class="font-mono text-sm align-middle">↗</span>
          </a>
          <div class="font-mono text-xs mt-1" style="color: var(--paper-deep); opacity: 0.6;">@emmilcheung</div>
        </div>

        <div class="col-span-6 md:col-span-4">
          <div class="font-mono text-[0.68rem] uppercase tracking-[0.18em]" style="color: var(--paper-deep); opacity: 0.7;">Network</div>
          <a href="https://www.linkedin.com/in/emmil-cheung/" target="_blank" rel="noopener noreferrer" class="font-display text-[1.5rem] mt-2 block hover:text-accent transition-colors" style="font-variation-settings: 'opsz' 96, 'SOFT' 30, 'wght' 380;">
            LinkedIn <span class="font-mono text-sm align-middle">↗</span>
          </a>
          <div class="font-mono text-xs mt-1" style="color: var(--paper-deep); opacity: 0.6;">/in/emmil-cheung</div>
        </div>

        <div class="col-span-12 md:col-span-4">
          <div class="font-mono text-[0.68rem] uppercase tracking-[0.18em]" style="color: var(--paper-deep); opacity: 0.7;">Located</div>
          <div class="font-display text-[1.5rem] mt-2" style="font-variation-settings: 'opsz' 96, 'SOFT' 30, 'wght' 380;">
            Sha Tin, HK
          </div>
          <div class="font-mono text-xs mt-1" style="color: var(--paper-deep); opacity: 0.6;">22.38°N · 114.19°E</div>
        </div>
      </div>
    </div>

    <!-- Colophon line -->
    <div class="pt-6 flex flex-wrap items-baseline justify-between gap-4 text-[0.7rem] font-mono uppercase tracking-[0.18em]" style="border-top: 1px solid var(--paper); color: var(--paper-deep); opacity: 0.7;">
      <div>© {currentYear} Emmil Cheung. All rights reserved.</div>
      <div class="hidden md:block">Set in Fraunces, Newsreader &amp; JetBrains Mono.</div>
      <div>End of document — §06 / 06</div>
    </div>
  </div>
</footer>
