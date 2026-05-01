<script lang="ts">
  import TypingIndicator from './TypingIndicator.svelte';
  import type { Message } from './types';
  import { marked } from 'marked';
  import DOMPurify from 'dompurify';

  export let message: Message;

  // Only parse markdown once typing is complete to avoid flickering on partial syntax.
  // User messages are always rendered as plain text.
  $: renderedHtml =
    message.role === 'assistant' && !message.typing && message.content
      ? DOMPurify.sanitize(marked.parse(message.content) as string, {
          ALLOWED_TAGS: ['p', 'strong', 'em', 'ul', 'ol', 'li', 'code', 'br'],
          ALLOWED_ATTR: [],
        })
      : null;
</script>

<div class="flex {message.role === 'user' ? 'justify-end' : 'justify-start'} mb-3">
  {#if message.role === 'assistant'}
    <!-- Avatar -->
    <div class="w-7 h-7 rounded-full bg-gradient-to-br from-amber-400 to-orange-500 flex items-center justify-center text-white text-xs font-bold mr-2 mt-auto mb-0.5 shrink-0">
      E
    </div>
  {/if}

  <div
    class="
      max-w-[78%] px-3.5 py-2.5 rounded-2xl text-sm leading-relaxed shadow-sm
      {message.role === 'user'
        ? 'bg-gradient-to-br from-amber-400 to-orange-500 text-white rounded-br-sm'
        : 'bg-white dark:bg-slate-700 text-slate-700 dark:text-slate-200 rounded-bl-sm border border-slate-100 dark:border-slate-600'}
    "
  >
    {#if message.typing && message.content === ''}
      <TypingIndicator />
    {:else if renderedHtml !== null}
      <div class="msg-md">{@html renderedHtml}</div>
    {:else}
      {message.content}
    {/if}
  </div>
</div>

<style>
  /* Styles for markdown content injected via {@html}. Must use :global()
     because Svelte's scoped hash does not apply to dynamically injected HTML. */
  .msg-md :global(p) {
    margin: 0 0 0.35em;
  }
  .msg-md :global(p:last-child) {
    margin-bottom: 0;
  }
  .msg-md :global(ul),
  .msg-md :global(ol) {
    margin: 0.25em 0 0.35em 1.1em;
    padding: 0;
  }
  .msg-md :global(ul) {
    list-style: disc;
  }
  .msg-md :global(ol) {
    list-style: decimal;
  }
  .msg-md :global(li) {
    margin: 0.15em 0;
  }
  .msg-md :global(strong) {
    font-weight: 600;
  }
  .msg-md :global(em) {
    font-style: italic;
  }
  .msg-md :global(code) {
    font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
    font-size: 0.82em;
    background: rgba(0, 0, 0, 0.07);
    padding: 0.1em 0.3em;
    border-radius: 3px;
  }
</style>
