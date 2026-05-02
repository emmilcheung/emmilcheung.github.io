<script lang="ts">
  interface Certification {
    code: string;
    name: string;
    issuer: string;
    issuerUrl?: string;
    date: string;
  }

  const certifications: Certification[] = [
    {
      code: "AWS-DVA",
      name: "AWS Certified Developer — Associate",
      issuer: "Amazon Web Services",
      issuerUrl: "https://www.credly.com/badges/5c8c259d-c1d2-49e7-99cf-756c7336c9e0/public_url",
      date: "Oct 2025"
    }
  ];
</script>

<section id="certifications" class="px-6 md:px-10 py-24 md:py-32 bg-paper-deep/40">
  <div class="max-w-[1400px] mx-auto">

    <header class="grid grid-cols-12 gap-6 md:gap-10 mb-16 md:mb-24 reveal">
      <div class="col-span-12 md:col-span-3">
        <div class="folio">§04</div>
      </div>
      <div class="col-span-12 md:col-span-9">
        <div class="rule-thick pt-3">
          <div class="label mb-2">Section Four</div>
          <h2 class="font-display text-[2.5rem] md:text-[3.75rem] leading-[1] tracking-[-0.02em]" style="font-variation-settings: 'opsz' 144, 'SOFT' 30, 'wght' 380;">
            <span style="font-style: italic;">Credentials</span> &amp; certificates.
          </h2>
        </div>
      </div>
    </header>

    <div class="grid grid-cols-12 gap-6 md:gap-10 reveal">
      <aside class="col-span-12 md:col-span-3">
        <div class="label">Index</div>
        <div class="font-mono text-xs text-muted mt-2">{certifications.length} on record</div>
      </aside>

      <div class="col-span-12 md:col-span-9">
        <div class="rule pt-5">
          {#each certifications as cert, i}
            <div class="grid grid-cols-12 gap-3 md:gap-5 py-7 border-b" style="border-color: var(--rule);">
              <div class="col-span-3 md:col-span-2">
                <span class="font-mono text-xs text-accent">{cert.code}</span>
                <div class="font-mono text-xs text-muted mt-1">{String(i + 1).padStart(2, '0')}</div>
              </div>
              <div class="col-span-9 md:col-span-7">
                <h3 class="font-display text-[1.35rem] md:text-[1.6rem] leading-snug mb-1" style="font-variation-settings: 'opsz' 72, 'SOFT' 30, 'wght' 460;">
                  {cert.name}
                </h3>
                <p class="font-serif-body italic text-ink-soft">
                  {#if cert.issuerUrl}
                    <a href={cert.issuerUrl} target="_blank" rel="noopener noreferrer" class="editorial-link">{cert.issuer} ↗</a>
                  {:else}{cert.issuer}{/if}
                </p>
              </div>
              <div class="col-span-12 md:col-span-3 md:text-right">
                <div class="label md:text-right">Issued</div>
                <div class="font-mono text-sm mt-1 md:text-right">{cert.date}</div>
              </div>
            </div>
          {/each}
        </div>
      </div>
    </div>
  </div>
</section>
