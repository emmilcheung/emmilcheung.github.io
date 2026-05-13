<script lang="ts">
  import TypingIndicator from './TypingIndicator.svelte';
  import type { Message } from './types';
  import { marked } from 'marked';
  import DOMPurify from 'dompurify';

  let { message }: { message: Message } = $props();

  const renderedHtml = $derived(
    message.role === 'assistant' && !message.typing && message.content
      ? DOMPurify.sanitize(marked.parse(message.content) as string, {
          ALLOWED_TAGS: ['p', 'strong', 'em', 'ul', 'ol', 'li', 'code', 'br'],
          ALLOWED_ATTR: [],
        })
      : null
  );
</script>

<div class="msg-wrap" class:user={message.role === 'user'} class:bot={message.role === 'assistant'}>
  {#if message.role === 'assistant'}
    <div class="avatar">AI</div>
  {/if}

  <div class="bubble" class:user-bubble={message.role === 'user'} class:bot-bubble={message.role === 'assistant'}>
    {#if message.typing && message.content === ''}
      <TypingIndicator />
    {:else if renderedHtml !== null}
      <div class="msg-md">{@html renderedHtml}</div>
    {:else}
      {message.content}
    {/if}
  </div>

  {#if message.role === 'user'}
    <div class="avatar user-av">U</div>
  {/if}
</div>

<style>
  .msg-wrap {
    display: flex; gap: 12px; margin-bottom: 14px;
    max-width: 92%;
  }
  .msg-wrap.user { align-self: flex-end; margin-left: auto; }
  .msg-wrap.bot { align-self: flex-start; }

  .avatar {
    flex-shrink: 0;
    width: 28px; height: 28px; border-radius: 7px;
    display: grid; place-items: center;
    font-size: 11px; font-weight: 700;
    font-family: 'JetBrains Mono', monospace;
    background: linear-gradient(135deg, var(--accent, #00E5FF), var(--violet, #A78BFA));
    color: var(--on-accent, #02141a);
    align-self: flex-end;
  }
  .user-av {
    background: var(--surface-2, #181C26);
    color: var(--text-dim, #8B93A7);
    border: 1px solid var(--border, #1F2330);
  }

  .bubble {
    padding: 11px 14px;
    border-radius: 10px;
    font-size: 14px; line-height: 1.55;
  }
  .bot-bubble {
    background: var(--surface-2, #181C26);
    border: 1px solid var(--border, #1F2330);
    color: var(--text, #E8EBF2);
  }
  .user-bubble {
    background: var(--accent-faint, rgba(0,229,255,0.08));
    border: 1px solid var(--accent-soft, rgba(0,229,255,0.22));
    color: var(--text, #E8EBF2);
  }

  .msg-md :global(p) { margin: 0 0 0.35em; }
  .msg-md :global(p:last-child) { margin-bottom: 0; }
  .msg-md :global(ul), .msg-md :global(ol) { margin: 0.25em 0 0.35em 1.1em; padding: 0; }
  .msg-md :global(ul) { list-style: disc; }
  .msg-md :global(ol) { list-style: decimal; }
  .msg-md :global(li) { margin: 0.15em 0; }
  .msg-md :global(strong) { font-weight: 600; color: var(--text, #E8EBF2); }
  .msg-md :global(em) { font-style: italic; }
  .msg-md :global(code) {
    font-family: 'JetBrains Mono', ui-monospace, monospace;
    font-size: 0.82em;
    background: var(--accent-faint, rgba(0,229,255,0.08));
    color: var(--accent, #00E5FF);
    padding: 0.1em 0.3em;
    border-radius: 3px;
  }
</style>
