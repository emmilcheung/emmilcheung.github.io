<script lang="ts">
  import { createEventDispatcher, tick } from 'svelte';
  import ChatMessage from './ChatMessage.svelte';
  import type { Message } from './types';

  export let apiUrl: string;
  export let title: string;
  export let placeholder: string;

  const dispatch = createEventDispatcher<{ close: void }>();

  let messages: Message[] = [
    {
      role: 'assistant',
      content: "Hi! I'm here to answer questions about Emmil's professional background. What would you like to know?",
    },
  ];
  let question = '';
  let loading = false;
  let messagesEl: HTMLDivElement;

  async function scrollToBottom() {
    await tick();
    if (messagesEl) messagesEl.scrollTop = messagesEl.scrollHeight;
  }

  async function sendMessage() {
    const q = question.trim();
    if (!q || loading) return;

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
      messages = [
        ...messages,
        { role: 'assistant', content: "Sorry, I couldn't process that right now. Please try again." },
      ];
      await scrollToBottom();
    } finally {
      loading = false;
    }
  }

  /** Reveal the assistant reply word-by-word for a human-like feel */
  async function typeMessage(text: string) {
    const words = text.split(' ');
    // Start with an empty typing bubble
    messages = [...messages, { role: 'assistant', content: '', typing: true }];
    await scrollToBottom();

    let built = '';
    for (const word of words) {
      built += (built ? ' ' : '') + word;
      messages = messages.map((m, i) =>
        i === messages.length - 1 ? { ...m, content: built } : m
      );
      await scrollToBottom();
      // Variable delay: 30-70ms per word — mimics natural typing rhythm
      await new Promise<void>(r => setTimeout(r, 30 + Math.random() * 40));
    }

    // Mark typing complete
    messages = messages.map((m, i) =>
      i === messages.length - 1 ? { ...m, typing: false } : m
    );
  }

  function handleKeydown(e: KeyboardEvent) {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  }
</script>

<!-- Panel shell -->
<div
  class="
    fixed bottom-24 right-6 z-50
    w-[360px] max-w-[calc(100vw-3rem)]
    flex flex-col
    rounded-2xl overflow-hidden shadow-2xl
    bg-white/95 dark:bg-slate-900/95 backdrop-blur-md
    border border-slate-200/60 dark:border-slate-700/60
    animate-chat-slide-up
  "
  style="height: 480px;"
>
  <!-- Header -->
  <div class="flex items-center justify-between px-4 py-3 bg-gradient-to-r from-amber-400 to-orange-500 shrink-0">
    <div class="flex items-center gap-2">
      <div class="w-8 h-8 rounded-full bg-white/20 flex items-center justify-center text-white font-bold text-sm">E</div>
      <div>
        <p class="text-white font-semibold text-sm leading-tight">{title}</p>
        <!-- <p class="text-white/80 text-xs">Powered by Claude AI</p> -->
      </div>
    </div>
    <button
      on:click={() => dispatch('close')}
      class="text-white/80 hover:text-white transition-colors p-1 rounded-lg hover:bg-white/10"
      aria-label="Close chat"
    >
      <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
      </svg>
    </button>
  </div>

  <!-- Messages -->
  <div
    bind:this={messagesEl}
    class="flex-1 overflow-y-auto px-3 py-4 space-y-0 scroll-smooth"
  >
    {#each messages as message (message)}
      <ChatMessage {message} />
    {/each}

    {#if loading && !messages.at(-1)?.typing}
      <!-- Show typing indicator while awaiting first word -->
      <div class="flex justify-start mb-3">
        <div class="w-7 h-7 rounded-full bg-gradient-to-br from-amber-400 to-orange-500 flex items-center justify-center text-white text-xs font-bold mr-2 mt-auto mb-0.5 shrink-0">E</div>
        <div class="px-3.5 py-2.5 bg-white dark:bg-slate-700 rounded-2xl rounded-bl-sm border border-slate-100 dark:border-slate-600 shadow-sm">
          <span class="flex items-center gap-1 px-1 py-0.5">
            <span class="w-2 h-2 rounded-full bg-amber-400 animate-bounce-dot" style="animation-delay: 0ms"></span>
            <span class="w-2 h-2 rounded-full bg-amber-400 animate-bounce-dot" style="animation-delay: 160ms"></span>
            <span class="w-2 h-2 rounded-full bg-amber-400 animate-bounce-dot" style="animation-delay: 320ms"></span>
          </span>
        </div>
      </div>
    {/if}
  </div>

  <!-- Input -->
  <div class="shrink-0 px-3 py-3 border-t border-slate-100 dark:border-slate-700/60 bg-white/50 dark:bg-slate-800/50">
    <div class="flex items-end gap-2">
      <textarea
        bind:value={question}
        on:keydown={handleKeydown}
        {placeholder}
        rows="1"
        disabled={loading}
        class="
          flex-1 resize-none rounded-xl border border-slate-200 dark:border-slate-600
          bg-white dark:bg-slate-700 text-slate-800 dark:text-slate-100
          placeholder-slate-400 dark:placeholder-slate-500
          px-3 py-2 text-sm leading-relaxed
          focus:outline-none focus:ring-2 focus:ring-amber-400/60 focus:border-amber-400
          disabled:opacity-50 transition-all
          max-h-24 overflow-y-auto
        "
        style="field-sizing: content;"
      ></textarea>
      <button
        on:click={sendMessage}
        disabled={loading || !question.trim()}
        class="
          shrink-0 w-9 h-9 rounded-xl
          bg-gradient-to-br from-amber-400 to-orange-500
          text-white flex items-center justify-center
          hover:shadow-md hover:-translate-y-px transition-all
          disabled:opacity-40 disabled:cursor-not-allowed disabled:hover:translate-y-0
        "
        aria-label="Send message"
      >
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 19V5M5 12l7-7 7 7"/>
        </svg>
      </button>
    </div>
    <p class="text-center text-xs text-slate-400 dark:text-slate-500 mt-2">
      Questions about Emmil's background only
    </p>
  </div>
</div>
