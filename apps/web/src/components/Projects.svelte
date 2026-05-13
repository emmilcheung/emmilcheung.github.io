<script lang="ts">
  // Featured project: polyglot ticketing platform
</script>

<section class="section lined" id="projects">
  <div class="container">
    <div class="section-head reveal">
      <div class="left">
        <div class="section-num">§ FEATURED · 01 / 01</div>
        <h2 class="h2">A distributed ticketing platform,<br class="hide-sm"/>built end-to-end.</h2>
        <p class="sublead">A personal project that mirrors a real e-commerce/ticketing topology — polyglot services, event-driven by design, with both sync (gRPC) and async (Kafka) communication.</p>
      </div>
      <a class="btn" href="https://github.com/emmilcheung/k8s-multi-language-gRPC-microservice" target="_blank" rel="noopener">
        <svg class="icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .5C5.65.5.5 5.65.5 12c0 5.08 3.29 9.39 7.86 10.91.58.11.79-.25.79-.56 0-.27-.01-1.16-.02-2.1-3.2.7-3.87-1.36-3.87-1.36-.52-1.32-1.27-1.67-1.27-1.67-1.04-.71.08-.7.08-.7 1.15.08 1.76 1.18 1.76 1.18 1.02 1.75 2.68 1.25 3.34.96.1-.74.4-1.25.73-1.54-2.55-.29-5.24-1.27-5.24-5.67 0-1.25.45-2.27 1.18-3.07-.12-.29-.51-1.45.11-3.03 0 0 .96-.31 3.15 1.17a10.95 10.95 0 0 1 5.74 0c2.19-1.48 3.15-1.17 3.15-1.17.62 1.58.23 2.74.11 3.03.73.8 1.18 1.82 1.18 3.07 0 4.41-2.7 5.38-5.26 5.66.41.36.78 1.06.78 2.14 0 1.55-.01 2.8-.01 3.18 0 .31.21.68.8.56C20.21 21.38 23.5 17.07 23.5 12 23.5 5.65 18.35.5 12 .5z"/></svg>
        View source
      </a>
    </div>

    <div class="featured reveal" style="--reveal-delay:80ms">
      <div class="featured-head">
        <div class="title-block">
          <div class="crumb">
            <span>personal</span>
            <span class="sep">/</span>
            <span>k8s-multi-language-gRPC-microservice</span>
            <span class="pill branch">main</span>
          </div>
          <h3>Polyglot Ticketing Platform <span class="accent-link">↗</span></h3>
          <p class="sub">8 independently-deployable services. Saga-based order flow. Federated GraphQL gateway. Sub-second seat reservations through a Redis hot path.</p>
        </div>
        <!-- <div class="actions">
          <a class="btn" href="https://github.com/emmilcheung/k8s-multi-language-gRPC-microservice" target="_blank" rel="noopener">
            <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="6 3 20 12 6 21 6 3"/></svg>
            Demo
          </a>
          <a class="btn primary" href="https://github.com/emmilcheung/k8s-multi-language-gRPC-microservice" target="_blank" rel="noopener">Walkthrough →</a>
        </div> -->
      </div>

      <div class="arch-diagram">
        <div class="layers">

          <div class="arch-row">
            <div class="arch-label">CLIENT</div>
            <div class="nodes">
              <div class="node"><span class="dot" style="background:#7DD3FC"></span>Web<span class="lang">next.js</span></div>
              <div class="node"><span class="dot" style="background:#7DD3FC"></span>Admin<span class="lang">next.js</span></div>
            </div>
          </div>

          <div class="arch-row">
            <div class="arch-label">GATEWAY</div>
            <div class="nodes">
              <div class="node"><span class="dot" style="background:#FB923C"></span>Apollo Router<span class="lang">graphql federation</span></div>
              <div class="node"><span class="dot" style="background:#FB923C"></span>Kong<span class="lang">rest · jwt · csrf</span></div>
            </div>
          </div>

          <div class="arch-row">
            <div class="arch-label">SERVICES</div>
            <div class="nodes">
              <div class="node"><span class="dot" style="background:#4ADE80"></span>events<span class="lang">go</span></div>
              <div class="node"><span class="dot" style="background:#F472B6"></span>orders<span class="lang">java/spring</span></div>
              <div class="node"><span class="dot" style="background:#A78BFA"></span>seats<span class="lang">ts/nestjs</span></div>
              <div class="node"><span class="dot" style="background:#4ADE80"></span>payments<span class="lang">go</span></div>
              <div class="node"><span class="dot" style="background:#F472B6"></span>users<span class="lang">java/spring</span></div>
              <div class="node"><span class="dot" style="background:#A78BFA"></span>notify<span class="lang">ts/nestjs</span></div>
              <div class="node"><span class="dot" style="background:#4ADE80"></span>inventory<span class="lang">go</span></div>
              <div class="node"><span class="dot" style="background:#A78BFA"></span>search<span class="lang">ts/nestjs</span></div>
            </div>
          </div>

          <div class="arch-row bus-row">
            <div class="arch-label">EVENT BUS</div>
            <div class="nodes">
              <div class="node bus-node">Kafka · transactional outbox · saga</div>
              <div class="node bus-node">gRPC contracts (sync)</div>
              <div class="node bus-node">SSE → browser (live seat map)</div>
            </div>
          </div>

          <div class="arch-row">
            <div class="arch-label">DATA</div>
            <div class="nodes">
              <div class="node data-node">PostgreSQL · source of truth</div>
              <div class="node data-node">MongoDB · per-service</div>
              <div class="node data-node">Redis · hot path / holds</div>
            </div>
          </div>

        </div>
      </div>

      <div class="featured-meta">
        <div class="item"><div class="k">Services</div><div class="v">8 polyglot · K8s-deployment</div></div>
        <div class="item"><div class="k">Languages</div><div class="v">Go · Java · TypeScript</div></div>
        <div class="item"><div class="k">Patterns</div><div class="v">Saga · Outbox · CQRS-lite</div></div>
        <div class="item"><div class="k">Status</div><div class="v active">● Active build</div></div>
      </div>
    </div>
  </div>
</section>

<style>
  .hide-sm { display: block; }

  .featured {
    background: linear-gradient(180deg, var(--surface), var(--bg-1));
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 36px;
    position: relative;
    overflow: hidden;
  }
  .featured::before {
    content: ''; position: absolute; top: -1px; left: 36px; right: 36px; height: 1px;
    background: linear-gradient(90deg, transparent, var(--accent), transparent);
    opacity: 0.6;
  }

  .featured-head {
    display: flex; justify-content: space-between; align-items: start; gap: 32px;
    margin-bottom: 32px;
  }

  .crumb {
    display: flex; align-items: center; gap: 10px;
    font-family: 'JetBrains Mono', monospace; font-size: 11px;
    color: var(--text-dim); margin-bottom: 12px;
  }
  .sep { color: var(--text-faint); }
  .branch {
    font-size: 10px; padding: 2px 8px;
    background: var(--surface-2); border-color: var(--border);
    border-radius: 4px;
  }

  .title-block h3 {
    font-size: 36px; line-height: 1.05; letter-spacing: -0.025em;
    font-weight: 700; margin: 0;
    color: var(--text);
  }
  .accent-link { color: var(--accent); }
  .sub { margin-top: 10px; color: var(--text-dim); font-size: 16px; max-width: 620px; }

  .actions { display: flex; gap: 8px; flex-shrink: 0; }

  /* Architecture diagram */
  .arch-diagram {
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 28px;
  }
  .layers { display: grid; grid-template-columns: 1fr; gap: 20px; }
  .arch-row { display: flex; align-items: center; gap: 14px; }
  .arch-label {
    width: 110px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px; color: var(--text-faint);
    letter-spacing: 0.08em; text-transform: uppercase;
    flex-shrink: 0;
  }
  .nodes { display: flex; gap: 8px; flex-wrap: wrap; }
  .node {
    display: flex; align-items: center; gap: 8px;
    padding: 9px 12px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 7px;
    font-size: 12px;
    font-family: 'JetBrains Mono', monospace;
    color: var(--text);
  }
  .dot { width: 6px; height: 6px; border-radius: 50%; flex-shrink: 0; }
  .lang { color: var(--text-faint); font-size: 10px; margin-left: 4px; }

  .bus-row {
    padding: 10px 0;
    border-top: 1px dashed var(--border);
    border-bottom: 1px dashed var(--border);
    margin: 4px 0;
  }
  .bus-node {
    background: rgba(167,139,250,0.06);
    border-color: rgba(167,139,250,0.25);
    color: var(--violet);
  }
  .data-node {
    background: var(--accent-faint);
    border-color: var(--accent-soft);
    color: var(--accent);
    font-weight: 500;
  }

  /* Meta strip */
  .featured-meta {
    display: grid; grid-template-columns: repeat(4, 1fr);
    gap: 24px;
    margin-top: 28px;
    padding-top: 24px;
    border-top: 1px solid var(--border);
  }
  .item .k {
    font-family: 'JetBrains Mono', monospace; font-size: 10px;
    color: var(--text-faint); letter-spacing: 0.08em; text-transform: uppercase;
    margin-bottom: 6px;
  }
  .item .v { font-size: 14px; color: var(--text); }
  .item .v.active { color: var(--accent); }

  @media (max-width: 1024px) {
    .featured-meta { grid-template-columns: repeat(2, 1fr); }
  }

  @media (max-width: 768px) {
    .hide-sm { display: none; }
    .featured { padding: 20px; }
    .featured::before { left: 20px; right: 20px; }
    .featured-head { flex-direction: column; gap: 18px; align-items: flex-start; margin-bottom: 24px; }
    .title-block h3 { font-size: 24px; }
    .sub { font-size: 14px; }
    .actions { width: 100%; }
    .arch-diagram { padding: 16px; }
    .arch-row { flex-direction: column; align-items: flex-start; gap: 10px; }
    .arch-label { width: auto; font-size: 9px; }
    .featured-meta { grid-template-columns: 1fr 1fr; padding-top: 20px; gap: 16px; }
  }

  @media (max-width: 480px) {
    .featured-meta { grid-template-columns: 1fr; }
  }
</style>
