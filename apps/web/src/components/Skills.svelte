<script lang="ts">
  interface SkillRow { name: string; level: number; }
  interface SkillCategory { title: string; count: number; items: SkillRow[]; }

  const categories: SkillCategory[] = [
    {
      title: "Languages", count: 6,
      items: [
        { name: "TypeScript", level: 5 },
        { name: "Java", level: 4 },
        { name: "Python", level: 4 },
        { name: "Go", level: 3 },
        { name: "SQL", level: 4 },
        { name: "HTML/CSS", level: 4 },
      ],
    },
    {
      title: "Backend & APIs", count: 7,
      items: [
        { name: "NestJS / Express.js", level: 5 },
        { name: "Serverless Framework", level: 4 },
        { name: "Spring Boot", level: 3 },
        { name: "Flask / FastAPI", level: 3 },
        { name: "gRPC", level: 3 },
        { name: "GraphQL · Apollo", level: 3 },
      ],
    },
    {
      title: "Cloud & Infra", count: 8,
      items: [
        { name: "AWS Lambda", level: 5 },
        { name: "AWS AppSync", level: 4 },
        { name: "GCP Cloud Run", level: 4 },
        { name: "Kubernetes", level: 3 },
        { name: "Docker", level: 5 },
        { name: "Terraform", level: 4 },
        { name: "GitLab CI", level: 5 },
        { name: "Kafka", level: 3 },
      ],
    },
    {
      title: "Data & Frontend", count: 7,
      items: [
        { name: "PostgreSQL", level: 4 },
        { name: "MongoDB", level: 5 },
        { name: "Redis", level: 5 },
        { name: "DynamoDB", level: 3 },
        { name: "React · Next.js", level: 5 },
        { name: "Svelte", level: 3 },
        { name: "Playwright · Jest", level: 4 },
      ],
    },
  ];
</script>

<section class="section lined" id="stack">
  <div class="container">
    <div class="section-head reveal">
      <div class="left">
        <div class="section-num">§ STACK</div>
        <h2 class="h2">Tools I reach for.</h2>
        <p class="sublead">Production-tested. Filled dots indicate depth of use — open dots are working knowledge.</p>
      </div>
    </div>

    <div class="stack-grid reveal" style="--reveal-delay:60ms">
      {#each categories as cat}
        <div class="stack-cat">
          <div class="cat-head">
            <div class="cat-name">{cat.title}</div>
            <div class="cat-count">{String(cat.count).padStart(2, '0')}</div>
          </div>
          <div class="items">
            {#each cat.items as item}
              <div class="row">
                <span class="skill-name">{item.name}</span>
                <span class="lvl">
                  {#each Array(5) as _, d}
                    <span class:on={d < item.level}></span>
                  {/each}
                </span>
              </div>
            {/each}
          </div>
        </div>
      {/each}
    </div>
  </div>
</section>

<style>
  .stack-grid {
    display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px;
  }

  .stack-cat {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 22px;
  }

  .cat-head {
    display: flex; align-items: center; justify-content: space-between;
    margin-bottom: 14px; padding-bottom: 14px;
    border-bottom: 1px solid var(--border);
  }
  .cat-name { font-size: 13px; font-weight: 600; color: var(--text); }
  .cat-count {
    font-family: 'JetBrains Mono', monospace; font-size: 10px;
    color: var(--text-faint);
  }

  .items { display: flex; flex-direction: column; gap: 9px; }

  .row { display: flex; align-items: center; justify-content: space-between; font-size: 13px; }

  .skill-name {
    color: var(--text);
    font-family: 'JetBrains Mono', monospace; font-size: 12px;
  }

  .lvl { display: flex; gap: 3px; }
  .lvl span {
    width: 6px; height: 6px; border-radius: 50%;
    background: var(--surface-2); border: 1px solid var(--border);
  }
  .lvl span.on { background: var(--accent); border-color: var(--accent); }

  @media (max-width: 1024px) {
    .stack-grid { grid-template-columns: repeat(2, 1fr); }
  }

  @media (max-width: 768px) {
    .stack-grid { grid-template-columns: 1fr; gap: 12px; }
    .stack-cat { padding: 18px; }
  }
</style>
