<script lang="ts">
  import ChatPanel from './ChatPanel.svelte';
  import type { ChatWidgetProps } from './types';

  export let apiUrl: ChatWidgetProps['apiUrl'];
  export let title: string = 'Ask about Emmil';
  export let placeholder: string = 'Ask about my experience, skills...';

  let open = false;
  let firstOpen = true;

  function toggle() {
    open = !open;
    if (open) firstOpen = false;
  }
</script>

<!-- Floating action button -->
<div class="fixed bottom-6 right-6 z-50 flex flex-col items-end gap-3">
  {#if !open && firstOpen}
    <!-- Nudge bubble: draws attention on first load -->
    <div class="
      bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-200
      text-xs px-3 py-2 rounded-xl rounded-br-sm shadow-lg
      border border-slate-100 dark:border-slate-700
      animate-fade-in max-w-[160px] text-center leading-snug
    ">
      Ask me about Emmil's background!
    </div>
  {/if}

  <button
    on:click={toggle}
    class="
      relative w-14 h-14 rounded-full
      bg-gradient-to-br from-amber-400 to-orange-500
      text-white shadow-lg hover:shadow-xl
      hover:-translate-y-1 active:translate-y-0
      transition-all duration-200
      flex items-center justify-center
    "
    aria-label={open ? 'Close chat' : 'Open chat'}
    aria-expanded={open}
  >
    <!-- Pulse ring (visible when closed) -->
    {#if !open}
      <span class="absolute inset-0 rounded-full bg-amber-400 opacity-30 animate-ping" style="animation-duration: 2.5s;"></span>
    {/if}

    <!-- Icon swap with crossfade feel -->
    <span class="transition-transform duration-200 {open ? 'scale-0 absolute' : 'scale-100'}">
      <!-- Chat bubble icon -->
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
          d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
      </svg>
    </span>
    <span class="transition-transform duration-200 {open ? 'scale-100' : 'scale-0 absolute'}">
      <!-- X icon -->
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12"/>
      </svg>
    </span>
  </button>
</div>

<!-- Chat panel -->
{#if open}
  <ChatPanel
    {apiUrl}
    {title}
    {placeholder}
    on:close={() => (open = false)}
  />
{/if}
