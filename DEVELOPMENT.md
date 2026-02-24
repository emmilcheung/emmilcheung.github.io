# Development Guide

## Prerequisites

- Node.js 20 and npm
- Modern web browser

## Installation

```bash
npm install
```

## Development

Start the development server with hot reload:

```bash
npm run dev
```

The site will be available at `http://localhost:5173`

## Type Checking

Run TypeScript type checking:

```bash
npm run check
```

## Building

Build for production:

```bash
npm run build
```

The output will be in the `dist` directory.

## Preview Production Build

Preview the production build locally:

```bash
npm run preview
```

## Deployment

### Automatic Deployment (Recommended)

Push to the `master` branch and GitHub Actions will automatically build and deploy to GitHub Pages.

### Manual Deployment

```bash
npm run deploy
```

## Project Structure

```
.
├── src/
│   ├── components/          # Svelte components
│   │   ├── Hero.svelte
│   │   ├── Experience.svelte
│   │   ├── Education.svelte
│   │   ├── Certifications.svelte
│   │   ├── Skills.svelte
│   │   └── Footer.svelte
│   ├── App.svelte          # Main app component
│   ├── main.ts             # Entry point
│   ├── app.css             # Global styles
│   └── vite-env.d.ts       # Type definitions
├── index.html              # HTML template
├── vite.config.ts          # Vite configuration
├── svelte.config.ts        # Svelte configuration
├── tailwind.config.js      # Tailwind CSS configuration
├── postcss.config.js       # PostCSS configuration
├── tsconfig.json           # TypeScript configuration
└── package.json            # Dependencies and scripts
```

## Customization

### Updating Content

Edit the component files in `src/components/` to update your resume content:

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
npm run dev -- --port 3000
```

### Build Errors

Clear cache and reinstall:
```bash
rm -rf node_modules package-lock.json
npm install
```

### Type Errors

Run type check to see all errors:
```bash
npm run check
```
