<script lang="ts">
  interface SkillCategory {
    code: string;
    title: string;
    skills: string[];
  }

  const skillCategories: SkillCategory[] = [
    {
      code: "A",
      title: "Languages",
      skills: ["Java", "JavaScript", "TypeScript", "Python", "Golang", "SQL", "HTML", "CSS"]
    },
    {
      code: "B",
      title: "Frameworks",
      skills: ["Express.js", "NestJS", "ReactJS", "Next.js", "Jest", "Mocha", "Playwright", "Flask", "Spring Boot", "gRPC"]
    },
    {
      code: "C",
      title: "Tools & Platforms",
      skills: ["Git", "GitLab", "Docker", "Kubernetes", "Terraform", "MongoDB", "PostgreSQL", "Redis", "AWS", "GCP", "Firebase"]
    }
  ];

  // Flatten for marquee
  const all = skillCategories.flatMap(c => c.skills);
  const marquee = [...all, ...all];
</script>

<section id="skills" class="px-6 md:px-10 py-24 md:py-32">
  <div class="max-w-[1400px] mx-auto">

    <header class="grid grid-cols-12 gap-6 md:gap-10 mb-16 md:mb-24 reveal">
      <div class="col-span-12 md:col-span-3">
        <div class="folio">§05</div>
      </div>
      <div class="col-span-12 md:col-span-9">
        <div class="rule-thick pt-3">
          <div class="label mb-2">Section Five</div>
          <h2 class="font-display text-[2.5rem] md:text-[3.75rem] leading-[1] tracking-[-0.02em]" style="font-variation-settings: 'opsz' 144, 'SOFT' 30, 'wght' 380;">
            <span style="font-style: italic;">Toolkit</span> — a complete index.
          </h2>
        </div>
      </div>
    </header>

    <!-- Three column tabular index -->
    <div class="grid grid-cols-12 gap-6 md:gap-10 reveal">
      {#each skillCategories as category, i}
        <div class="col-span-12 md:col-span-4">
          <div class="rule pt-5 h-full">
            <div class="flex items-baseline justify-between mb-5">
              <div>
                <div class="label">Index {category.code}</div>
                <h3 class="font-display text-[1.6rem] md:text-[1.85rem] mt-1 leading-tight" style="font-variation-settings: 'opsz' 96, 'SOFT' 30, 'wght' 460;">
                  {category.title}<span class="text-accent">.</span>
                </h3>
              </div>
              <div class="font-mono text-xs text-muted">{String(category.skills.length).padStart(2, '0')} entries</div>
            </div>

            <ol>
              {#each category.skills as skill, j}
                <li class="grid grid-cols-12 items-baseline py-2.5 border-t" style="border-color: var(--rule);">
                  <span class="col-span-2 font-mono text-xs text-muted">{String(j + 1).padStart(2, '0')}</span>
                  <span class="col-span-10 font-serif-body text-[1.05rem] tracking-tight">{skill}</span>
                </li>
              {/each}
              <li class="border-t" style="border-color: var(--rule);"></li>
            </ol>
          </div>
        </div>
      {/each}
    </div>

  </div>

  <!-- Marquee — full bleed below the three columns -->
  <div class="mt-24 md:mt-32 py-8 border-y reveal" style="border-color: var(--ink);" aria-hidden="true">
    <div class="overflow-hidden whitespace-nowrap">
      <div class="marquee-track inline-block whitespace-nowrap">
        {#each marquee as skill, k}
          <span class="font-display text-[2.5rem] md:text-[4rem] leading-none mx-6 align-middle" style="font-variation-settings: 'opsz' 144, 'SOFT' 30, 'wght' 360; font-style: {k % 3 === 0 ? 'italic' : 'normal'};">
            {skill}
          </span>
          <span class="text-accent text-[2.5rem] md:text-[4rem] align-middle">·</span>
        {/each}
      </div>
    </div>
  </div>
</section>
