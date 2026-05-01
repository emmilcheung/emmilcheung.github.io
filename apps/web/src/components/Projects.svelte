<script lang="ts">
  interface ProjectHighlight {
    icon: string;
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
      title: "Ticketing Platform — Polyglot Microservices",
      subtitle: "Event ticketing system built with 8 independently deployable microservices",
      githubUrl: "https://github.com/emmilcheung/k8s-multi-language-gRPC-microservice",
      techStack: ["Go", "Java", "Spring Boot", "TypeScript", "NestJS", "Next.js", "PostgreSQL", "MongoDB", "Redis", "Kafka", "gRPC", "Kubernetes", "GraphQL", "Kong"],
      highlights: [
        {
          icon: "🏗️",
          title: "Polyglot Microservices Architecture",
          description: "Designed and built a polyglot event-ticketing platform comprising 8 independently deployable microservices with per-service data ownership, Apache Kafka event-driven fan-out, and saga-based order orchestration via transactional outbox."
        },
        {
          icon: "⚡",
          title: "Real-time Seat Reservation",
          description: "Implemented real-time seat reservation via dual-write: Redis hot path for sub-second holds with PostgreSQL as source of truth, gRPC contracts between services, and SSE push for live seat-map updates across manual and auto-assign modes."
        },
        {
          icon: "🌐",
          title: "GraphQL Federation Gateway & REST APIs",
          description: "Built a GraphQL Federation gateway (Apollo Router, 6 subgraphs) and REST APIs through Kong with RS256 JWT/JWKS auth, rate limiting, CSRF protection, and DB-less config — supporting both client-facing and inter-service query patterns."
        }
      ]
    }
  ];
</script>

<section id="projects" class="py-20 px-4 bg-gradient-to-br from-amber-50/50 to-orange-50/50 dark:from-slate-800/50 dark:to-slate-900">
  <div class="max-w-6xl mx-auto">
    <div class="text-center mb-16">
      <div class="handwriting text-2xl text-amber-600 dark:text-amber-400 mb-2">Things I've built</div>
      <h2 class="text-4xl md:text-5xl font-bold text-slate-800 dark:text-slate-100">
        Projects
      </h2>
    </div>

    <div class="space-y-8">
      {#each projects as project, i}
        <div
          class="bg-white dark:bg-slate-800 rounded-3xl p-8 hover:shadow-xl transition-all duration-300 border-2 border-amber-100 dark:border-slate-700 relative overflow-hidden"
          style="animation-delay: {i * 0.1}s"
        >
          <!-- Decorative blob -->
          <div class="absolute top-0 right-0 w-40 h-40 bg-amber-200/20 dark:bg-amber-900/10 rounded-full -mr-20 -mt-20 pointer-events-none"></div>

          <div class="flex flex-col md:flex-row md:items-start md:justify-between mb-6 relative z-10">
            <div class="mb-4 md:mb-0">
              <h3 class="text-2xl font-bold text-slate-900 dark:text-white mb-2">{project.title}</h3>
              <p class="text-slate-600 dark:text-slate-400">{project.subtitle}</p>
            </div>
            {#if project.githubUrl}
              <a
                href={project.githubUrl}
                target="_blank"
                rel="noopener noreferrer"
                class="flex items-center gap-2 px-4 py-2 bg-slate-800 dark:bg-slate-700 text-white rounded-xl hover:bg-slate-700 dark:hover:bg-slate-600 transition-all hover:-translate-y-0.5 shadow-md text-sm font-medium shrink-0"
              >
                <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                </svg>
                View on GitHub
              </a>
            {/if}
          </div>

          <div class="mb-6 p-4 bg-amber-50 dark:bg-slate-700/50 rounded-2xl border border-amber-200 dark:border-slate-600 relative z-10">
            <p class="font-semibold text-slate-700 dark:text-slate-300 mb-3 uppercase text-xs tracking-wider">
              Tech Stack
            </p>
            <div class="flex flex-wrap gap-2">
              {#each project.techStack as tech}
                <span class="px-3 py-1.5 bg-amber-100 dark:bg-amber-900/30 text-amber-900 dark:text-amber-300 rounded-full text-sm font-medium border border-amber-200 dark:border-amber-800">
                  {tech}
                </span>
              {/each}
            </div>
          </div>

          <div class="space-y-5 relative z-10">
            {#each project.highlights as highlight}
              <div class="border-l-2 border-amber-400 pl-4">
                <h4 class="font-bold text-slate-900 dark:text-white mb-2">{highlight.title}</h4>
                <p class="text-slate-700 dark:text-slate-300 leading-relaxed">{highlight.description}</p>
              </div>
            {/each}
          </div>
        </div>
      {/each}
    </div>
  </div>
</section>
