<script lang="ts">
  interface ProjectHighlight {
    title: string;
    description: string;
  }

  interface Project {
    title: string;
    subtitle: string;
    githubUrl?: string;
    techStack: string[];
    highlights: ProjectHighlight[];
  }

  const projects: Project[] = [
    {
      title: "Ticketing Platform",
      subtitle: "Polyglot event-ticketing system built across eight independently deployable microservices.",
      githubUrl: "https://github.com/emmilcheung/k8s-multi-language-gRPC-microservice",
      techStack: ["Go", "Java", "Spring Boot", "TypeScript", "NestJS", "Next.js", "PostgreSQL", "MongoDB", "Redis", "Kafka", "gRPC", "Kubernetes", "GraphQL", "Kong"],
      highlights: [
        {
          title: "Polyglot Microservices Architecture",
          description: "Designed and built a polyglot event-ticketing platform comprising 8 independently deployable microservices with per-service data ownership, Apache Kafka event-driven fan-out, and saga-based order orchestration via transactional outbox."
        },
        {
          title: "Real-time Seat Reservation",
          description: "Implemented real-time seat reservation via dual-write: Redis hot path for sub-second holds with PostgreSQL as source of truth, gRPC contracts between services, and SSE push for live seat-map updates across manual and auto-assign modes."
        },
        {
          title: "GraphQL Federation Gateway & REST APIs",
          description: "Built a GraphQL Federation gateway (Apollo Router, 6 subgraphs) and REST APIs through Kong with RS256 JWT/JWKS auth, rate limiting, CSRF protection, and DB-less config — supporting both client-facing and inter-service query patterns."
        }
      ]
    }
  ];
</script>

<section id="projects" class="px-6 md:px-10 py-24 md:py-32 bg-paper-deep/40">
  <div class="max-w-[1400px] mx-auto">

    <!-- Section header -->
    <header class="grid grid-cols-12 gap-6 md:gap-10 mb-16 md:mb-24 reveal">
      <div class="col-span-12 md:col-span-3">
        <div class="folio">§02</div>
      </div>
      <div class="col-span-12 md:col-span-9">
        <div class="rule-thick pt-3">
          <div class="label mb-2">Section Two</div>
          <h2 class="font-display text-[2.5rem] md:text-[3.75rem] leading-[1] tracking-[-0.02em]" style="font-variation-settings: 'opsz' 144, 'SOFT' 30, 'wght' 380;">
            Selected <span style="font-style: italic;">projects.</span>
          </h2>
          <p class="mt-4 max-w-xl font-serif-body text-ink-soft text-[1.02rem] leading-relaxed">
            Side work, experiments, and longer-running studies. Source available on GitHub where indicated.
          </p>
        </div>
      </div>
    </header>

    <div class="space-y-24">
      {#each projects as project, i}
        <article class="grid grid-cols-12 gap-6 md:gap-10 reveal">

          <!-- Index rail -->
          <aside class="col-span-12 md:col-span-3">
            <div class="md:sticky md:top-24">
              <div class="label">Project {String(i + 1).padStart(2, '0')}</div>
              <div class="font-mono text-xs text-muted mt-2 leading-relaxed">
                <div>Type — Personal / OSS</div>
                <div>Status — In progress</div>
                <div>Year — 2024–25</div>
              </div>
              {#if project.githubUrl}
                <div class="mt-5">
                  <a href={project.githubUrl} target="_blank" rel="noopener noreferrer" class="arrow-link font-mono text-sm">
                    <span>Source on GitHub</span><span class="arrow">→</span>
                  </a>
                </div>
              {/if}
            </div>
          </aside>

          <!-- Content -->
          <div class="col-span-12 md:col-span-9">
            <div class="rule pt-5">
              <h3 class="font-display text-[2rem] md:text-[3rem] leading-[1.02] tracking-[-0.025em] mb-3" style="font-variation-settings: 'opsz' 144, 'SOFT' 30, 'wght' 380;">
                <span class="text-accent mr-2">¶</span>{project.title}<span class="text-accent">.</span>
              </h3>
              <p class="font-serif-body italic text-[1.18rem] text-ink-soft max-w-2xl leading-snug mb-8">
                {project.subtitle}
              </p>

              <div class="mb-10">
                <div class="label mb-3">Tech Stack</div>
                <div class="flex flex-wrap gap-x-5 gap-y-1">
                  {#each project.techStack as tech}
                    <span class="tag">{tech}</span>
                  {/each}
                </div>
              </div>

              <ol class="space-y-7">
                {#each project.highlights as highlight, j}
                  <li class="grid grid-cols-12 gap-3 md:gap-5">
                    <div class="col-span-2 md:col-span-1 pt-1">
                      <span class="font-mono text-xs text-accent">→ {String(j + 1).padStart(2, '0')}</span>
                    </div>
                    <div class="col-span-10 md:col-span-11">
                      <h4 class="font-display text-[1.15rem] md:text-[1.25rem] leading-snug mb-1.5" style="font-variation-settings: 'opsz' 36, 'SOFT' 30, 'wght' 520;">
                        {highlight.title}
                      </h4>
                      <p class="prose font-serif-body text-[1rem] md:text-[1.05rem] leading-[1.62] text-ink-soft max-w-prose">
                        {highlight.description}
                      </p>
                    </div>
                  </li>
                {/each}
              </ol>
            </div>
          </div>
        </article>
      {/each}
    </div>

  </div>
</section>
