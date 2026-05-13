<span class="typing-dots" aria-label="Assistant is typing">
  <span style="animation-delay: 0ms"></span>
  <span style="animation-delay: 150ms"></span>
  <span style="animation-delay: 300ms"></span>
</span>

<style>
  .typing-dots {
    display: inline-flex; align-items: center; gap: 4px;
    padding: 4px 0;
  }
  .typing-dots span {
    width: 6px; height: 6px; border-radius: 50%;
    background: var(--text-dim, #8B93A7);
    animation: bounce 1.2s infinite;
  }
  @keyframes bounce {
    0%, 80%, 100% { transform: translateY(0); opacity: 0.4; }
    40% { transform: translateY(-4px); opacity: 1; }
  }
</style>
