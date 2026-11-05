# Données

- **Source** : Pump it Up: Data Mining the Water Table, DrivenData (compétition 7). Données Taarifa et ministère de l'Eau de Tanzanie.
- **Lien** : https://www.drivendata.org/competitions/7/pump-it-up-data-mining-the-water-table/ (fichiers fournis sur clé)
- **Version utilisée** : fichiers de la clé, empreintes MD5 :

| Copier sous | Fichier d'origine (clé) | MD5 |
|---|---|---|
| `raw/train_values.csv` | `4910797b-ee55-40a7-8668-10efd5c1b960.csv` | `7f81583401fcd17fd588208179f22441` |
| `raw/train_labels.csv` | `0bf8bc6e-30d0-4c50-956a-603fc693d966.csv` | `743edfcd5364347eae58377a8788d54d` |

Ne pas utiliser `702ddfc5-…csv` (test officiel sans étiquettes) ni `SubmissionFormat.csv`.

## Contenu du dossier

- `raw/` : les deux CSV ci-dessus, non versionnés.
- `livrable2/split.csv` : le découpage figé (`id`, `part`), versionné.
- `livrable2/train.csv`, `val.csv`, `test.csv` : produits par le notebook 02, non versionnés.
- `exemple.json` : un point d'eau de la validation, pour tester `src/predict.py`.
