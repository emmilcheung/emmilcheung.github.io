<script lang="ts">
  interface Achievement {
    title: string;
    description: string;
    descriptionHtml?: string;
  }

  interface Experience {
    title: string;
    company: string;
    companyUrl?: string;
    location: string;
    period: string;
    techStack: string[];
    achievements: Achievement[];
  }

  const experiences: Experience[] = [
    {
      title: "Programmer",
      company: "Zensis Limited",
      companyUrl: "https://www.zensis.com/",
      location: "Hong Kong",
      period: "Aug 2021 — Aug 2025",
      techStack: ["NodeJS", "Java", "Python", "React.js", "MongoDB", "Redis", "Docker", "AWS"],
      achievements: [
        {
          title: "Cloud Native Development",
          description: "Served as a key contributor and maintainer for cloud native applications throughout the full Software Development Life Cycle (SDLC), encompassing requirement analysis, technical planning, development, deployment and documentation"
        },
        {
          title: "CI/CD & DevOps",
          description: "Established GitOps and CI/CD workflows for both internal and client projects by streamlining development processes through GitLab CI, Docker, Terraform and Jenkins, achieving 50%+ reduction in time required to introduce new projects and stages"
        },
        {
          title: "System Architecture",
          description: "Facilitated the in-house system revamp by Object-Orientated Design and Dependency Injection (DI) framework in TypeScript with comprehensive unit and integration tests, achieving a 70%+ increase in code coverage and reduction in bugs report"
        },
        {
          title: "Enterprise Solutions",
          description: "Designed and developed backend services and APIs in NodeJS for the staff communication application of Wilson Group utilizing service-oriented architecture (SOA), role-based access control (RBAC) and Terraform on AWS and MongoDB Atlas, facilitating on-job training, events and information delivery within 5000+ active employees",
          descriptionHtml: 'Designed and developed backend services and APIs in NodeJS for the <a href="https://www.zensis.com/portfolio/wilson-group/" target="_blank" rel="noopener noreferrer">staff communication application</a> of Wilson Group utilizing service-oriented architecture (SOA), role-based access control (RBAC) and Terraform on AWS and MongoDB Atlas, facilitating on-job training, events and information delivery within <strong>5000+ active employees</strong>'
        },
        {
          title: "Serverless Architecture",
          description: "Managed an event-driven system and organizer panel of a real-time trail running event application under AWS serverless architecture (AWS Lambda, SQS, AppSync, S3, CloudWatch), GraphQL and Next.js, supporting 20+ public events annually",
          descriptionHtml: 'Managed an event-driven system and organizer panel of a real-time <a href="https://www.zensis.com/portfolio/trailme/" target="_blank" rel="noopener noreferrer">trail running event application</a> under AWS serverless architecture (AWS Lambda, SQS, AppSync, S3, CloudWatch), GraphQL and Next.js, supporting <strong>20+ public events annually</strong>'
        },
        {
          title: "Frontend Development",
          description: "Built front-end web applications, widgets, and UI components under React.js and modern JavaScript best practices for clients across diverse industries including 9GAG, ViuTV, Makealive, Open Up, GO PARK Sports, and government",
          descriptionHtml: 'Built front-end web applications, widgets, and UI components under React.js and modern JavaScript best practices for clients across diverse industries including <a href="https://9gag.com/" target="_blank" rel="noopener noreferrer">9GAG</a>, <a href="https://www.zensis.com/portfolio/viutv/" target="_blank" rel="noopener noreferrer">ViuTV</a>, <a href="https://makealive.com/" target="_blank" rel="noopener noreferrer">Makealive</a>, <a href="https://www.zensis.com/portfolio/openup/" target="_blank" rel="noopener noreferrer">Open Up</a>, <a href="https://www.zensis.com/portfolio/go-park-sports/" target="_blank" rel="noopener noreferrer">GO PARK Sports</a>, and <a href="https://www.zensis.com/portfolio/ipdnofakes/" target="_blank" rel="noopener noreferrer">government</a>'
        },
        {
          title: "AI Integration",
          description: "Built in-house product, Chatsquare (Q&A Chatbot, Admin panel), and feedback system with Next.js, LangChain and Redis",
          descriptionHtml: 'Built in-house product, <a href="https://www.chatsquare.ai/" target="_blank" rel="noopener noreferrer">Chatsquare</a> (Q&A Chatbot, Admin panel), and feedback system with Next.js, LangChain and Redis'
        },
        {
          title: "Legacy Maintenance",
          description: "Participated in maintenance and support routine for legacy systems in Vert.x 3 (Java), Flask (Python) and NodeJS"
        }
      ]
    },
    {
      title: "Web App Development Intern",
      company: "ponte+",
      companyUrl: "https://hk.linkedin.com/company/ponteplus",
      location: "Hong Kong",
      period: "Aug 2020 — Oct 2020",
      techStack: ["NodeJS", "React.js", "Firebase", "Adobe XD"],
      achievements: [
        {
          title: "PWA Development",
          description: "Developed a mobile-first Progressive Web App (PWA) focused on performing art events from scratch and delivered to beta"
        },
        {
          title: "Collaboration",
          description: "Participated in weekly meetings with director, supervisor and UI/UX Designer on business and development direction"
        }
      ]
    },
    {
      title: "Customer Service Assistant",
      company: "The Commercial Press (HK) Ltd",
      companyUrl: "https://www.commercialpress.com.hk/ww/index.html",
      location: "Hong Kong · Part-time",
      period: "Feb 2017 — Oct 2020",
      techStack: [],
      achievements: [
        {
          title: "Customer Operations",
          description: "Supported daily store operations, customer assistance, product purchases and inter-shop logistic arrangement"
        },
        {
          title: "Tool Development",
          description: "Built a book search web application with React.js and Flask (Python) for internal use to facilitate book search and inventory check"
        },
        {
          title: "Order Communication Automation",
          description: "Enhanced message delivery on order status updates to customers by developing automated VBA scripts integrated with WhatsApp Business API"
        }
      ]
    }
  ];
</script>

<section id="work" class="px-6 md:px-10 py-24 md:py-32">
  <div class="max-w-[1400px] mx-auto">

    <!-- Section header -->
    <header class="grid grid-cols-12 gap-6 md:gap-10 mb-16 md:mb-24 reveal">
      <div class="col-span-12 md:col-span-3">
        <div class="folio">§01</div>
      </div>
      <div class="col-span-12 md:col-span-9">
        <div class="rule-thick pt-3">
          <div class="label mb-2">Section One</div>
          <h2 class="font-display text-[2.5rem] md:text-[3.75rem] leading-[1] tracking-[-0.02em]" style="font-variation-settings: 'opsz' 144, 'SOFT' 30, 'wght' 380;">
            A working <span style="font-style: italic;">history.</span>
          </h2>
          <p class="mt-4 max-w-xl font-serif-body text-ink-soft text-[1.02rem] leading-relaxed">
            Roles, places, and the things shipped. Listed in reverse chronological order — most recent first, in the manner of a printed CV.
          </p>
        </div>
      </div>
    </header>

    <!-- Experience entries -->
    <div class="space-y-20 md:space-y-28">
      {#each experiences as exp, i}
        <article class="grid grid-cols-12 gap-6 md:gap-10 reveal" style="transition-delay: {i * 80}ms;">

          <!-- Year rail -->
          <aside class="col-span-12 md:col-span-3">
            <div class="md:sticky md:top-24">
              <div class="label">{String(i + 1).padStart(2, '0')} / {String(experiences.length).padStart(2, '0')}</div>
              <div class="font-mono text-sm mt-2 text-ink">{exp.period}</div>
              <div class="mt-1 font-mono text-xs text-muted">{exp.location}</div>
            </div>
          </aside>

          <!-- Content -->
          <div class="col-span-12 md:col-span-9">
            <div class="rule pt-5">
              <div class="flex flex-wrap items-baseline justify-between gap-x-6 gap-y-2 mb-1">
                <h3 class="font-display text-[1.85rem] md:text-[2.4rem] leading-[1.05] tracking-[-0.02em]" style="font-variation-settings: 'opsz' 96, 'SOFT' 30, 'wght' 400;">
                  {exp.title}
                </h3>
                <div class="font-mono text-xs uppercase tracking-[0.18em] text-muted">at —</div>
              </div>
              <p class="font-serif-body text-[1.15rem] italic text-ink-soft mb-6">
                {#if exp.companyUrl}
                  <a href={exp.companyUrl} target="_blank" rel="noopener noreferrer" class="editorial-link">{exp.company}</a>
                {:else}
                  {exp.company}
                {/if}
              </p>

              {#if exp.techStack.length > 0}
                <div class="mb-8">
                  <div class="label mb-3">Stack</div>
                  <div class="flex flex-wrap gap-x-5 gap-y-1">
                    {#each exp.techStack as tech}
                      <span class="tag">{tech}</span>
                    {/each}
                  </div>
                </div>
              {/if}

              <ol class="space-y-6">
                {#each exp.achievements as achievement, j}
                  <li class="grid grid-cols-12 gap-3 md:gap-5">
                    <div class="col-span-2 md:col-span-1 pt-1">
                      <span class="font-mono text-xs text-accent">→ {String(j + 1).padStart(2, '0')}</span>
                    </div>
                    <div class="col-span-10 md:col-span-11">
                      <h4 class="font-display text-[1.1rem] md:text-[1.18rem] leading-snug mb-1.5" style="font-variation-settings: 'opsz' 36, 'SOFT' 30, 'wght' 520;">
                        {achievement.title}
                      </h4>
                      <p class="prose font-serif-body text-[1rem] md:text-[1.04rem] leading-[1.6] text-ink-soft max-w-prose">
                        {#if achievement.descriptionHtml}
                          {@html achievement.descriptionHtml}
                        {:else}
                          {achievement.description}
                        {/if}
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
