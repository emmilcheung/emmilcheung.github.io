<script lang="ts">
  import { tick } from 'svelte';
  import ChatMessage from './ChatMessage.svelte';
  import type { Message } from './types';

  let {
    apiUrl,
    title,
    placeholder,
    onclose,
  }: { apiUrl: string; title: string; placeholder: string; onclose: () => void } = $props();

  const suggested = [
    "Walk me through the ticketing platform",
    "What's his AWS Lambda experience?",
    "How does this chatbot work?",
  ];

  let showSuggested = $state(true);

  let messages = $state<Message[]>([
    {
      role: 'assistant',
      content: "Hi — I've read Emmil's full resume, project notes, and code samples. Ask me about his experience, architecture decisions, or how this chatbot itself works.",
    },
  ]);
  let question = $state('');
  let loading = $state(false);
  let messagesEl = $state<HTMLDivElement | undefined>(undefined);

  async function scrollToBottom() {
    await tick();
    if (messagesEl) (messagesEl as HTMLDivElement).scrollTop = (messagesEl as HTMLDivElement).scrollHeight;
  }

  async function sendMessage() {
    const q = question.trim();
    if (!q || loading) return;
    showSuggested = false;
    messages = [...messages, { role: 'user', content: q }];
    question = '';
    loading = true;
    await scrollToBottom();
    try {
      const res = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: q }),
      });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json() as { answer: string };
      await typeMessage(data.answer);
    } catch {
      messages = [...messages, { role: 'assistant', content: "Sorry, I couldn't process that right now. Please try again." }];
      await scrollToBottom();
    } finally {
      loading = false;
    }
  }

  async function typeMessage(text: string) {
    const words = text.split(' ');
    messages = [...messages, { role: 'assistant', content: '', typing: true }];
    await scrollToBottom();
    let built = '';
    for (const word of words) {
      built += (built ? ' ' : '') + word;
      messages = messages.map((m, i) => i === messages.length - 1 ? { ...m, content: built } : m);
      await scrollToBottom();
      await new Promise<void>(r => setTimeout(r, 30 + Math.random() * 40));
    }
    messages = messages.map((m, i) => i === messages.length - 1 ? { ...m, typing: false } : m);
  }

  function handleKeydown(e: KeyboardEvent) {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  }

  function fillSuggestion(chip: string) {
    question = chip;
    sendMessage();
  }
</script>

<div class="chat-card">
  <!-- Header -->
  <div class="head">
    <div class="head-title">
      <span class="badge">RAG</span>
      <span>{title}</span>
    </div>
    <div class="head-meta">
      <span style="color: var(--success, #4ADE80);">●</span> DeepSeek V4 Pro
      <button class="close-btn" onclick={onclose} aria-label="Close chat">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4">
          <path d="M18 6 6 18M6 6l12 12"/>
        </svg>
      </button>
    </div>
  </div>

  <!-- Messages -->
  <div class="body" bind:this={messagesEl}>
    {#each messages as message (message)}
      <ChatMessage {message} />
    {/each}

    {#if loading && !messages.at(-1)?.typing}
      <div class="msg bot">
        <div class="who">AI</div>
        <div class="bubble">
          <span class="typing">
            <span></span><span></span><span></span>
          </span>
        </div>
      </div>
    {/if}
  </div>

  <!-- Suggested chips — hidden after first send -->
  {#if showSuggested}
    <div class="suggested">
      {#each suggested as chip}
        <button class="chip" onclick={() => fillSuggestion(chip)}>{chip}</button>
      {/each}
    </div>
  {/if}

  <!-- Input -->
  <div class="input-row">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--text-faint, #535B70)" stroke-width="2">
      <circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>
    </svg>
    <input
      bind:value={question}
      onkeydown={handleKeydown}
      placeholder={placeholder}
      disabled={loading}
    />
    <button class="send-btn" onclick={sendMessage} disabled={loading || !question.trim()} aria-label="Send">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
        <path d="m5 12 7-7 7 7"/><path d="M12 5v14"/>
      </svg>
    </button>
  </div>

  <!-- Footer bar -->
  <div class="footer-bar">
    <span>retrieval: cosine · top_k=5 · resume.db</span>
    <div class="footer-right">
      <span>↑↓ history</span>
      <span>⏎ send</span>
    </div>
  </div>
</div>

<style>
  .chat-card {
    width: 400px;
    max-width: calc(100vw - 32px);
    background: linear-gradient(180deg, var(--surface, #12151C), var(--bg-1, #0D0F14));
    border: 1px solid var(--border, #1F2330);
    border-radius: 14px;
    overflow: hidden;
    box-shadow:
      0 30px 80px -30px var(--accent-glow, rgba(0,229,255,0.18)),
      0 0 0 1px var(--tint-on-surface, rgba(255,255,255,0.012)) inset;
    position: relative;
    font-family: 'Inter', system-ui, sans-serif;
    -webkit-font-smoothing: antialiased;
  }
  .chat-card::before {
    content: ''; position: absolute; inset: 0;
    border-radius: 14px; padding: 1px;
    background: linear-gradient(180deg, var(--accent-soft, rgba(0,229,255,0.22)), transparent 30%);
    -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
    -webkit-mask-composite: xor;
            mask-composite: exclude;
    pointer-events: none;
  }

  /* Head */
  .head {
    display: flex; align-items: center; justify-content: space-between;
    padding: 14px 16px;
    border-bottom: 1px solid var(--border-soft, #161A23);
    background: var(--tint-on-surface, rgba(255,255,255,0.012));
  }
  .head-title {
    display: flex; align-items: center; gap: 10px;
    font-size: 13px; font-weight: 600; color: var(--text, #E8EBF2);
  }
  .badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px; letter-spacing: 0.08em;
    color: var(--accent, #00E5FF);
    background: var(--accent-faint, rgba(0,229,255,0.08));
    padding: 3px 7px; border-radius: 4px;
    border: 1px solid var(--accent-soft, rgba(0,229,255,0.22));
  }
  .head-meta {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px; color: var(--text-faint, #535B70);
    display: flex; align-items: center; gap: 8px;
  }
  .close-btn {
    background: none; border: none; cursor: pointer;
    color: var(--text-faint, #535B70); padding: 4px;
    display: grid; place-items: center;
    border-radius: 4px; transition: color 160ms;
  }
  .close-btn:hover { color: var(--text, #E8EBF2); }

  /* Messages */
  .body {
    padding: 22px 20px 18px;
    display: flex; flex-direction: column; gap: 16px;
    max-height: 340px; overflow-y: auto;
    min-height: 200px;
  }
  .body::-webkit-scrollbar { width: 6px; }
  .body::-webkit-scrollbar-thumb { background: var(--border, #1F2330); border-radius: 3px; }

  .msg { display: flex; gap: 12px; max-width: 92%; }
  .msg.bot { align-self: flex-start; }
  .who {
    flex-shrink: 0;
    width: 28px; height: 28px; border-radius: 7px;
    display: grid; place-items: center;
    font-size: 11px; font-weight: 700;
    font-family: 'JetBrains Mono', monospace;
  }
  .msg.bot .who {
    background: linear-gradient(135deg, var(--accent, #00E5FF), var(--violet, #A78BFA));
    color: var(--on-accent, #02141a);
  }
  .bubble {
    background: var(--surface-2, #181C26);
    border: 1px solid var(--border, #1F2330);
    padding: 11px 14px;
    border-radius: 10px;
    font-size: 14px; line-height: 1.55;
    color: var(--text, #E8EBF2);
  }

  .typing { display: inline-flex; gap: 4px; padding: 4px 0; }
  .typing span {
    width: 6px; height: 6px; border-radius: 50%;
    background: var(--text-dim, #8B93A7);
    animation: bounce 1.2s infinite;
  }
  .typing span:nth-child(2) { animation-delay: 0.15s; }
  .typing span:nth-child(3) { animation-delay: 0.3s; }
  @keyframes bounce {
    0%, 80%, 100% { transform: translateY(0); opacity: 0.4; }
    40% { transform: translateY(-4px); opacity: 1; }
  }

  /* Suggested chips */
  .suggested {
    padding: 0 20px 12px;
    display: flex; flex-wrap: wrap; gap: 6px;
  }
  .chip {
    font-size: 12px; padding: 6px 10px;
    border: 1px solid var(--border, #1F2330);
    background: var(--tint-on-surface, rgba(255,255,255,0.012));
    border-radius: 999px;
    color: var(--text-dim, #8B93A7);
    cursor: pointer; transition: all 160ms;
    font-family: inherit;
  }
  .chip:hover {
    border-color: var(--accent-soft, rgba(0,229,255,0.22));
    color: var(--text, #E8EBF2);
    background: var(--accent-faint, rgba(0,229,255,0.08));
  }

  /* Input */
  .input-row {
    display: flex; align-items: center; gap: 10px;
    margin: 0 16px 16px;
    padding: 10px 12px 10px 14px;
    background: var(--bg-1, #0D0F14);
    border: 1px solid var(--border, #1F2330);
    border-radius: 10px;
  }
  .input-row input {
    flex: 1;
    background: transparent; border: 0; outline: 0;
    color: var(--text, #E8EBF2); font-size: 14px;
    font-family: inherit;
  }
  .input-row input::placeholder { color: var(--text-faint, #535B70); }
  .input-row input:disabled { opacity: 0.5; }
  .send-btn {
    width: 28px; height: 28px; border-radius: 6px;
    background: var(--accent, #00E5FF);
    color: var(--on-accent, #02141a);
    display: grid; place-items: center;
    border: 0; cursor: pointer; flex-shrink: 0;
    transition: background 160ms;
  }
  .send-btn:hover { background: var(--accent-2, #7DF9FF); }
  .send-btn:disabled { opacity: 0.4; cursor: not-allowed; }

  /* Footer bar */
  .footer-bar {
    display: flex; align-items: center; justify-content: space-between;
    padding: 10px 16px;
    border-top: 1px solid var(--border-soft, #161A23);
    background: var(--tint-on-surface, rgba(255,255,255,0.012));
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px; color: var(--text-faint, #535B70);
  }
  .footer-right { display: flex; gap: 12px; }

  @media (max-width: 768px) {
    .chat-card { width: 100%; max-width: none; }
  }
</style>
