<script lang="ts">
  // RAG pipeline section — static
</script>

<section class="section lined" id="how">
  <div class="container">
    <div class="section-head reveal">
      <div class="left">
        <div class="section-num">§ HOW THIS PAGE WORKS</div>
        <h2 class="h2">The chatbot in the corner<br class="hide-sm"/>is its own portfolio piece.</h2>
        <p class="sublead">RAG over my resume, project notes, and a curated Q&amp;A set. Built on the same patterns I use in production: monorepo + serverless + a thin retrieval layer in front of an LLM.</p>
      </div>
      <a class="btn" href="https://github.com/emmilcheung" target="_blank" rel="noopener">
        <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
        Source on GitHub
      </a>
    </div>

    <div class="rag-stage reveal" style="--reveal-delay:80ms">

      <div class="rag-pipeline">

        <div class="rag-node">
          <div class="num">01 · INPUT</div>
          <div class="label">User question</div>
          <div class="tech">ChatWidget · Svelte</div>
        </div>
        <div class="rag-arrow">→</div>

        <div class="rag-node">
          <div class="num">02 · EMBED</div>
          <div class="label">Vectorize query</div>
          <div class="tech">text-embedding-3</div>
        </div>
        <div class="rag-arrow">→</div>

        <div class="rag-node active">
          <div class="num">03 · RETRIEVE</div>
          <div class="label">Top-k chunks</div>
          <div class="tech">SQLite · cosine · k=5</div>
        </div>
        <div class="rag-arrow">→</div>

        <div class="rag-node">
          <div class="num">04 · COMPOSE</div>
          <div class="label">Prompt + context</div>
          <div class="tech">LangChain · Python</div>
        </div>
        <div class="rag-arrow">→</div>

        <div class="rag-node">
          <div class="num">05 · STREAM</div>
          <div class="label">Tokens → browser</div>
          <div class="tech">SSE · Lambda</div>
        </div>

      </div>

      <div class="rag-flow">
        <span class="c">┌─</span> request flow<br/>
        <span class="c">│</span>   <span class="l">apps/web</span>             → Svelte ChatPanel posts question<br/>
        <span class="c">│</span>   <span class="l">packages/chat-widget</span> → embedded library, framework-agnostic API<br/>
        <span class="c">│</span>   <span class="l">services/rag</span>         → <span class="p">Python Script</span> · embed query · retrieve from resume.db · stream completion<br/>
        <span class="c">│</span>   <span class="l">data/resume.db</span>       → curated chunks from <span class="s">resume_curated.md</span> + <span class="s">resume_qa.md</span><br/>
        <span class="c">└─</span> deployed via SST → CloudFront + Lambda<span class="c">@</span>Edge
      </div>

    </div>
  </div>
</section>

<style>
  .hide-sm { display: block; }

  .rag-stage {
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 36px;
    margin-top: 8px;
  }

  .rag-pipeline {
    display: grid;
    grid-template-columns: 1fr 28px 1fr 28px 1fr 28px 1fr 28px 1fr;
    gap: 0;
    align-items: stretch;
  }

  .rag-node {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px;
    display: flex; flex-direction: column; gap: 8px;
  }
  .rag-node.active {
    background: linear-gradient(180deg, var(--accent-faint), var(--surface));
    border-color: var(--accent-soft);
    box-shadow: 0 0 24px -8px var(--accent-glow);
  }

  .num {
    font-family: 'JetBrains Mono', monospace; font-size: 10px;
    color: var(--accent); letter-spacing: 0.06em;
  }
  .label { font-size: 13px; font-weight: 600; color: var(--text); }
  .tech {
    font-family: 'JetBrains Mono', monospace; font-size: 10px;
    color: var(--text-faint); margin-top: 4px;
  }

  .rag-arrow { display: grid; place-items: center; color: var(--text-faint); font-size: 14px; }

  .rag-flow {
    margin-top: 20px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 18px 22px;
    font-family: 'JetBrains Mono', monospace; font-size: 12px;
    line-height: 1.8;
    color: var(--text-dim);
  }
  .rag-flow .l { color: var(--text); }
  .rag-flow .c { color: var(--accent); }
  .rag-flow .p { color: var(--violet); }
  .rag-flow .s { color: var(--success); }

  @media (max-width: 768px) {
    .hide-sm { display: none; }
    .rag-stage { padding: 22px; }
    .rag-pipeline {
      grid-template-columns: 1fr !important;
      gap: 0;
    }
    .rag-arrow {
      padding: 6px 0;
      transform: rotate(90deg);
      width: 100%;
    }
    .rag-flow {
      font-size: 11px;
      padding: 14px 16px;
      overflow-x: auto;
      white-space: nowrap;
    }
  }
</style>
