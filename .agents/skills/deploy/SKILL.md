# /deploy Command - Deploy Project

## Trigger
- `/deploy`
- `/deploy [platform]`
- `/deploy --preview`

## Purpose
Deploy the built project to a hosting platform using OpenAgents.

## Prerequisites
- Project must be built (run `/build` first)
- Dependencies must be installed

## Workflow

### 1. Detect project type
From `.openagent-ux.json`:
- Framework (astro, nextjs, gatsby, etc.)
- Build command (npm run build, astro build, etc.)
- Output directory (.next, dist, public, etc.)

### 2. Deploy options

**Local Network (default)**
- Uses OpenAgents agn daemon
- Creates local tunnel with `agn tunnel`
- Provides public preview URL
- Best for development/preview

**Vercel**
```bash
npx vercel --prod
```
- Best for Next.js
- Automatic detection
- CI/CD integration

**Netlify**
```bash
npx netlify deploy --prod
```
- Works with all static sites
- Drag-and-drop alternative

**Cloudflare Pages**
```bash
npx wrangler pages deploy
```
- Free tier
- Fast global CDN

### 3. Execute deployment
- Build the project first (if not built)
- Run deploy command
- Capture output URL
- Update config with deploy info

### 4. Agent delegation
- `/agent deploy` → Handle deployment via OpenAgents

## Output
- Deployed URL
- Build artifacts deployed
- Config updated with deploy info

## Example

```
User: /deploy

Agent: Detected: Next.js project
Deploying to Vercel...

✓ Building project... (npm run build)
✓ Deploying to Vercel...
✓ Deployed: https://my-project.vercel.app

You can also:
- /deploy --preview  (preview without prod)
- /deploy netlify    (deploy to Netlify)
- /deploy cf         (deploy to Cloudflare)
```

## Platforms

| Platform | Command | Best For |
|----------|---------|----------|
| Vercel | `npx vercel` | Next.js |
| Netlify | `npx netlify deploy` | Static sites |
| Cloudflare | `npx wrangler pages` | Free hosting |
| Local tunnel | `agn tunnel` | Development preview |