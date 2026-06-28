"""Interface en ligne de commande du pipeline.

Usage :
    po-pipeline fetch [--offline]
    po-pipeline normalize
    po-pipeline classify
    po-pipeline reconcile
    po-pipeline report
    po-pipeline validate
    po-pipeline all [--offline]
"""

from __future__ import annotations

import argparse
import sys


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="po-pipeline",
                                     description="Inventaire des prélèvements obligatoires en France")
    sub = parser.add_subparsers(dest="stage", required=True)

    p_fetch = sub.add_parser("fetch", help="télécharger les sources")
    p_fetch.add_argument("--offline", action="store_true",
                         help="ne pas appeler le réseau, utiliser le cache")
    sub.add_parser("normalize", help="parser les sources -> interim")
    sub.add_parser("classify", help="appliquer la règle de décision")
    sub.add_parser("reconcile", help="fusionner + mesurer la couverture")
    sub.add_parser("report", help="générer docs/RAPPORT.md")
    sub.add_parser("validate", help="valider le jeu de données (schéma JSON)")
    p_all = sub.add_parser("all", help="exécuter tous les étages")
    p_all.add_argument("--offline", action="store_true")

    args = parser.parse_args(argv)

    if args.stage == "fetch":
        from .fetch import fetch
        fetch(offline=args.offline)
    elif args.stage == "normalize":
        from .normalize import normalize
        normalize()
    elif args.stage == "classify":
        from .classify import classify
        # classify lit interim et renvoie les enregistrements classés ;
        # ils sont consommés par reconcile, pas re-persistés ici.
        recs = classify()
        print(f"[classify] {len(recs)} enregistrements classés")
    elif args.stage == "reconcile":
        from .reconcile import reconcile
        reconcile()
    elif args.stage == "report":
        from .report import report
        report()
    elif args.stage == "validate":
        from .validate import validate_dataset
        validate_dataset()
    elif args.stage == "all":
        from .fetch import fetch
        from .normalize import normalize
        from .reconcile import reconcile
        from .report import report
        from .validate import validate_dataset
        fetch(offline=args.offline)
        normalize()
        reconcile()  # appelle classify() en interne
        validate_dataset()
        report()

    return 0


if __name__ == "__main__":
    sys.exit(main())
