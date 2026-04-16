#!/usr/bin/env python3
"""
Template Fetcher - Downloads template sources from GitHub
Run with: python scripts/fetch_all_templates.py
"""

import os
import subprocess
import shutil
from pathlib import Path
from typing import Optional
import time

# All template sources - GitHub repositories to clone
TEMPLATE_SOURCES = {
    # === ASTRO TEMPLATES (12) ===
    "astrowind": {
        "repo": "onwidget/astrowind",
        "framework": "astro",
        "description": "Production-ready SaaS/marketing template",
        "categories": ["saas", "marketing", "landing", "blog"]
    },
    "astroship": {
        "repo": "surjithctly/astroship",
        "framework": "astro",
        "description": "Startup marketing template",
        "categories": ["saas", "startup", "landing"]
    },
    "astro-paper": {
        "repo": "satnaing/astro-paper",
        "framework": "astro",
        "description": "Minimal SEO-friendly blog theme",
        "categories": ["blog", "portfolio"]
    },
    "astrofy": {
        "repo": "manuelernestog/astrofy",
        "framework": "astro",
        "description": "Personal portfolio template",
        "categories": ["portfolio", "personal"]
    },
    "blogsmith-free": {
        "repo": "Cosmic-Themes/blogsmithfree",
        "framework": "astro",
        "description": "Blog theme with Tailwind v4",
        "categories": ["blog"]
    },
    "astro-cactus": {
        "repo": "chrismwilliams/astro-theme-cactus",
        "framework": "astro",
        "description": "Clean blog and docs theme",
        "categories": ["blog", "docs"]
    },
    "flowbite-admin": {
        "repo": "flowbite/flowbite-admin-dashboard",
        "framework": "astro",
        "description": "Admin dashboard with Flowbite",
        "categories": ["dashboard", "admin"]
    },
    "starlight-docs": {
        "repo": "withastro/starlight",
        "framework": "astro",
        "description": "Official Astro documentation theme",
        "categories": ["documentation"]
    },
    "astro-ecommerce": {
        "repo": "Charca/astro-ecommerce",
        "framework": "astro",
        "description": "E-commerce template",
        "categories": ["ecommerce"]
    },
    "accessible-astro-starter": {
        "repo": "markteekay/accessible-astro-starter",
        "framework": "astro",
        "description": "Accessible marketing starter",
        "categories": ["blog", "marketing"]
    },
    "astro-micro": {
        "repo": "nickymarino/astro-micro",
        "framework": "astro",
        "description": "Minimal blog starter",
        "categories": ["blog"]
    },
    "astro-boilerplate": {
        "repo": "ixartz/Astro-Boilerplate",
        "framework": "astro",
        "description": "Production boilerplate",
        "categories": ["boilerplate", "portfolio"]
    },

    # === GATSBY TEMPLATES (10) ===
    "gatsby-starter-blog": {
        "repo": "gatsbyjs/gatsby-starter-blog",
        "framework": "gatsby",
        "description": "Official Gatsby blog starter",
        "categories": ["blog"]
    },
    "gatsby-portfolio-cara": {
        "repo": "LekoArts/gatsby-starter-portfolio-cara",
        "framework": "gatsby",
        "description": "Colorful portfolio with parallax",
        "categories": ["portfolio"]
    },
    "gatsby-minimal-blog": {
        "repo": "LekoArts/gatsby-starter-minimal-blog",
        "framework": "gatsby",
        "description": "Typography-driven blog",
        "categories": ["blog"]
    },
    "gatsby-advanced-starter": {
        "repo": "Vagr9K/gatsby-advanced-starter",
        "framework": "gatsby",
        "description": "Minimal base for advanced sites",
        "categories": ["boilerplate", "blog"]
    },
    "gatsby-decap-cms": {
        "repo": "decaporg/gatsby-starter-decap-cms",
        "framework": "gatsby",
        "description": "Blog with Decap CMS",
        "categories": ["blog", "cms"]
    },
    "gatsby-starter-shopify": {
        "repo": "gatsbyjs/gatsby-starter-shopify",
        "framework": "gatsby",
        "description": "Shopify e-commerce integration",
        "categories": ["ecommerce"]
    },
    "gatsby-gitbook-starter": {
        "repo": "hasura/gatsby-gitbook-starter",
        "framework": "gatsby",
        "description": "Documentation site builder",
        "categories": ["documentation"]
    },
    "gatsby-starter-ghost": {
        "repo": "TryGhost/gatsby-starter-ghost",
        "framework": "gatsby",
        "description": "Ghost CMS integration",
        "categories": ["blog"]
    },
    "gatsby-universal": {
        "repo": "gatsbyjs/gatsby-starter-universal",
        "framework": "gatsby",
        "description": "Marketing and SaaS starter",
        "categories": ["marketing", "saas"]
    },
    "gatsby-starter-wordpress": {
        "repo": "gatsbyjs/gatsby-starter-wordpress",
        "framework": "gatsby",
        "description": "WordPress CMS integration",
        "categories": ["blog"]
    },

    # === NEXT.JS TEMPLATES (10) ===
    "nextjs-blog-starter": {
        "repo": "vercel/next.js",
        "path": "examples/blog",
        "framework": "nextjs",
        "description": "Official Next.js blog starter",
        "categories": ["blog"],
        "note": "Use --example blog with create-next-app"
    },
    "nextjs-commerce": {
        "repo": "vercel/commerce",
        "framework": "nextjs",
        "description": "Vercel e-commerce starter",
        "categories": ["ecommerce"]
    },
    "create-t3-app": {
        "repo": "t3dotoss/create-t3-app",
        "framework": "nextjs",
        "description": "Full-stack SaaS with tRPC + Prisma",
        "categories": ["saas", "fullstack"],
        "note": "Use npm create t3-app@latest"
    },
    "nextjs-dashboard": {
        "repo": "vercel/next.js",
        "path": "examples/dashboard",
        "framework": "nextjs",
        "description": "Admin dashboard with App Router",
        "categories": ["dashboard", "admin"],
        "note": "Use --example dashboard with create-next-app"
    },
    "nextjs-saas-starter": {
        "repo": "vercel/next.js",
        "path": "examples/app-router-starter",
        "framework": "nextjs",
        "description": "SaaS application starter",
        "categories": ["saas", "landing"]
    },
    "nextjs-docs": {
        "repo": "vercel/next.js",
        "path": "examples/docs-with-notion",
        "framework": "nextjs",
        "description": "Documentation with Notion",
        "categories": ["documentation"]
    },
    "nextjs-portfolio": {
        "repo": "leerob/leerob.io",
        "framework": "nextjs",
        "description": "Popular portfolio template",
        "categories": ["portfolio"]
    },
    "nextjs-medusa": {
        "repo": "medusajs/nextjs-starter-medusa",
        "framework": "nextjs",
        "description": "E-commerce with Medusa",
        "categories": ["ecommerce"]
    },
    "nextjs-stripe-saas": {
        "repo": "jjacobs17/next-saas-starter",
        "framework": "nextjs",
        "description": "Stripe-integrated SaaS starter",
        "categories": ["saas", "payments"]
    },
    "nextjs-shopify": {
        "repo": "shopify/nextjs-buy-sdk-examples",
        "framework": "nextjs",
        "description": "Shopify integration example",
        "categories": ["ecommerce"]
    },

    # === NUXT TEMPLATES (8) ===
    "nuxt-starter": {
        "repo": "nuxt/starter",
        "framework": "nuxt",
        "description": "Official Nuxt starter",
        "categories": ["boilerplate"]
    },
    "nuxt-content-template": {
        "repo": "nuxt/content",
        "path": "templates/content",
        "framework": "nuxt",
        "description": "Content-powered blog",
        "categories": ["blog", "docs"]
    },
    "nuxt-docus": {
        "repo": "nuxt/content",
        "path": "templates/docs",
        "framework": "nuxt",
        "description": "Documentation theme",
        "categories": ["documentation"]
    },
    "nuxt-commerce": {
        "repo": "nuxt-modules/shopify",
        "framework": "nuxt",
        "description": "Shopify integration",
        "categories": ["ecommerce"]
    },
    "nuxt-tailwindcss-starter": {
        "repo": "nuxt/ui-starter",
        "framework": "nuxt",
        "description": "Nuxt UI starter with Tailwind",
        "categories": ["saas", "landing"]
    },
    "nuxt-portfolio-theme": {
        "repo": "LekoArts/nuxt-portfolio-starter",
        "framework": "nuxt",
        "description": "Creative portfolio starter",
        "categories": ["portfolio"]
    },
    "nuxt-layered-architecture": {
        "repo": "nuxt/framework",
        "path": "examples/advanced",
        "framework": "nuxt",
        "description": "Layered architecture example",
        "categories": ["boilerplate"]
    },
    "nuxt-module-starter": {
        "repo": "nuxt/modules",
        "path": "package-template",
        "framework": "nuxt",
        "description": "Nuxt module development starter",
        "categories": ["development"]
    },

    # === HUGO TEMPLATES (5) ===
    "hugo-paper": {
        "repo": "nanxstats/hugo-paper",
        "framework": "hugo",
        "description": "Clean paper-like theme",
        "categories": ["blog"]
    },
    "hugo-ananke": {
        "repo": "theNewDynamic/gohugo-theme-ananke",
        "framework": "hugo",
        "description": "Official Hugo theme",
        "categories": ["blog", "marketing"]
    },
    "hugo-coder": {
        "repo": "joegilliarman/hugo-coder",
        "framework": "hugo",
        "description": "Developer blog theme",
        "categories": ["blog", "portfolio"]
    },
    "hugo-papermod": {
        "repo": "adityatelange/hugo-PaperMod",
        "framework": "hugo",
        "description": "Feature-rich blog theme",
        "categories": ["blog"]
    },
    "hugo-universal": {
        "repo": "devcows/hugo-universal-theme",
        "framework": "hugo",
        "description": "Multi-purpose business theme",
        "categories": ["business", "marketing"]
    },

    # === SVELTE TEMPLATES (8) ===
    "sveltekit-blog": {
        "repo": "sveltejs/kit",
        "path": "packages/create-svelte/templates/default",
        "framework": "svelte",
        "description": "Official SvelteKit default template",
        "categories": ["blog", "boilerplate"]
    },
    "sveltekit-minimal": {
        "repo": "sveltejs/kit",
        "path": "packages/create-svelte/templates/skeleton",
        "framework": "svelte",
        "description": "SvelteKit minimal skeleton",
        "categories": ["boilerplate"]
    },
    "sveltekit-spa": {
        "repo": "sveltejs/kit",
        "path": "packages/create-svelte/templates/skeletonlib",
        "framework": "svelte",
        "description": "SvelteKit SPA template",
        "categories": ["spa"]
    },
    "svelte-preprocessor": {
        "repo": "sveltejs/preprocess",
        "framework": "svelte",
        "description": "Svelte preprocessor template",
        "categories": ["boilerplate"]
    },
    "svelte-routify": {
        "repo": "sveltejs/routify",
        "framework": "svelte",
        "description": "Svelte routing template",
        "categories": ["routing"]
    },
    "svelte-sapper": {
        "repo": "sveltejs/sapper-template",
        "framework": "svelte",
        "description": "Sapper (Svelte) template",
        "categories": ["fullstack"]
    },
    "sveltekit-pocketbase": {
        "repo": "rajatsharma/sveltekit-pocketbase",
        "framework": "svelte",
        "description": "SvelteKit + PocketBase starter",
        "categories": ["saas", "fullstack"]
    },
    "svelte-stripe": {
        "repo": "ghostdevv/svelte-stripe",
        "framework": "svelte",
        "description": "Svelte Stripe template",
        "categories": ["payments", "saas"]
    },

    # === HTML TEMPLATES (from various sources) ===
    "html5up-bold": {
        "repo": "justinribeiro/html5up-bold",
        "framework": "html",
        "description": "Business and portfolio template",
        "categories": ["business", "portfolio"]
    },
    "html5up-stellar": {
        "repo": "justinribeiro/html5up-stellar",
        "framework": "html",
        "description": "Single-page landing template",
        "categories": ["landing", "business"]
    },
    "html5up-multiverse": {
        "repo": "justinribeiro/html5up-multiverse",
        "framework": "html",
        "description": "Gallery and portfolio template",
        "categories": ["portfolio"]
    },
    "html5up-arcana": {
        "repo": "justinribeiro/html5up-arcana",
        "framework": "html",
        "description": "Business services template",
        "categories": ["business"]
    },
    "html5up-fifty": {
        "repo": "justinribeiro/html5up-fifty",
        "framework": "html",
        "description": "Clean landing page",
        "categories": ["landing"]
    },
}

# Community component libraries
COMMUNITY_SOURCES = {
    # UI Component Libraries
    "shadcn-ui": {
        "repo": "shadcn-ui/ui",
        "framework": "react",
        "description": "Beautifully designed React components",
        "categories": ["components", "ui-kit"]
    },
    "radix-ui": {
        "repo": "radix-ui/primitives",
        "framework": "react",
        "description": "Unstyled accessible components",
        "categories": ["components", "ui-kit"]
    },
    "headless-ui": {
        "repo": "tailwindlabs/headlessui",
        "framework": "react",
        "description": "Accessible UI components",
        "categories": ["components", "ui-kit"]
    },
    "ark-ui": {
        "repo": "chakra-ui/ark",
        "framework": "react",
        "description": "Headless UI for React",
        "categories": ["components", "ui-kit"]
    },

    # Tailwind Themes
    "tailwind-ui": {
        "repo": "tailwindlabs/tailwindcss-ui",
        "framework": "tailwind",
        "description": "Tailwind UI component library",
        "categories": ["components", "ui-kit"]
    },
    "flowbite-react": {
        "repo": "flowbite/flowbite-react",
        "framework": "react",
        "description": "Flowbite React components",
        "categories": ["components", "ui-kit"]
    },
    "daisyui": {
        "repo": "saadeghi/daisyui",
        "framework": "tailwind",
        "description": "Tailwind CSS component library",
        "categories": ["components", "ui-kit"]
    },

    # Motion/Animation
    "framer-motion": {
        "repo": "framer/motion",
        "framework": "react",
        "description": "Animation library for React",
        "categories": ["animation", "motion"]
    },
    "react-spring": {
        "repo": "react-spring/react-spring",
        "framework": "react",
        "description": "Spring-based animation",
        "categories": ["animation", "motion"]
    },
    "motion-one": {
        "repo": "motiondivision/motion",
        "framework": "vanilla",
        "description": "Lightweight animation library",
        "categories": ["animation", "motion"]
    },

    # Design Systems
    "chakra-ui": {
        "repo": "chakra-ui/chakra-ui",
        "framework": "react",
        "description": "Component library for React",
        "categories": ["design-system", "ui-kit"]
    },
    "mantine": {
        "repo": "mantinedev/mantine",
        "framework": "react",
        "description": "React components library",
        "categories": ["design-system", "ui-kit"]
    },
    "primereact": {
        "repo": "primefaces/primereact",
        "framework": "react",
        "description": "React UI Component Library",
        "categories": ["design-system", "ui-kit"]
    },
    "ant-design": {
        "repo": "ant-design/ant-design",
        "framework": "react",
        "description": "Enterprise UI components",
        "categories": ["design-system", "ui-kit"]
    },
    "ui-shadcn": {
        "repo": "nuannat/TailwindUI-Kit",
        "framework": "tailwind",
        "description": "Tailwind UI Kit components",
        "categories": ["design-system", "ui-kit"]
    },

    # Icon Libraries (just the main repos)
    "heroicons": {
        "repo": "tailwindlabs/heroicons",
        "framework": "svg",
        "description": "SVG icons by Tailwind",
        "categories": ["icons"]
    },
    "lucide-react": {
        "repo": "lucide-icons/lucide",
        "framework": "react",
        "description": "Beautiful & consistent icons",
        "categories": ["icons"]
    },
    "phosphor-icons": {
        "repo": "phosphor-icons/phosphor-home",
        "framework": "svg",
        "description": "Phosphor Icons repo",
        "categories": ["icons"]
    },
    "remix-icon": {
        "repo": "Remix-Design/RemixIcon",
        "framework": "svg",
        "description": "Open source icon library",
        "categories": ["icons"]
    },
}

def get_templates_dir() -> Path:
    """Get the templates directory path."""
    return Path("templates")

def get_components_dir() -> Path:
    """Get the community components directory path."""
    return Path("components/community")

def fetch_repository(repo: str, target_path: Path, subpath: str = "", timeout: int = 300) -> bool:
    """Clone a single repository."""
    repo_url = f"https://github.com/{repo}.git"
    print(f"  Cloning {repo_url}...")

    # Remove existing directory if it exists
    if target_path.exists():
        print(f"  Removing existing directory: {target_path}")
        shutil.rmtree(target_path)

    try:
        result = subprocess.run(
            ["git", "clone", "--depth", "1", repo_url, str(target_path)],
            capture_output=True,
            text=True,
            timeout=timeout
        )

        if result.returncode != 0:
            print(f"  Error: {result.stderr}")
            return False

        # Handle subpath extraction
        if subpath:
            subpath_dir = target_path / subpath
            if subpath_dir.exists():
                for item in subpath_dir.iterdir():
                    dest = target_path / item.name
                    if item.is_dir():
                        if dest.exists():
                            shutil.rmtree(dest)
                        shutil.move(str(item), str(dest))
                    else:
                        shutil.copy2(str(item), str(dest))
                shutil.rmtree(subpath_dir)

        return True

    except subprocess.TimeoutExpired:
        print(f"  Error: Clone timed out after {timeout}s")
        return False
    except Exception as e:
        print(f"  Error: {e}")
        return False

def fetch_template(template_id: str) -> bool:
    """Fetch a single template."""
    if template_id not in TEMPLATE_SOURCES:
        print(f"Unknown template: {template_id}")
        return False

    source = TEMPLATE_SOURCES[template_id]
    repo = source["repo"]
    subpath = source.get("path", "")

    template_path = get_templates_dir() / source["framework"] / template_id
    template_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"Fetching {template_id}...")
    return fetch_repository(repo, template_path, subpath)

def fetch_community_component(component_id: str) -> bool:
    """Fetch a community component library."""
    if component_id not in COMMUNITY_SOURCES:
        print(f"Unknown component: {component_id}")
        return False

    source = COMMUNITY_SOURCES[component_id]
    repo = source["repo"]

    component_path = get_components_dir() / component_id
    component_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"Fetching component {component_id}...")
    return fetch_repository(repo, component_path, "")

def fetch_all_templates() -> dict:
    """Fetch all templates."""
    results = {}

    by_framework = {}
    for tid, info in TEMPLATE_SOURCES.items():
        fw = info["framework"]
        if fw not in by_framework:
            by_framework[fw] = []
        by_framework[fw].append(tid)

    total = len(TEMPLATE_SOURCES)
    current = 0

    for framework, template_ids in by_framework.items():
        print(f"\n{'='*60}")
        print(f"Fetching {framework.upper()} templates ({len(template_ids)})")
        print("="*60)

        for template_id in template_ids:
            current += 1
            print(f"[{current}/{total}] ", end="")
            success = fetch_template(template_id)
            results[template_id] = "✓" if success else "✗"

    return results

def fetch_all_community_components() -> dict:
    """Fetch all community components."""
    results = {}

    total = len(COMMUNITY_SOURCES)
    current = 0

    print(f"\n{'='*60}")
    print(f"Fetching Community Components ({total})")
    print("="*60)

    for component_id in COMMUNITY_SOURCES.keys():
        current += 1
        print(f"[{current}/{total}] ", end="")
        success = fetch_community_component(component_id)
        results[component_id] = "✓" if success else "✗"

    return results

def list_templates() -> None:
    """List all available templates."""
    print("\nAvailable Templates:")
    print("=" * 60)

    by_framework = {}
    for tid, info in TEMPLATE_SOURCES.items():
        fw = info["framework"]
        if fw not in by_framework:
            by_framework[fw] = []
        by_framework[fw].append((tid, info["description"], info.get("categories", [])))

    for framework, templates in by_framework.items():
        print(f"\n{'='*60}")
        print(f"📦 {framework.upper()} ({len(templates)})")
        print("=" * 60)
        for tid, desc, cats in templates:
            print(f"  • {tid}")
            print(f"    {desc}")
            print(f"    Tags: {', '.join(cats)}")

    print("\n\nCommunity Components:")
    print("=" * 60)
    for cid, info in COMMUNITY_SOURCES.items():
        print(f"  • {cid}: {info['description']}")

def generate_registry():
    """Generate a JSON registry of all templates and components."""
    import json

    registry = {
        "templates": [],
        "components": [],
        "total": {
            "templates": len(TEMPLATE_SOURCES),
            "components": len(COMMUNITY_SOURCES)
        }
    }

    for tid, info in TEMPLATE_SOURCES.items():
        registry["templates"].append({
            "id": tid,
            "framework": info["framework"],
            "description": info["description"],
            "categories": info.get("categories", []),
            "path": f"templates/{info['framework']}/{tid}"
        })

    for cid, info in COMMUNITY_SOURCES.items():
        registry["components"].append({
            "id": cid,
            "framework": info["framework"],
            "description": info["description"],
            "categories": info.get("categories", []),
            "path": f"components/community/{cid}"
        })

    registry_path = get_templates_dir().parent / "templates-registry.json"
    with open(registry_path, "w") as f:
        json.dump(registry, f, indent=2)

    print(f"\nRegistry generated: {registry_path}")

def main():
    import sys

    if len(sys.argv) < 2:
        list_templates()
        print("\n" + "="*60)
        print("USAGE:")
        print("  python fetch_all_templates.py templates   - Fetch all 50+ templates")
        print("  python fetch_all_templates.py components  - Fetch community components")
        print("  python fetch_all_templates.py all         - Fetch everything")
        print("  python fetch_all_templates.py registry   - Generate registry JSON")
        print("  python fetch_all_templates.py list       - List available")
        sys.exit(0)

    command = sys.argv[1]

    if command == "list":
        list_templates()
    elif command == "templates":
        results = fetch_all_templates()
        print("\n" + "="*60)
        print("RESULTS:")
        for tid, status in results.items():
            print(f"  {status} {tid}")
        print("="*60)
    elif command == "components":
        results = fetch_all_community_components()
        print("\n" + "="*60)
        print("RESULTS:")
        for cid, status in results.items():
            print(f"  {status} {cid}")
        print("="*60)
    elif command == "all":
        print("\n" + "="*60)
        print("FETCHING ALL TEMPLATES AND COMPONENTS")
        print("="*60)
        t_results = fetch_all_templates()
        c_results = fetch_all_community_components()
        generate_registry()
        print("\n" + "="*60)
        print("FINAL RESULTS:")
        print(f"  Templates: {sum(1 for v in t_results.values() if v == '✓')}/{len(t_results)}")
        print(f"  Components: {sum(1 for v in c_results.values() if v == '✓')}/{len(c_results)}")
        print("="*60)
    elif command == "registry":
        generate_registry()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()