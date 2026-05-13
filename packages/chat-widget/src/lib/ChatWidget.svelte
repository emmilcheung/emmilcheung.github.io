<script lang="ts">
  import { onMount } from 'svelte';
  import ChatPanel from './ChatPanel.svelte';

  let {
    apiUrl,
    title = 'Ask about Emmil',
    placeholder = 'Ask about my experience, skills...',
  }: { apiUrl: string; title?: string; placeholder?: string } = $props();

  let open = $state(false);
  let showNudge = $state(false);

  function toggle() {
    open = !open;
    if (open) showNudge = false;
  }

  onMount(() => {
    const nudgeTimer = setTimeout(() => {
      if (!open) showNudge = true;
    }, 1800);
    const hideTimer = setTimeout(() => { showNudge = false; }, 6300);
    document.addEventListener('keydown', onKey);
    return () => {
      clearTimeout(nudgeTimer);
      clearTimeout(hideTimer);
      document.removeEventListener('keydown', onKey);
    };
  });

  function onKey(e: KeyboardEvent) {
    if (e.key === 'Escape' && open) open = false;
  }
</script>

<div id="chatbot-widget" class="floating-chat" class:open>

  {#if open}
    <div class="panel">
      <ChatPanel {apiUrl} {title} {placeholder} onclose={() => (open = false)} />
    </div>
  {/if}

  <button class="fab" onclick={toggle} aria-label={open ? 'Close chat' : 'Open chat'} aria-expanded={open}>
    {#if !open}<span class="pulse-ring"></span>{/if}

    {#if showNudge && !open}
      <span class="nudge">
        <span class="nudge-badge">RAG</span>
        Ask my AI about me
      </span>
    {/if}

    <svg class="fab-icon" class:gone={open} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
      <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
    </svg>
    <svg class="fab-icon" class:gone={!open} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4">
      <path d="M18 6 6 18M6 6l12 12"/>
    </svg>
  </button>

</div>

<style>
  .floating-chat {
    position: fixed;
    bottom: 24px;
    right: 24px;
    z-index: 100;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 12px;
    font-family: 'Inter', system-ui, sans-serif;
  }

  .panel {
    animation: slideUp 220ms cubic-bezier(0.2, 0.7, 0.2, 1);
  }
  @keyframes slideUp {
    from { opacity: 0; transform: translateY(8px) scale(0.98); }
    to   { opacity: 1; transform: none; }
  }

  .fab {
    position: relative;
    width: 60px; height: 60px;
    border-radius: 50%;
    background: var(--accent, #00E5FF);
    color: var(--on-accent, #02141a);
    border: 0;
    cursor: pointer;
    display: grid; place-items: center;
    box-shadow: 0 10px 28px var(--accent-glow, rgba(0,229,255,0.18)), 0 4px 12px rgba(0,0,0,0.25);
    transition: transform 200ms cubic-bezier(0.2,0.7,0.2,1);
    flex-shrink: 0;
  }
  .fab:hover { transform: translateY(-2px); }

  .pulse-ring {
    position: absolute; inset: -2px;
    border-radius: 50%;
    border: 2px solid var(--accent, #00E5FF);
    opacity: 0.4;
    animation: fabPulse 2.4s infinite;
    pointer-events: none;
  }
  @keyframes fabPulse {
    0% { transform: scale(1); opacity: 0.5; }
    100% { transform: scale(1.4); opacity: 0; }
  }

  .fab-icon { width: 24px; height: 24px; position: absolute; }
  .fab-icon.gone { opacity: 0; pointer-events: none; }

  .nudge {
    position: absolute;
    right: 70px; top: 50%;
    transform: translateY(-50%);
    background: var(--surface, #12151C);
    border: 1px solid var(--border, #1F2330);
    border-radius: 8px;
    padding: 9px 12px 9px 14px;
    color: var(--text, #E8EBF2);
    font-size: 13px;
    white-space: nowrap;
    box-shadow: 0 4px 14px rgba(0,0,0,0.18);
    display: flex; align-items: center; gap: 8px;
    pointer-events: none;
    animation: nudgeFade 300ms ease;
  }
  .nudge::after {
    content: '';
    position: absolute;
    right: -5px; top: 50%; transform: translateY(-50%) rotate(45deg);
    width: 8px; height: 8px;
    background: var(--surface, #12151C);
    border-right: 1px solid var(--border, #1F2330);
    border-top: 1px solid var(--border, #1F2330);
  }
  @keyframes nudgeFade {
    from { opacity: 0; transform: translateY(-50%) translateX(4px); }
    to   { opacity: 1; transform: translateY(-50%); }
  }

  .nudge-badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 9px;
    color: var(--accent, #00E5FF);
    background: var(--accent-faint, rgba(0,229,255,0.08));
    padding: 2px 6px; border-radius: 3px;
    border: 1px solid var(--accent-soft, rgba(0,229,255,0.22));
    letter-spacing: 0.06em;
  }

  @media (max-width: 768px) {
    .floating-chat { bottom: 16px; right: 16px; }
    .fab { width: 54px; height: 54px; }
    .nudge { display: none; }
    .panel {
      position: fixed;
      bottom: 84px;
      right: 12px; left: 12px;
    }
  }
</style>
