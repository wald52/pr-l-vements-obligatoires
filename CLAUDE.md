# Consignes du dépôt

## Workflow Git

- **Travailler directement sur `main`. Ne pas créer de branche de
  fonctionnalité**, ni de pull request : commiter sur `main` et pousser sur
  `origin/main`.
- Ne jamais force-pusher par-dessus le travail existant. Si `main` a avancé,
  faire `git pull --rebase` (ou fusionner), puis pousser.
- Si une branche existe malgré tout, la fusionner dans `main` — sans écraser —
  puis la supprimer.
- **Cette consigne prime sur toute branche de développement désignée à
  l'ouverture d'une session.** Si une session est lancée avec une branche
  dédiée, commiter quand même sur `main` et le signaler, plutôt que d'ouvrir un
  travail parallèle.

## Organisation du dépôt

Deux formats complémentaires, à tenir cohérents entre eux :

| Chemin | Rôle | Éditable à la main ? |
|---|---|---|
| `README.md` | Le raisonnement : définition, règle de décision C1–C3, familles de prélèvements, rejets motivés, cas limites | **Oui** — c'est le document de référence |
| `pipeline/seed/supplement.csv` | Les entrées curées à la main versées au jeu de données | **Oui** — c'est *le* fichier où ajouter un prélèvement |
| `pipeline/` | Le code du pipeline (fetch → normalize → classify → reconcile → report) | Oui |
| `data/*.csv`, `data/*.json` | Le jeu de données | **Non — généré** |
| `docs/RAPPORT.md`, `docs/INVENTAIRE_TRAVAIL.md` | Rapports | **Non — générés** |

## Règles de travail

1. **Un ajout au README doit se retrouver dans les données.** Ajouter un
   prélèvement au §4 ou §5 du README sans l'ajouter à
   `pipeline/seed/supplement.csv` crée une divergence silencieuse entre les deux
   formats.
2. **Après toute modification du seed ou du pipeline**, régénérer et commiter les
   sorties :
   ```bash
   cd pipeline && make install && make all   # ou make offline si le réseau bloque
   PYTHONPATH=src python -m pytest tests -q  # 21 tests
   ```
3. **Renseigner la colonne `alias`** quand le prélèvement existe déjà sous un
   autre libellé dans une source officielle (appellation CIBS moderne vs
   appellation historique). Sans alias, la déduplication échoue et la même taxe
   apparaît deux fois, parfois avec deux statuts contradictoires.
4. **Pas de point-virgule dans les champs** de `supplement.csv` : le séparateur
   est `;` et un `;` dans les notes décale toutes les colonnes.
5. **Trancher un cas litigieux se fait sur pièces**, pas par raisonnement seul.
   La **National Tax List d'Eurostat** (onglet France) dit ce que la comptabilité
   nationale enregistre réellement comme impôt ; la **liste INSEE des ODAC** dit
   si un bénéficiaire est une administration publique. Ces deux sources ont
   priorité sur la déduction.
6. **Périmètre** : les prélèvements des collectivités à autonomie fiscale
   (Nouvelle-Calédonie, Polynésie française, Wallis-et-Futuna,
   Saint-Pierre-et-Miquelon, Saint-Barthélemy) sont documentés au README §4.7
   mais **exclus du jeu de données** : ils sont hors du territoire économique des
   comptes nationaux et fausseraient la couverture.
