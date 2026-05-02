<script lang="ts">
  interface EducationDetail { label: string; value: string; }
  interface Education {
    degree: string;
    institution: string;
    institutionUrl?: string;
    period: string;
    details: EducationDetail[];
  }

  const education: Education = {
    degree: "BSc in Computer Science",
    institution: "The Chinese University of Hong Kong",
    institutionUrl: "https://www.cse.cuhk.edu.hk/",
    period: "Sep 2017 — Jul 2021",
    details: [
      { label: "Honours", value: "Second Class Upper Division" },
      { label: "Stream",  value: "Distributed Systems, Networks and Security" },
      { label: "Minor",   value: "Japanese Language" }
    ]
  };
</script>

<section id="education" class="px-6 md:px-10 py-24 md:py-32">
  <div class="max-w-[1400px] mx-auto">

    <header class="grid grid-cols-12 gap-6 md:gap-10 mb-16 md:mb-24 reveal">
      <div class="col-span-12 md:col-span-3">
        <div class="folio">§03</div>
      </div>
      <div class="col-span-12 md:col-span-9">
        <div class="rule-thick pt-3">
          <div class="label mb-2">Section Three</div>
          <h2 class="font-display text-[2.5rem] md:text-[3.75rem] leading-[1] tracking-[-0.02em]" style="font-variation-settings: 'opsz' 144, 'SOFT' 30, 'wght' 380;">
            Where I <span style="font-style: italic;">studied.</span>
          </h2>
        </div>
      </div>
    </header>

    <article class="grid grid-cols-12 gap-6 md:gap-10 reveal">
      <aside class="col-span-12 md:col-span-3">
        <div class="md:sticky md:top-24">
          <div class="label">01 / 01</div>
          <div class="font-mono text-sm mt-2">{education.period}</div>
          <div class="font-mono text-xs text-muted mt-1">Sha Tin, HK</div>
        </div>
      </aside>

      <div class="col-span-12 md:col-span-9">
        <div class="rule pt-5">
          <h3 class="font-display text-[2rem] md:text-[3rem] leading-[1.02] tracking-[-0.025em] mb-3" style="font-variation-settings: 'opsz' 144, 'SOFT' 30, 'wght' 380;">
            {education.degree}<span class="text-accent">.</span>
          </h3>
          <p class="font-serif-body italic text-[1.18rem] text-ink-soft mb-10">
            {#if education.institutionUrl}
              <a href={education.institutionUrl} target="_blank" rel="noopener noreferrer" class="editorial-link">{education.institution}</a>
            {:else}{education.institution}{/if}
          </p>

          <div>
            {#each education.details as detail}
              <div class="spec-row">
                <span class="label">{detail.label}</span>
                <span class="font-serif-body text-[1.05rem]">{detail.value}</span>
              </div>
            {/each}
          </div>
        </div>
      </div>
    </article>
  </div>
</section>
