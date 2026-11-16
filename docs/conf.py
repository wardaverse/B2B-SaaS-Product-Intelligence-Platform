"""Sphinx configuration for B2B SaaS Product Intelligence Platform."""

project = "B2B SaaS Product Intelligence Platform"
author = "Warda Shafiq"
copyright = "2026, Warda Shafiq"

extensions = [
    "myst_parser",
    "sphinx_copybutton",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

templates_path = ["_templates"]
exclude_patterns = ["_build"]

html_theme = "furo"
html_title = "SaaS Growth Analytics — Docs"
