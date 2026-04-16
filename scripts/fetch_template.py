#!/usr/bin/env python3
"""
Template Fetcher - Downloads template sources on demand
Used by agents to fetch templates when user selects one.
"""

import os
import subprocess
import shutil
from pathlib import Path
from typing import Optional

# Template sources - GitHub repositories to clone
TEMPLATE_SOURCES = {
    # Astro
    "astrowind": {
        "repo": "onwidget/astrowind",
        "framework": "astro",
        "description": "Production-ready SaaS/marketing template"
    },
    "astroship": {
        "repo": "surjithctly/astroship",
        "framework": "astro", 
        "description": "Startup marketing template"
    },
    "astro-paper": {
        "repo": "satnaing/astro-paper",
        "framework": "astro",
        "description": "Minimal SEO-friendly blog theme"
    },
    "astrofy": {
        "repo": "manuelernestog/astrofy",
        "framework": "astro",
        "description": "Personal portfolio template"
    },
    "flowbite-admin": {
        "repo": "flowbite/flowbite-admin-dashboard",
        "framework": "astro",
        "description": "Admin dashboard template"
    },
    "starlight-docs": {
        "repo": "withastro/starlight",
        "framework": "astro",
        "description": "Documentation template"
    },
    
    # Gatsby
    "gatsby-starter-blog": {
        "repo": "gatsbyjs/gatsby-starter-blog",
        "framework": "gatsby",
        "description": "Official Gatsby blog starter"
    },
    "gatsby-portfolio-cara": {
        "repo": "LekoArts/gatsby-starter-portfolio-cara",
        "framework": "gatsby",
        "description": "Colorful portfolio with parallax"
    },
    "gatsby-minimal-blog": {
        "repo": "LekoArts/gatsby-starter-minimal-blog",
        "framework": "gatsby",
        "description": "Typography-driven blog"
    },
    "gatsby-advanced-starter": {
        "repo": "Vagr9K/gatsby-advanced-starter",
        "framework": "gatsby",
        "description": "Minimal base for advanced sites"
    },
    
    # Next.js
    "nextjs-blog": {
        "repo": "vercel/next.js",
        "path": "examples/blog}",
        "framework": "nextjs",
        "description": "Official Next.js blog"
    },
    "nextjs-commerce": {
        "repo": "vercel/commerce",
        "framework": "nextjs",
        "description": "E-commerce starter"
    },
    "create-t3-app": {
        "repo": "t3dotoss/create-t3-app",
        "framework": "nextjs",
        "description": "Full-stack SaaS starter"
    },
    
    # Gatsby more
    "gatsby-decap-cms": {
        "repo": "decaporg/decap-sites",
        "path": "gatsby-starter-decap-cms",
        "framework": "gatsby",
        "description": "Blog with Decap CMS"
    },
    "gatsby-starter-shopify": {
        "repo": "gatsbyjs/gatsby-starter-shopify",
        "framework": "gatsby",
        "description": "Shopify e-commerce"
    },
    
    # Nuxt
    "nuxt-starter": {
        "repo": "nuxt/starter",
        "framework": "nuxt",
        "description": "Official Nuxt starter"
    },
    "nuxt-content-template": {
        "repo": "nuxt/content",
        "path": "templates/content",
        "framework": "nuxt",
        "description": "Content-powered blog"
    },
}


def get_template_dir() -> Path:
    """Get the templates directory path."""
    return Path("templates")


def fetch_template(template_id: str, target_dir: Optional[str] = None) -> bool:
    """
    Fetch a template from GitHub.
    
    Args:
        template_id: Key from TEMPLATE_SOURCES
        target_dir: Optional custom directory name
        
    Returns:
        True if successful, False otherwise
    """
    if template_id not in TEMPLATE_SOURCES:
        print(f"Error: Unknown template '{template_id}'")
        print(f"Available: {list(TEMPLATE_SOURCES.keys())}")
        return False
    
    source = TEMPLATE_SOURCES[template_id]
    repo = source["repo"]
    subpath = source.get("path", "")
    
    # Determine target directory
    if target_dir is None:
        target_dir = template_id
    
    template_path = get_template_dir() / source["framework"] / target_dir
    
    # Create parent directory
    template_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Clone the repository
    repo_url = f"https://github.com/{repo}.git"
    print(f"Cloning {repo_url}...")
    
    try:
        # Use git clone --depth 1 for faster cloning
        result = subprocess.run(
            ["git", "clone", "--depth", "1", repo_url, str(template_path)],
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )
        
        if result.returncode != 0:
            print(f"Error cloning: {result.stderr}")
            return False
            
        # If template has subpath, move contents
        if subpath:
            subpath_dir = template_path / subpath
            if subpath_dir.exists():
                # Move subpath contents to root
                for item in subpath_dir.iterdir():
                    dest = template_path / item.name
                    if item.is_dir():
                        shutil.move(str(item), str(dest))
                    else:
                        shutil.copy2(str(item), str(dest))
                # Remove empty subpath
                shutil.rmtree(subpath_dir)
                
        print(f"Template '{template_id}' cloned to {template_path}")
        return True
        
    except subprocess.TimeoutExpired:
        print("Error: Clone timed out after 5 minutes")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def list_templates() -> None:
    """List all available templates."""
    print("\nAvailable Templates:")
    print("=" * 60)
    
    by_framework = {}
    for tid, info in TEMPLATE_SOURCES.items():
        fw = info["framework"]
        if fw not in by_framework:
            by_framework[fw] = []
        by_framework[fw].append((tid, info["description"]))
    
    for framework, templates in by_framework.items():
        print(f"\n{'='*60}")
        print(f"📦 {framework.upper()} ({len(templates)})")
        print("=" * 60)
        for tid, desc in templates:
            print(f"  • {tid}")
            print(f"    {desc}")


def main():
    import sys
    
    if len(sys.argv) < 2:
        list_templates()
        sys.exit(0)
    
    command = sys.argv[1]
    
    if command == "list":
        list_templates()
    elif command == "fetch" and len(sys.argv) >= 3:
        template_id = sys.argv[2]
        target = sys.argv[3] if len(sys.argv) > 3 else None
        success = fetch_template(template_id, target)
        sys.exit(0 if success else 1)
    else:
        print(f"Usage: {sys.argv[0]} [list|fetch <template-id>]")
        sys.exit(1)


if __name__ == "__main__":
    main()