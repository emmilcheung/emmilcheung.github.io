/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{svelte,js,ts}",
    "../../packages/chat-widget/src/**/*.{svelte,js,ts}",
  ],
  theme: {
    extend: {
      colors: {
        bg:           'var(--bg)',
        'bg-1':       'var(--bg-1)',
        surface:      'var(--surface)',
        'surface-2':  'var(--surface-2)',
        border:       'var(--border)',
        'border-soft':'var(--border-soft)',
        text:         'var(--text)',
        'text-dim':   'var(--text-dim)',
        'text-faint': 'var(--text-faint)',
        accent:       'var(--accent)',
        'accent-2':   'var(--accent-2)',
        success:      'var(--success)',
        warn:         'var(--warn)',
        pink:         'var(--pink)',
        violet:       'var(--violet)',
        orange:       'var(--orange)',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'ui-monospace', 'monospace'],
      },
      animation: {
        'fade-in': 'fadeIn 0.6s ease-in',
        'chat-slide-up': 'chatSlideUp 0.3s cubic-bezier(0.34, 1.56, 0.64, 1)',
        'bounce-dot': 'bounceDot 1.2s infinite',
        'fab-pulse': 'fabPulse 2.4s infinite',
        'pulse-dot': 'pulseDot 2s infinite',
      },
      keyframes: {
        fadeIn: { '0%': { opacity: '0' }, '100%': { opacity: '1' } },
        chatSlideUp: {
          '0%': { transform: 'translateY(8px) scale(0.98)', opacity: '0' },
          '100%': { transform: 'none', opacity: '1' },
        },
        bounceDot: {
          '0%, 80%, 100%': { transform: 'translateY(0)', opacity: '0.4' },
          '40%': { transform: 'translateY(-4px)', opacity: '1' },
        },
        fabPulse: {
          '0%': { transform: 'scale(1)', opacity: '0.5' },
          '100%': { transform: 'scale(1.4)', opacity: '0' },
        },
        pulseDot: {
          '0%, 100%': { opacity: '1' },
          '50%': { opacity: '0.4' },
        },
      },
    },
  },
  plugins: [],
}
