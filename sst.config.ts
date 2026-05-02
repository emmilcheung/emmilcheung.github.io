/// <reference path="./.sst/platform/config.d.ts" />

/**
 * SST v4 — Infrastructure for the resume RAG chat Lambda.
 *
 * Deploys:
 *   - Lambda function (Node 24, 512 MB) with bundled resume.db
 *   - API Gateway V2 (HTTP API) with CORS locked to GitHub Pages origin
 *
 * Usage:
 *   pnpm sst install          # first time only
 *   pnpm sst secret set OpenRouterKey sk-or-...
 *   pnpm sst deploy --stage production
 *
 * After deploy, capture the chatUrl output and add it as
 * VITE_CHAT_URL in the GitHub Actions secret.
 */

export default $config({
  app(input) {
    return {
      name: 'emmil-portfolio',
      removal: input?.stage === 'production' ? 'retain' : 'remove',
      protect: input?.stage === 'production',
      home: 'aws',
      providers: { aws: { region: 'ap-east-1' } }, // Hong Kong — lowest latency for HK-based visitors
    };
  },

  async run() {
    const openrouterKey = new sst.Secret('OpenRouterKey');

    const allowedOrigin =
      $app.stage === 'production'
        ? 'https://emmilcheung.github.io'
        : '*'; // allow any origin in dev/staging

    const chat = new sst.aws.Function('Chat', {
      handler: 'packages/functions/src/chat.handler',
      runtime: 'nodejs24.x',
      memory: '512 MB',
      timeout: '30 seconds',

      // Bundle resume.db from data/ into the Lambda zip at /var/task/resume.db
      copyFiles: [{ from: 'data/resume.db', to: 'resume.db' }],

      environment: {
        OPENROUTER_API_KEY: openrouterKey.value,
        ALLOWED_ORIGIN: allowedOrigin,
        // In Lambda, copyFiles places the db at /var/task/resume.db.
        // In sst dev the artifacts dir is used as cwd, so we pass the
        // absolute path explicitly instead.
        DB_PATH: $app.stage === 'production'
          ? '/var/task/resume.db'
          : new URL('data/resume.db', `file://${process.cwd()}/`).pathname,
      },

      // Tell SST's bundler to install the native better-sqlite3 binary
      // for the Lambda linux-x64 target rather than the host binary.
      nodejs: {
        install: ['better-sqlite3', 'sqlite-vec'],
      },
    });

    const api = new sst.aws.ApiGatewayV2('Api', {
      cors: {
        allowOrigins: [allowedOrigin],
        allowMethods: ['POST', 'OPTIONS'],
        allowHeaders: ['Content-Type'],
        maxAge: '1 day',
      },
    });

    api.route('POST /chat', chat.arn);

    return {
      chatUrl: $interpolate`${api.url}/chat`,
    };
  },
});
