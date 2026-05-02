# Emmil Cheung - Portfolio

🔗 **Live Site:** https://emmilcheung.github.io/

Modern, responsive portfolio website built with Svelte, Vite, Tailwind CSS, and SST.

## 🚀 Features

- ⚡ Lightning-fast performance with Svelte
- 🎨 Modern UI with Tailwind CSS
- 📱 Fully responsive design
- 🌙 Dark mode support
- 🚀 Optimized for GitHub Pages
- ♿ Accessible and SEO-friendly

## 🛠️ Tech Stack

- **Framework:** Svelte 5
- **Build Tool:** Vite 8
- **Styling:** Tailwind CSS 3
- **Deployment:** GitHub Pages
- **Infra:** SST + AWS Lambda for the portfolio chat API
- **CI/CD:** GitHub Actions

## 📦 Development

### Prerequisites

- Node.js 20
- pnpm
- nvm (recommended for Node version management)

> **Note:** Use Node 20 for all local package operations in this repo:
> ```bash
> nvm use 20
> ```

### Install Dependencies

```bash
pnpm install
```

### Start Development Server

```bash
pnpm dev
```

Visit `http://localhost:5173` to view the site.

### Build for Production

```bash
pnpm build
```

The built files will be in the `dist` directory.

### Preview Production Build

```bash
pnpm --filter @emmil/web preview
```

## 🚀 Deployment

This site automatically deploys to GitHub Pages when you push to the `master` branch.

The portfolio chat API is deployed separately via SST.

## 📝 Content Update

To update website content, edit the component files in `apps/web/src/components/`:

- `Hero.svelte` - Header and contact information
- `Experience.svelte` - Work experience
- `Education.svelte` - Educational background
- `Certifications.svelte` - Professional certifications
- `Skills.svelte` - Technical skills

To rebuild the RAG database used by the chat assistant, see `services/rag/README.md`.

## 📄 License

© 2026 Emmil Cheung. All rights reserved.
