# Emmil Cheung - Portfolio

🔗 **Live Site:** https://emmilcheung.github.io/

Modern, responsive portfolio website built with Svelte, Vite, and Tailwind CSS.

## 🚀 Features

- ⚡ Lightning-fast performance with Svelte
- 🎨 Modern UI with Tailwind CSS
- 📱 Fully responsive design
- 🌙 Dark mode support
- 🚀 Optimized for GitHub Pages
- ♿ Accessible and SEO-friendly

## 🛠️ Tech Stack

- **Framework:** Svelte 4
- **Build Tool:** Vite 6
- **Styling:** Tailwind CSS 3
- **Deployment:** GitHub Pages
- **CI/CD:** GitHub Actions

## 📦 Development

### Prerequisites

- Node.js 18+ or 20 (LTS recommended)
- npm
- nvm (recommended for Node version management)

> **Note:** If using Node 24+, you may encounter compatibility issues with Vite 5. Use Node 20 LTS for best results:
> ```bash
> nvm use 20
> ```

### Install Dependencies

```bash
npm install
```

### Start Development Server

```bash
npm run dev
```

Visit `http://localhost:5173` to view the site.

### Build for Production

```bash
npm run build
```

The built files will be in the `dist` directory.

### Preview Production Build

```bash
npm run preview
```

## 🚀 Deployment

This site automatically deploys to GitHub Pages when you push to the `master` branch.

### Manual Deployment

```bash
npm run deploy
```

## 📝 Content Update

To update resume content, edit the component files in `src/components/`:

- `Hero.svelte` - Header and contact information
- `Experience.svelte` - Work experience
- `Education.svelte` - Educational background
- `Certifications.svelte` - Professional certifications
- `Skills.svelte` - Technical skills

## 📄 License

© 2026 Emmil Cheung. All rights reserved.
