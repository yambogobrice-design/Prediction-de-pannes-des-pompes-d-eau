# Prediction de pannes des pompes d'eau

Prédiction de l'état fonctionnel des points d'eau en Tanzanie à partir du
dataset **« Pump it Up: Data Mining the Water Table »** (compétition
[DrivenData](https://www.drivendata.org/competitions/7/pump-it-up-data-mining-the-water-table/)).

Objectif : classer chaque point d'eau parmi trois classes —
`functional`, `functional needs repair`, `non functional`.

## Structure du projet

```
├── README.md
├── requirements.txt           # dépendances runtime
├── requirements-dev.txt       # + outils de dev (pytest, jupyter)
├── Makefile                   # raccourcis : make install / test / train
├── config/
│   └── config.yaml            # chemins & paramètres centralisés
├── data/
│   ├── raw/                   # données brutes (non modifiées, hors Git)
│   ├── interim/               # données nettoyées / fusionnées
│   ├── processed/             # matrices finales d'entraînement
│   ├── splits/                # découpage figé (généré)
│   └── livrable2/             # sorties du livrable 2 (généré)
├── notebooks/                 # exploration & expérimentation
│   ├── 01_exploration_et_decoupage.ipynb
│   ├── 02_livrable2_donnees.ipynb
│   ├── 03_livrable3_baseline.ipynb
│   └── archive/               # versions obsolètes
├── src/                       # code réutilisable et testable
│   ├── data/                  #   1. chargement / préparation
│   ├── features/              #   2. feature engineering
│   ├── models/                #   3. entraînement / prédiction
│   └── visualization/         #   4. visualisations
├── tests/                     # tests unitaires
├── outputs/                   # modèles, soumissions, métriques (généré)
├── livrables/                 # rapports, slides, documents
├── app/
│   ├── backend/
│   └── frontend/
└── .github/workflows/         # intégration continue
```

## Installation

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
```

## Données

Les fichiers bruts (CSV) ne sont **pas versionnés** dans Git. Déposer les
fichiers dans `data/raw/` en respectant les noms du tableau ci-dessous
(voir `data/raw/README.md`) :

| Nom attendu            | Contenu                              |
|------------------------|--------------------------------------|
| `train_values.csv`     | Variables d'entraînement (X)         |
| `train_labels.csv`     | Étiquettes d'entraînement (y)        |
| `test_values.csv`      | Variables de test (X_test)           |
| `submission_format.csv`| Format de soumission attendu         |

## Usage

```powershell
# Entraîner / prédire / tester
make train
make predict
make test

# Ou sans make :
python -m src.models.train_model
pytest tests
```

## Pipeline

1. `src.data.make_dataset` — charge `data/raw`, fige le découpage train/val/test.
2. `src.features.build_features` — nettoie et construit les features.
3. `src.models.train_model` — entraîne et évalue les modèles.
4. `src.models.predict_model` — produit `outputs/submission.csv`.
