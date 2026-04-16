#!/usr/bin/env python3
"""
Template Agent Integration
Enables agents to help users select and customize templates.
"""

import yaml
import os
from pathlib import Path
from typing import List, Dict, Optional

TEMPLATES_DIR = Path(__file__).parent.parent / "templates"

class TemplateSelector:
    """Helps agents guide users through template selection."""
    
    def __init__(self):
        self.catalog = self._load_catalog()
        
    def _load_catalog(self) -> dict:
        """Load template catalog."""
        catalog_path = TEMPLATES_DIR / "registry" / "catalog.yaml"
        if catalog_path.exists():
            with open(catalog_path) as f:
                return yaml.safe_load(f)
        return {"templates": []}
    
    def get_by_category(self, category: str) -> List[Dict]:
        """Get templates by category."""
        return [
            t for t in self.catalog.get("templates", [])
            if category in t.get("category", [])
        ]
    
    def get_by_framework(self, framework: str) -> List[Dict]:
        """Get templates by framework."""
        return [
            t for t in self.catalog.get("templates", [])
            if t.get("framework") == framework
        ]
    
    def search(self, query: str) -> List[Dict]:
        """Search templates by name or description."""
        query = query.lower()
        return [
            t for t in self.catalog.get("templates", [])
            if query in t.get("name", "").lower() 
            or query in t.get("description", "").lower()
        ]
    
    def get(self, template_id: str) -> Optional[Dict]:
        """Get specific template."""
        for t in self.catalog.get("templates", []):
            if t.get("id") == template_id:
                return t
        return None
    
    def list_frameworks(self) -> List[str]:
        """List all available frameworks."""
        return list(set(
            t.get("framework") 
            for t in self.catalog.get("templates", [])
        ))
    
    def list_categories(self) -> List[str]:
        """List all categories."""
        cats = set()
        for t in self.catalog.get("templates", []):
            cats.update(t.get("category", []))
        return sorted(cats)


def guide_user_selection(user_request: str) -> Dict:
    """
    Guide user through template selection based on their request.
    
    Returns recommended templates and questions to ask.
    """
    selector = TemplateSelector()
    request = user_request.lower()
    
    recommendations = {
        "questions": [],
        "templates": [],
        "framework_hint": None,
        "category_hint": None
    }
    
    # Detect framework hints
    frameworks = {
        "astro": ["astro"],
        "gatsby": ["gatsby"],
        "next": ["next", "nextjs", "vercel"],
        "nuxt": ["nuxt"],
        "hugo": ["hugo"],
        "html": ["html", "static"]
    }
    
    for fw, keywords in frameworks.items():
        if any(kw in request for kw in keywords):
            recommendations["framework_hint"] = fw
            break
    
    # Detect category hints
    categories = {
        "blog": ["blog", "post", "article", "writing"],
        "portfolio": ["portfolio", "showcase", "personal"],
        "saas": ["saas", "startup", "product", "landing"],
        "ecommerce": ["shop", "store", "product", "cart", "buy"],
        "dashboard": ["dashboard", "admin", "panel"],
        "documentation": ["docs", "documentation", "guide"]
    }
    
    for cat, keywords in categories.items():
        if any(kw in request for kw in keywords):
            recommendations["category_hint"] = cat
            break
    
    # Generate recommendations
    if recommendations["category_hint"]:
        templates = selector.get_by_category(recommendations["category_hint"])
    elif recommendations["framework_hint"]:
        templates = selector.get_by_framework(recommendations["framework_hint"])
    else:
        # Return top templates overall
        templates = sorted(
            selector.catalog.get("templates", []),
            key=lambda x: x.get("stars", 0),
            reverse=True
        )[:10]
    
    recommendations["templates"] = templates[:8]
    
    # Generate clarifying questions
    if not recommendations["framework_hint"]:
        recommendations["questions"].append(
            "Which framework do you prefer? (Astro, Gatsby, Next.js, Nuxt, Hugo, or plain HTML)"
        )
    
    if not recommendations["category_hint"]:
        recommendations["questions"].append(
            "What's the purpose of the site? (blog, portfolio, SaaS, e-commerce, dashboard, docs)"
        )
    
    recommendations["questions"].append(
        "Would you like to apply a custom design personality, or keep the template's default design?"
    )
    
    return recommendations


def format_template_list(templates: List[Dict]) -> str:
    """Format templates for display."""
    if not templates:
        return "No templates found."
    
    lines = ["**Available Templates:**\n"]
    for t in templates:
        stars = t.get("stars", "N/A")
        fw = t.get("framework", "unknown")
        cats = ", ".join(t.get("category", [])[:2])
        lines.append(f"- **{t['name']}** (`{t['id']}`)")
        lines.append(f"  - {t.get('description', '')}")
        lines.append(f"  - Framework: {fw} | Category: {cats} | Stars: {stars}")
        lines.append("")
    
    return "\n".join(lines)


# Example usage
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        request = " ".join(sys.argv[1:])
    else:
        request = "I want a blog template"
    
    result = guide_user_selection(request)
    
    print("=" * 60)
    print("TEMPLATE SELECTION GUIDE")
    print("=" * 60)
    
    if result["framework_hint"]:
        print(f"\nFramework detected: {result['framework_hint']}")
    if result["category_hint"]:
        print(f"Category detected: {result['category_hint']}")
    
    print("\n" + "-" * 60)
    print("Questions to ask user:")
    for q in result["questions"]:
        print(f"  • {q}")
    
    print("\n" + "-" * 60)
    print(format_template_list(result["templates"]))