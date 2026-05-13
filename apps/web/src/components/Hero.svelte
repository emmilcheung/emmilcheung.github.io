<script lang="ts">
  // No runtime state needed
</script>

<section class="hero">
  <div class="container">
    <div class="hero-stack reveal">

      <div class="name-row">
        <div class="avatar">EC
          <span class="online-dot"></span>
        </div>
        <div>
          <div class="eyebrow"><span class="dot"></span>Hong Kong · GMT+8 · Open to work</div>
          <div class="mono handle">emmil.cheung</div>
        </div>
      </div>

      <h1 class="hero-headline">
        Backend &amp; cloud engineer<br class="hide-mobile"/>
        who ships production <span class="accent">systems.</span>
      </h1>

      <p class="hero-lead">
        <span class="dim">4 years building</span> event-driven serverless backends,
        multi-tenant SaaS, and LLM products
        <span class="dim">— from architecture to deploy.</span>
      </p>

      <div class="ctas">
        <a class="btn primary" href="#chatbot-widget">
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
          Ask my AI about me
          <span class="arrow">→</span>
        </a>
        <a class="btn" href="#work">See work</a>
        <a class="btn" href="https://github.com/emmilcheung" target="_blank" rel="noopener">
          <svg class="icon" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .5C5.65.5.5 5.65.5 12c0 5.08 3.29 9.39 7.86 10.91.58.11.79-.25.79-.56 0-.27-.01-1.16-.02-2.1-3.2.7-3.87-1.36-3.87-1.36-.52-1.32-1.27-1.67-1.27-1.67-1.04-.71.08-.7.08-.7 1.15.08 1.76 1.18 1.76 1.18 1.02 1.75 2.68 1.25 3.34.96.1-.74.4-1.25.73-1.54-2.55-.29-5.24-1.27-5.24-5.67 0-1.25.45-2.27 1.18-3.07-.12-.29-.51-1.45.11-3.03 0 0 .96-.31 3.15 1.17a10.95 10.95 0 0 1 5.74 0c2.19-1.48 3.15-1.17 3.15-1.17.62 1.58.23 2.74.11 3.03.73.8 1.18 1.82 1.18 3.07 0 4.41-2.7 5.38-5.26 5.66.41.36.78 1.06.78 2.14 0 1.55-.01 2.8-.01 3.18 0 .31.21.68.8.56C20.21 21.38 23.5 17.07 23.5 12 23.5 5.65 18.35.5 12 .5z"/></svg>
          GitHub
        </a>
      </div>

      <div class="hero-stats">
        <div class="stat">
          <div class="v">4<span class="accent">+</span></div>
          <div class="k">Years shipping</div>
        </div>
        <!-- <div class="stat">
          <div class="v">5K<span class="accent">+</span></div>
          <div class="k">Daily users served</div>
        </div> -->
        <div class="stat">
          <div class="v">CUHK</div>
          <div class="k">B.Sc in Computer Science</div>
        </div>
        <div class="stat">
          <div class="v">AWS</div>
          <div class="k">DVA Certified · '25</div>
        </div>
      </div>

    </div>
  </div>
</section>

<style>
  .hero { padding: 80px 0 100px; }

  .hero-stack { max-width: 900px; display: flex; flex-direction: column; }

  .name-row { display: flex; align-items: center; gap: 16px; margin-bottom: 28px; }

  .avatar {
    width: 56px; height: 56px; border-radius: 50%;
    background: linear-gradient(135deg, var(--surface-2), var(--surface));
    border: 1px solid var(--border);
    display: grid; place-items: center;
    font-weight: 700; font-size: 22px;
    color: var(--text);
    position: relative;
    flex-shrink: 0;
  }
  .online-dot {
    position: absolute; right: -2px; bottom: -2px;
    width: 14px; height: 14px; border-radius: 50%;
    background: var(--success);
    border: 3px solid var(--bg);
  }

  .handle {
    font-size: 12px; color: var(--text-faint); margin-top: 6px;
    font-family: 'JetBrains Mono', monospace;
  }

  .hero-headline {
    font-size: clamp(38px, 7.4vw, 88px);
    line-height: 1.0;
    letter-spacing: -0.038em;
    font-weight: 700;
    margin: 8px 0 0;
    color: var(--text);
  }
  .hero-headline .accent { color: var(--accent); }

  .hero-lead {
    margin-top: 24px;
    font-size: clamp(16px, 1.6vw, 20px);
    line-height: 1.5;
    color: var(--text);
    font-weight: 500;
    letter-spacing: -0.01em;
    max-width: 700px;
  }
  .hero-lead .dim { color: var(--text-dim); font-weight: 400; }

  .ctas { display: flex; gap: 10px; margin-top: 32px; flex-wrap: wrap; }

  .hero-stats {
    display: grid; grid-template-columns: repeat(4, 1fr);
    margin-top: 48px;
    border-top: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
  }
  .stat {
    padding: 18px 16px 18px 0;
    border-right: 1px solid var(--border);
  }
  .stat:last-child { border-right: 0; padding-right: 0; }
  .stat:not(:first-child) { padding-left: 18px; }
  .v {
    font-size: 28px; font-weight: 700; letter-spacing: -0.02em;
    color: var(--text);
    font-feature-settings: 'tnum';
  }
  .v .accent { color: var(--accent); }
  .k {
    font-size: 11px; color: var(--text-faint);
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 0.06em; text-transform: uppercase;
    margin-top: 4px;
  }

  .hide-mobile { display: block; }

  @media (max-width: 768px) {
    .hero { padding: 40px 0 56px; }
    .hide-mobile { display: none; }
    .hero-headline { font-size: 38px; letter-spacing: -0.03em; }
    .hero-lead { font-size: 16px; }
    .name-row { gap: 12px; margin-bottom: 22px; }
    .avatar { width: 48px; height: 48px; font-size: 18px; }
    .ctas { gap: 8px; margin-top: 24px; }
    .hero-stats { grid-template-columns: 1fr 1fr; margin-top: 32px; }
    .stat { padding: 14px 12px; border-right: 0; }
    .stat:nth-child(odd) { padding-left: 0; border-right: 1px solid var(--border); }
    .stat:nth-child(even) { padding-left: 16px; }
    .stat:nth-child(3), .stat:nth-child(4) { border-top: 1px solid var(--border); }
    .v { font-size: 22px; }
  }

  @media (max-width: 480px) {
    .hero-headline { font-size: 32px; }
  }
</style>
