"""Chargement des fichiers de configuration YAML."""

from __future__ import annotations

from typing import Any

import yaml

from .paths import RULES_CONFIG, SOURCES_CONFIG


def load_sources() -> dict[str, Any]:
    with open(SOURCES_CONFIG, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_rules() -> dict[str, Any]:
    with open(RULES_CONFIG, encoding="utf-8") as f:
        return yaml.safe_load(f)


def enabled_sources(cfg: dict[str, Any] | None = None) -> list[dict[str, Any]]:
    cfg = cfg or load_sources()
    return [s for s in cfg.get("sources", []) if s.get("enabled")]
