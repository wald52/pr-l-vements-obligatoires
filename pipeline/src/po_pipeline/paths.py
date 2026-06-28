"""Chemins du projet, résolus relativement à ce fichier.

Structure :
    pipeline/
      config/                 <- CONFIG_DIR
      src/po_pipeline/        <- ce paquet
      data/raw|interim|processed
    data/                     <- DATASET_DIR (sorties finales versionnées)
    docs/                     <- DOCS_DIR
"""

from __future__ import annotations

from pathlib import Path

# .../pipeline/src/po_pipeline/paths.py -> remonter à pipeline/, puis racine repo
PKG_DIR = Path(__file__).resolve().parent
PIPELINE_DIR = PKG_DIR.parent.parent
REPO_ROOT = PIPELINE_DIR.parent

CONFIG_DIR = PIPELINE_DIR / "config"
DATA_DIR = PIPELINE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
PROCESSED_DIR = DATA_DIR / "processed"

# Sorties finales versionnées à la racine du dépôt.
DATASET_DIR = REPO_ROOT / "data"
DOCS_DIR = REPO_ROOT / "docs"

SOURCES_CONFIG = CONFIG_DIR / "sources.yaml"
RULES_CONFIG = CONFIG_DIR / "decision_rules.yaml"


def ensure_dirs() -> None:
    """Crée les répertoires de travail s'ils n'existent pas."""
    for d in (RAW_DIR, INTERIM_DIR, PROCESSED_DIR, DATASET_DIR, DOCS_DIR):
        d.mkdir(parents=True, exist_ok=True)
