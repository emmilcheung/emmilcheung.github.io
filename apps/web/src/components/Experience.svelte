<script lang="ts">
  interface SubProject {
    name: string;
    desc: string;
    metric: string;
    url?: string;
  }

  interface ExperienceItem {
    period: string;
    duration: string;
    location: string;
    roleTag: string;
    title: string;
    company: string;
    companyAccent?: boolean;
    companyUrl?: string;
    summary: string;
    projects?: SubProject[];
    stack: string[];
  }

  const experiences: ExperienceItem[] = [
    {
      period: "Aug 2021 — Aug 2025",
      duration: "~4 years · current",
      location: "Hong Kong",
      roleTag: "Software Developer · Programmer",
      title: "Software Developer",
      company: "Zensis Limited",
      companyAccent: true,
      companyUrl: "https://www.zensis.com/",
      summary: "Owned cloud-native client applications end-to-end — requirement analysis, architecture, build, deploy, and on-call. Worked across backend, frontend, and DevOps. Established GitOps + CI/CD across the org, cutting deploy lead time by 50%+.",
      projects: [
        { name: "Wilson Group · staff comms", desc: "Multi-tenant SaaS backend on AWS + MongoDB Atlas. Service-oriented, tenant-aware, RBAC.", metric: "5,000+ active employees", url: "https://www.zensis.com/portfolio/wilson-group/" },
        { name: "TrailMe · real-time trail running", desc: "Event-driven AWS serverless: Lambda, AppSync, SQS, S3. Next.js organiser admin.", metric: "20+ public events / year", url: "https://www.zensis.com/portfolio/trailme/" },
        { name: "Internal employee system", desc: "Architected revamp + migration Heroku → GCP (Cloud Run, Pub/Sub, Firestore).", metric: "~70% hosting cost cut" },
        { name: "Chatsquare · LLM product", desc: "Q&A chatbot, admin panel, feedback loop. Next.js + LangChain + Redis.", metric: "Prior LLM/RAG production work", url: "https://www.chatsquare.ai/" },
      ],
      stack: ["NodeJS", "TypeScript", "Java", "Python", "React", "AWS", "GCP", "MongoDB", "Redis", "Docker", "Terraform", "GitLab CI"],
    },
    {
      period: "Aug 2020 — Oct 2020",
      duration: "3 months · internship",
      location: "Hong Kong",
      roleTag: "Web App Development Intern",
      title: "Intern",
      company: "ponte+",
      companyAccent: true,
      companyUrl: "https://hk.linkedin.com/company/ponteplus",
      summary: "Built a mobile-first PWA for performing-arts events from scratch and shipped a functional beta in 10 weeks. Weekly direction-setting with the director, supervisor, and UI/UX designer.",
      stack: ["NodeJS", "React", "Firebase", "PWA"],
    },
    {
      period: "Feb 2017 — Oct 2020",
      duration: "3.5 years · part-time",
      location: "Hong Kong",
      roleTag: "Customer Service · Part-time",
      title: "Customer Service Assistant",
      company: "The Commercial Press HK",
      companyAccent: false,
      companyUrl: "https://www.commercialpress.com.hk/ww/index.html",
      summary: "Retail role during school + uni. Quietly automated order comms — first production-style automation, a foreshadowing of later DevOps work.",
      stack: ["VBA", "Python", "WhatsApp Business API", "React", "Flask"],
    },
  ];
</script>

<section class="section lined" id="work">
  <div class="container">
    <div class="section-head">
      <div class="left">
        <div class="section-num">§ EXPERIENCE</div>
        <h2 class="h2">What I've shipped in production.</h2>
        <p class="sublead">Four years at Zensis on cloud-native client work — backend, frontend, DevOps depending on the project. Before that, a PWA internship and several years of part-time work where automation crept in.</p>
      </div>
    </div>

    <div class="exp-list">
      {#each experiences as exp, i}
        <article class="exp-item reveal" style="--reveal-delay:{i * 60}ms">
          <div class="when">
            <div class="period">{exp.period}</div>
            <div class="duration">{exp.duration}</div>
            <div class="loc">📍 {exp.location}</div>
          </div>
          <div class="what">
            <div class="role-tag">{exp.roleTag}</div>
            <h3>
              {exp.title}
              <span class="at">at</span>
              {#if exp.companyUrl}
                <a href={exp.companyUrl} target="_blank" rel="noopener" class="co">{exp.company}</a>
              {:else}
                <span class="co">{exp.company}</span>
              {/if}
            </h3>
            <p class="summary">{exp.summary}</p>

            {#if exp.projects}
              <div class="exp-projects">
                {#each exp.projects as proj}
                  <div class="exp-project">
                    <div class="name">
                      {proj.name}
                      {#if proj.url}<span class="arrow-out">↗</span>{/if}
                    </div>
                    <div class="desc">{proj.desc}</div>
                    <div class="metric">{proj.metric}</div>
                  </div>
                {/each}
              </div>
            {/if}

            <div class="exp-stack">
              {#each exp.stack as tech}
                <span class="stack-tag">{tech}</span>
              {/each}
            </div>
          </div>
        </article>
      {/each}
    </div>
  </div>
</section>

<style>
  .exp-list { display: flex; flex-direction: column; }

  .exp-item {
    display: grid; grid-template-columns: 200px 1fr;
    gap: 40px;
    padding: 28px 0;
    border-top: 1px solid var(--border-soft);
  }
  .exp-item:first-child { border-top: 0; padding-top: 0; }

  .when .period {
    font-family: 'JetBrains Mono', monospace; font-size: 13px;
    color: var(--text); letter-spacing: -0.005em;
  }
  .when .duration {
    font-family: 'JetBrains Mono', monospace; font-size: 11px;
    color: var(--text-faint); margin-top: 4px;
  }
  .when .loc {
    font-family: 'JetBrains Mono', monospace; font-size: 11px;
    color: var(--text-faint); margin-top: 10px;
    display: flex; align-items: center; gap: 6px;
  }

  h3 {
    font-size: 22px; letter-spacing: -0.015em; font-weight: 600;
    margin: 0 0 4px;
    color: var(--text);
  }
  .at { color: var(--text-faint); font-weight: 400; margin: 0 4px; }
  .co { color: var(--accent); font-weight: 600; }

  .summary {
    color: var(--text-dim); font-size: 15px; margin: 10px 0 18px;
    max-width: 720px; line-height: 1.6;
  }

  .exp-projects { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 8px; }

  .exp-project {
    padding: 14px 16px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    transition: border-color 160ms;
  }
  .exp-project:hover { border-color: var(--accent-soft); }

  .name {
    font-size: 13px; font-weight: 600; color: var(--text);
    display: flex; align-items: center; gap: 8px;
    margin-bottom: 4px;
  }
  .arrow-out { color: var(--text-faint); font-size: 11px; transition: color 160ms; }
  .exp-project:hover .arrow-out { color: var(--accent); }

  .desc { font-size: 13px; color: var(--text-dim); line-height: 1.5; }

  .metric {
    margin-top: 8px;
    font-family: 'JetBrains Mono', monospace; font-size: 11px;
    color: var(--accent);
  }

  .exp-stack { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 14px; }

  @media (max-width: 768px) {
    .exp-item {
      grid-template-columns: 1fr;
      gap: 16px;
      padding: 28px 0;
    }
    .when { display: flex; flex-wrap: wrap; align-items: center; gap: 8px 14px; }
    .when .loc { margin-top: 0; }
    h3 { font-size: 20px; }
    .summary { font-size: 14px; }
    .exp-projects { grid-template-columns: 1fr; }
  }
</style>
