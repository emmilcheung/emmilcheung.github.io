<script lang="ts">
  const year = new Date().getFullYear();
</script>

<footer id="contact">
  <div class="container">
    <div class="footer-grid">

      <div class="cta-block">
        <div class="section-num" style="margin-bottom:12px;">§ CONTACT</div>
        <p class="quote">
          Hiring? Building something with serverless, events, or LLMs?
          <span style="color:var(--accent);">Let's talk.</span>
        </p>
        <!-- <div class="cta-actions">
          <a class="btn primary" href="mailto:">
              @gmail.com
            <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m7 7 10 10"/><path d="M17 7v10H7"/></svg>
          </a>
        </div> -->
        <div class="status-pills">
          <span class="pill live">Open to roles</span>
          <span class="pill">Remote OK · HK</span>
          <span class="pill">Backend / Cloud / Platform</span>
        </div>
      </div>

      <div class="footer-col">
        <h4>Find me</h4>
        <ul>
          <li><a href="https://github.com/emmilcheung" target="_blank" rel="noopener">GitHub ↗</a></li>
          <li><a href="https://www.linkedin.com/in/emmil-cheung/" target="_blank" rel="noopener">LinkedIn ↗</a></li>
          <!-- <li><a href="mailto:@gmail.com">Email ↗</a></li> -->
        </ul>
      </div>

      <div class="footer-col">
        <h4>Page</h4>
        <ul>
          <li><a href="#work">Work</a></li>
          <li><a href="#projects">Projects</a></li>
          <li><a href="#education">Education</a></li>
          <li><a href="#certifications">Certs</a></li>
          <li><a href="#stack">Stack</a></li>
          <li><a href="#how">How it works</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4>Meta</h4>
        <ul>
          <!-- <li><a href="mailto:emmilcheung2005@gmail.com">Contact me</a></li> -->
          <li><a href="https://www.credly.com/badges/5c8c259d-c1d2-49e7-99cf-756c7336c9e0/public_url" target="_blank" rel="noopener">AWS DVA · 2025</a></li>
          <li><a href="https://www.cse.cuhk.edu.hk/" target="_blank" rel="noopener">BSc CS · CUHK</a></li>
          <li><a href="https://github.com/emmilcheung/emmilcheung.github.io" target="_blank" rel="noopener">Source of this site</a></li>
        </ul>
      </div>

    </div>

    <div class="footer-bottom">
      <div>© {year} · Emmil Cheung · Built with Svelte + SST + a little RAG</div>
      <div>v2.0 · last deploy 2026-05-14</div>
    </div>
  </div>
</footer>

<style>
  footer {
    border-top: 1px solid var(--border-soft);
    padding: 60px 0 40px;
  }

  .footer-grid {
    display: grid; grid-template-columns: 2fr 1fr 1fr 1fr;
    gap: 60px;
  }

  h4 {
    font-family: 'JetBrains Mono', monospace; font-size: 11px;
    color: var(--text-faint);
    letter-spacing: 0.1em; text-transform: uppercase;
    margin: 0 0 14px;
    font-weight: 500;
  }

  ul { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 8px; }
  ul a { color: var(--text-dim); font-size: 14px; transition: color 160ms; }
  ul a:hover { color: var(--text); }

  .quote {
    font-size: 28px; line-height: 1.2; letter-spacing: -0.018em;
    font-weight: 600; margin: 0 0 20px;
    color: var(--text);
  }

  .cta-actions { display: flex; gap: 10px; flex-wrap: wrap; }

  .status-pills { margin-top: 24px; display: flex; gap: 10px; flex-wrap: wrap; }

  .footer-bottom {
    margin-top: 56px;
    padding-top: 20px;
    border-top: 1px solid var(--border-soft);
    display: flex; justify-content: space-between;
    font-family: 'JetBrains Mono', monospace; font-size: 11px;
    color: var(--text-faint);
  }

  @media (max-width: 1024px) {
    .footer-grid { grid-template-columns: 1fr 1fr; gap: 40px; }
    .cta-block { grid-column: 1 / -1; }
  }

  @media (max-width: 768px) {
    footer { padding: 48px 0 28px; }
    .footer-grid { grid-template-columns: 1fr; gap: 36px; }
    .quote { font-size: 22px; }
    .footer-bottom { flex-direction: column; gap: 8px; align-items: flex-start; }
  }
</style>
