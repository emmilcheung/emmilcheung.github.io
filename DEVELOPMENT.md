# Development Guide

## Prerequisites

- Node.js 20 and pnpm
- Modern web browser

## Installation

```bash
pnpm install
```

## Development

Start the development server with hot reload:

```bash
pnpm dev
```

The site will be available at `http://localhost:5173`

## Type Checking

Run TypeScript type checking:

```bash
pnpm check
```

## Building

Build for production:

```bash
pnpm build
```

The output will be in the `dist` directory.

## Preview Production Build

Preview the production build locally:

```bash
pnpm --filter @emmil/web preview
```

## Deployment

### Automatic Deployment (Recommended)

Push to the `master` branch and GitHub Actions will automatically build and deploy to GitHub Pages.

### API Deployment

```bash
pnpm infra:deploy
```

## Project Structure

```
.
├── apps/
│   └── web/                # Svelte frontend app
├── packages/
│   ├── chat-widget/        # Shared chat widget package
│   └── functions/          # Lambda handler source
├── services/
│   └── rag/                # Resume chunking + embedding build step
├── data/                   # Generated resume.db artifact
└── sst.config.ts           # SST infrastructure definition
```

## Customization

### Updating Content

Edit the component files in `apps/web/src/components/` to update your resume content:

- **Hero.svelte** - Name, contact info, and hero section
- **Experience.svelte** - Work experience with achievements
- **Education.svelte** - Educational background
- **Certifications.svelte** - Professional certifications
- **Skills.svelte** - Technical skills organized by category

### Styling

The project uses Tailwind CSS for styling. You can:

- Modify `tailwind.config.js` to customize the design system
- Edit `src/app.css` for global styles
- Add component-specific styles in the `<style>` sections

### Colors

Default color scheme uses blue and purple gradients. To change:

Edit `tailwind.config.js`:
```js
colors: {
  primary: '#3b82f6',    // Your primary color
  secondary: '#8b5cf6',  // Your secondary color
}
```

## Troubleshooting

### Port Already in Use

If port 5173 is already in use:
```bash
pnpm --filter @emmil/web dev -- --port 3000
```

### Build Errors

Clear cache and reinstall:
```bash
rm -rf node_modules pnpm-lock.yaml
pnpm install
```

### Type Errors

Run type check to see all errors:
```bash
pnpm check
```
