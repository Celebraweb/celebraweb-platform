"""
CW PMO
Paths

Rutas oficiales del proyecto.
"""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]

DOCS = ROOT / "docs"

GOVERNANCE = DOCS / "00-Governance"

ENGINEERING = DOCS / "06-Engineering"

SPRINTS = DOCS / "09-Sprints"