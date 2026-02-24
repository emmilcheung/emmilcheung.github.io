#!/bin/bash

# Setup script for Emmil Cheung Portfolio

echo "🚀 Setting up Emmil Cheung Portfolio..."

# Install dependencies
echo "📦 Installing dependencies..."
npm install

# Build the project
echo "🔨 Building the project..."
npm run build

echo "✅ Setup complete!"
echo ""
echo "To start development server:"
echo "  npm run dev"
echo ""
echo "To deploy to GitHub Pages:"
echo "  npm run deploy"
echo ""
echo "Or simply push to master branch for automatic deployment via GitHub Actions"
