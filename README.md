# Sujet 1 : quels points d'eau sont en panne ?

IIAA752, Projet IA. Classification à 3 classes (fonctionnel, à réparer, hors service) sur les données *Pump it Up* (Tanzanie).

## Démarrage rapide

Python 3.11 ou plus récent. Sous Windows, depuis la racine du projet :

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python src/predict.py --exemple data/exemple.json
```

Réponse attendue : hors service, probabilité 0,998.

Le modèle est dans le dépôt : ni les données ni les notebooks ne sont nécessaires pour cette commande.

## Données

Les données brutes ne sont pas dans Git. Voir `data/README.md` : il faut copier les deux CSV dans `data/raw/`.

## Refaire l'entraînement

Il faut les données ci-dessus. Ouvrir chaque notebook avec le Python du `.venv`, puis exécuter toutes les cellules, dans cet ordre :

1. `notebooks/02_livrable2_donnees.ipynb` : nettoyage et découpage dans `data/livrable2/`.
2. `notebooks/03_livrable3_baseline.ipynb` : baselines, journal `experiments.csv`, modèles dans `outputs/livrable3/`, analyse de 10 erreurs.

Le notebook 03 réécrit le modèle dans `outputs/livrable3/`.

## Résultats attendus (validation)

| Modèle | Exactitude | Rappel « à réparer » | F1 macro |
|---|---|---|---|
| majoritaire | 0,543 | 0,000 | 0,235 |
| logistique_10var | 0,732 | 0,037 | 0,519 |
| arbre_10var | 0,736 | 0,088 | 0,545 |

## Arborescence

```
data/        README (lien, version), exemple.json, livrable2/split.csv (découpage figé)
notebooks/   exploration et baselines
src/         predict.py (prédiction sur un exemple)
app/         prototype (à venir)
docs/        note de cadrage, fiche de données
outputs/     livrable3/arbre_10var.joblib (le modèle de predict.py) ; le reste n'est pas versionné
experiments.csv   journal : une ligne par essai
```

## Règles

- Graine 42.
- Le jeu de test n'est utilisé qu'une seule fois, en S5.
