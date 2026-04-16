#!/usr/bin/env python3
"""
Component Extractor - Analyzes templates and extracts reusable components
Creates a JSON registry mapping available components for pick n' mix functionality
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Set
from dataclasses import dataclass, field

# Component type mappings
COMPONENT_PATTERNS = {
    "button": ["button", "btn", "cta", "link-button", "action-button"],
    "navbar": ["navbar", "nav", "header", "navigation", "topbar", "menu"],
    "footer": ["footer", "site-footer", "bottom-bar"],
    "hero": ["hero", "banner", "jumbotron", "header-section", "landing-hero"],
    "card": ["card", "item-card", "post-card", "product-card", "feature-card"],
    "form": ["form", "input", "field", "contact-form", "newsletter", "signup"],
    "modal": ["modal", "dialog", "popup", "overlay"],
    "sidebar": ["sidebar", "side-nav", "aside"],
    "slider": ["slider", "carousel", "slideshow", "hero-slider"],
    "grid": ["grid", "masonry", "gallery", "features-grid"],
    "pricing": ["pricing", "price-table", "plan-card"],
    "testimonial": ["testimonial", "review", "quote", "feedback"],
    "team": ["team", "members", "staff", "about-team"],
    "faq": ["faq", "questions", "accordion"],
    "blog": ["blog", "post", "article", "news"],
    "portfolio": ["portfolio", "showcase", "work", "projects"],
    "ecommerce": ["product", "shop", "cart", "checkout", "store"],
    "dashboard": ["dashboard", "admin", "panel", "stats"],
    "docs": ["docs", "documentation", "guide", "api-docs"],
}

# Page section patterns
PAGE_SECTION_PATTERNS = {
    "hero-section": ["hero", "banner", "header", "jumbotron"],
    "features-section": ["features", "benefits", "what-we-offer"],
    "pricing-section": ["pricing", "plans", "packages", "prices"],
    "testimonials-section": ["testimonials", "reviews", "feedback", "clients"],
    "about-section": ["about", "story", "mission", "team"],
    "contact-section": ["contact", "get-in-touch", "reach-us"],
    "cta-section": ["cta", "call-to-action", "get-started", "join-us"],
    "faq-section": ["faq", "questions", "help"],
    "footer-section": ["footer", "bottom"],
    "blog-section": ["blog", "news", "articles", "latest-posts"],
    "portfolio-section": ["portfolio", "showcase", "work", "projects"],
    "products-section": ["products", "shop", "store", "catalog"],
}

# File extensions by framework
FRAMEWORK_FILE_TYPES = {
    "astro": [".astro", ".ts", ".jsx"],
    "gatsby": [".js", ".jsx", ".ts", ".tsx"],
    "nextjs": [".js", ".jsx", ".ts", ".tsx"],
    "nuxt": [".vue", ".js", ".ts"],
    "hugo": [".html", ".scss", ".css"],
    "html": [".html", ".css", ".js"],
    "react": [".jsx", ".tsx"],
    "vue": [".vue"],
}

@dataclass
class ExtractedComponent:
    name: str
    type: str
    path: str
    template: str
    framework: str
    file_type: str
    description: str = ""
    has_styles: bool = False
    has_props: bool = False

@dataclass
class ExtractedPage:
    name: str
    path: str
    template: str
    framework: str
    sections: List[str] = field(default_factory=list)
    has_layout: bool = False

class ComponentExtractor:
    """Analyzes templates and extracts reusable components."""

    def __init__(self, templates_dir: Path, components_dir: Path):
        self.templates_dir = templates_dir
        self.components_dir = components_dir
        self.registry: Dict = {
            "components": {},
            "pages": {},
            "sections": {},
            "layouts": {},
            "statistics": {}
        }
        self.processed_files: Set[str] = set()

    def scan_templates(self) -> None:
        """Scan all templates and extract components."""
        print("Scanning templates for components...")

        # Scan each framework
        for framework in ["astro", "gatsby", "nextjs", "nuxt", "hugo", "html"]:
            framework_path = self.templates_dir / framework
            if not framework_path.exists():
                continue

            print(f"  Processing {framework}...")
            for template_dir in framework_path.iterdir():
                if template_dir.is_dir() and not template_dir.name.startswith("."):
                    self._extract_from_template(template_dir, framework)

        # Scan community components
        if self.components_dir.exists():
            print("  Processing community components...")
            for component_dir in self.components_dir.iterdir():
                if component_dir.is_dir():
                    self._extract_from_component_lib(component_dir)

        self._generate_statistics()

    def _extract_from_template(self, template_dir: Path, framework: str) -> None:
        """Extract components from a single template."""
        template_name = template_dir.name

        # Find component directories
        component_dirs = ["components", "ui", "components/ui", "src/components"]
        for comp_dir_name in component_dirs:
            comp_dir = template_dir / comp_dir_name
            if comp_dir.exists():
                self._extract_components_from_dir(comp_dir, template_name, framework)

        # Find page directories
        page_dirs = ["pages", "src/pages", "app", "src/app", "layouts", "src/layouts"]
        for page_dir_name in page_dirs:
            page_dir = template_dir / page_dir_name
            if page_dir.exists():
                self._extract_pages_from_dir(page_dir, template_name, framework)

        # Find section patterns in source files
        self._scan_for_sections(template_dir, template_name, framework)

    def _extract_components_from_dir(self, comp_dir: Path, template: str, framework: str) -> None:
        """Extract components from a directory."""
        for file_path in comp_dir.rglob("*"):
            if not file_path.is_file():
                continue

            file_ext = file_path.suffix.lower()
            if file_ext not in [".jsx", ".tsx", ".vue", ".astro", ".js", ".ts"]:
                continue

            component_name = file_path.stem
            component_type = self._detect_component_type(component_name)

            if component_type not in self.registry["components"]:
                self.registry["components"][component_type] = []

            rel_path = str(file_path.relative_to(self.templates_dir.parent))

            # Check if component has props/parameters
            has_props = self._has_props(file_path)
            has_styles = self._has_styles(file_path)

            component_info = {
                "name": component_name,
                "template": template,
                "framework": framework,
                "path": rel_path,
                "type": component_type,
                "file_type": file_ext,
                "has_props": has_props,
                "has_styles": has_styles,
                "description": self._generate_description(component_name, component_type)
            }

            # Avoid duplicates
            if not any(c["path"] == rel_path for c in self.registry["components"][component_type]):
                self.registry["components"][component_type].append(component_info)

    def _extract_pages_from_dir(self, page_dir: Path, template: str, framework: str) -> None:
        """Extract pages from a directory."""
        for file_path in page_dir.rglob("*"):
            if not file_path.is_file():
                continue

            file_ext = file_path.suffix.lower()
            if file_ext not in [".jsx", ".tsx", ".vue", ".astro", ".js", ".ts", ".html"]:
                continue

            # Skip index files at root
            if file_path.parent == page_dir and file_path.stem == "index":
                continue

            page_name = file_path.stem
            page_type = self._detect_page_type(page_name)

            if page_type not in self.registry["pages"]:
                self.registry["pages"][page_type] = []

            rel_path = str(file_path.relative_to(self.templates_dir.parent))

            page_info = {
                "name": page_name,
                "template": template,
                "framework": framework,
                "path": rel_path,
                "type": page_type
            }

            if not any(p["path"] == rel_path for p in self.registry["pages"][page_type]):
                self.registry["pages"][page_type].append(page_info)

    def _scan_for_sections(self, template_dir: Path, template: str, framework: str) -> None:
        """Scan for page sections in template files."""
        for file_path in template_dir.rglob("*"):
            if not file_path.is_file():
                continue

            file_ext = file_path.suffix.lower()
            if file_ext not in [".jsx", ".tsx", ".vue", ".astro", ".html"]:
                continue

            try:
                content = file_path.read_text(encoding="utf-8", errors="ignore")
            except:
                continue

            # Look for section patterns
            for section_type, keywords in PAGE_SECTION_PATTERNS.items():
                for keyword in keywords:
                    if keyword in content.lower()[:500]:  # Check first part of file
                        if section_type not in self.registry["sections"]:
                            self.registry["sections"][section_type] = []

                        section_info = {
                            "template": template,
                            "framework": framework,
                            "path": str(file_path.relative_to(self.templates_dir.parent)),
                            "detected_from": keyword
                        }

                        if not any(s["path"] == section_info["path"] for s in self.registry["sections"][section_type]):
                            self.registry["sections"][section_type].append(section_info)
                        break

    def _extract_from_component_lib(self, lib_dir: Path) -> None:
        """Extract from community component libraries."""
        lib_name = lib_dir.name

        # Find package source
        packages_dir = lib_dir / "packages" if (lib_dir / "packages").exists() else lib_dir

        for file_path in packages_dir.rglob("*.tsx"):
            component_name = file_path.stem
            component_type = self._detect_component_type(component_name)

            if component_type not in self.registry["components"]:
                self.registry["components"][component_type] = []

            rel_path = str(file_path.relative_to(self.components_dir.parent))

            component_info = {
                "name": component_name,
                "template": f"community-{lib_name}",
                "framework": "react",
                "path": rel_path,
                "type": component_type,
                "file_type": ".tsx",
                "has_props": True,
                "has_styles": True,
                "description": f"Community component from {lib_name}"
            }

            if not any(c["path"] == rel_path for c in self.registry["components"].get(component_type, [])):
                self.registry["components"][component_type].append(component_info)

    def _detect_component_type(self, name: str) -> str:
        """Detect the type of a component from its name."""
        name_lower = name.lower()

        for component_type, patterns in COMPONENT_PATTERNS.items():
            for pattern in patterns:
                if pattern in name_lower:
                    return component_type

        return "other"

    def _detect_page_type(self, name: str) -> str:
        """Detect the type of a page from its name."""
        name_lower = name.lower()

        page_mappings = {
            "home": "home",
            "index": "home",
            "landing": "home",
            "about": "about",
            "contact": "contact",
            "pricing": "pricing",
            "blog": "blog",
            "posts": "blog",
            "news": "blog",
            "portfolio": "portfolio",
            "projects": "portfolio",
            "work": "portfolio",
            "shop": "shop",
            "products": "shop",
            "cart": "cart",
            "checkout": "checkout",
            "docs": "docs",
            "documentation": "docs",
            "guide": "docs",
            "login": "auth",
            "register": "auth",
            "signup": "auth",
            "dashboard": "dashboard",
            "admin": "admin",
            "profile": "profile",
            "settings": "settings",
        }

        for keyword, page_type in page_mappings.items():
            if keyword in name_lower:
                return page_type

        return "other"

    def _has_props(self, file_path: Path) -> bool:
        """Check if component accepts props."""
        try:
            content = file_path.read_text(encoding="utf-8", errors="ignore")
            return "props" in content or "Props" in content or "interface" in content
        except:
            return False

    def _has_styles(self, file_path: Path) -> bool:
        """Check if component has styles."""
        base = file_path.parent / file_path.stem

        style_files = [
            base.with_suffix(".css"),
            base.with_suffix(".scss"),
            base.with_suffix(".module.css"),
            base.with_suffix(".module.scss"),
            file_path.parent / "styles.css",
            file_path.parent / "styles.module.css",
        ]

        return any(f.exists() for f in style_files)

    def _generate_description(self, name: str, component_type: str) -> str:
        """Generate a description for a component."""
        descriptions = {
            "button": "Interactive button component with various states",
            "navbar": "Navigation header with links and branding",
            "hero": "Hero section for landing pages",
            "card": "Content card for displaying information",
            "form": "Form input component for user data",
            "footer": "Site footer with links and information",
            "modal": "Modal dialog for overlays",
            "sidebar": "Side navigation component",
            "slider": "Carousel/slider for content display",
            "grid": "Grid layout for organizing content",
            "pricing": "Pricing plan display component",
            "testimonial": "Customer testimonial display",
            "team": "Team member display component",
            "faq": "FAQ accordion component",
            "blog": "Blog post display component",
            "portfolio": "Portfolio project showcase",
            "ecommerce": "E-commerce product display",
            "dashboard": "Dashboard widget or card",
            "docs": "Documentation component",
            "other": "Reusable UI component"
        }
        return descriptions.get(component_type, descriptions["other"])

    def _generate_statistics(self) -> None:
        """Generate statistics about extracted components."""
        stats = {
            "total_components": sum(len(v) for v in self.registry["components"].values()),
            "total_pages": sum(len(v) for v in self.registry["pages"].values()),
            "total_sections": sum(len(v) for v in self.registry["sections"].values()),
            "by_type": {},
            "by_framework": {},
            "by_template": {}
        }

        # Count by type
        for comp_type, components in self.registry["components"].items():
            stats["by_type"][comp_type] = len(components)

        # Count by framework
        for comp_type, components in self.registry["components"].items():
            for comp in components:
                fw = comp.get("framework", "unknown")
                stats["by_framework"][fw] = stats["by_framework"].get(fw, 0) + 1

        # Count by template
        for comp_type, components in self.registry["components"].items():
            for comp in components:
                tmpl = comp.get("template", "unknown")
                stats["by_template"][tmpl] = stats["by_template"].get(tmpl, 0) + 1

        self.registry["statistics"] = stats

    def save_registry(self, output_path: Path) -> None:
        """Save the component registry to a JSON file."""
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(self.registry, f, indent=2, ensure_ascii=False)

        print(f"\nRegistry saved to: {output_path}")
        print(f"Statistics:")
        print(f"  - Total components: {self.registry['statistics'].get('total_components', 0)}")
        print(f"  - Total pages: {self.registry['statistics'].get('total_pages', 0)}")
        print(f"  - Total sections: {self.registry['statistics'].get('total_sections', 0)}")

    def print_summary(self) -> None:
        """Print a summary of extracted components."""
        print("\n" + "=" * 60)
        print("COMPONENT EXTRACTION SUMMARY")
        print("=" * 60)

        print("\nComponents by type:")
        for comp_type, components in sorted(self.registry["components"].items()):
            print(f"  {comp_type}: {len(components)} components")

        print("\nComponents by framework:")
        stats = self.registry.get("statistics", {})
        by_fw = stats.get("by_framework", {})
        for fw, count in sorted(by_fw.items(), key=lambda x: -x[1]):
            print(f"  {fw}: {count}")

        print("\nPages by type:")
        for page_type, pages in sorted(self.registry["pages"].items()):
            print(f"  {page_type}: {len(pages)} pages")

        print("\nPage sections by type:")
        for section_type, sections in sorted(self.registry["sections"].items()):
            print(f"  {section_type}: {len(sections)} sections")


def main():
    import sys

    templates_dir = Path("templates")
    components_dir = Path("components")
    output_path = Path("components-registry.json")

    if len(sys.argv) > 1:
        if sys.argv[1] == "templates":
            templates_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else templates_dir
        elif sys.argv[1] == "output":
            output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else output_path
        elif sys.argv[1] == "help":
            print("Usage: python extract_components.py [templates|output] [path]")
            print("  templates - Set templates directory (default: templates)")
            print("  output    - Set output file (default: components-registry.json)")
            return

    print("=" * 60)
    print("COMPONENT EXTRACTOR")
    print("=" * 60)

    extractor = ComponentExtractor(templates_dir, components_dir)
    extractor.scan_templates()
    extractor.print_summary()
    extractor.save_registry(output_path)

    print("\n" + "=" * 60)
    print("DONE - Registry generated for pick n' mix functionality")
    print("=" * 60)


if __name__ == "__main__":
    main()