# Données brutes (`data/raw/`)

Les CSV bruts ne sont **pas versionnés** dans Git (voir `.gitignore`).
Ils proviennent de la compétition DrivenData
« Pump it Up: Data Mining the Water Table ».

## Correspondance des fichiers

| Nom actuel                        | UUID d'origine                        | Rôle                          |
|-----------------------------------|---------------------------------------|-------------------------------|
| `train_values.csv`                | `4910797b-ee55-40a7-8668-10efd5c1b960` | Variables d'entraînement (X)  |
| `train_labels.csv`                | `0bf8bc6e-30d0-4c50-956a-603fc693d966` | Étiquettes (y) : `status_group` |
| `test_values.csv`                 | `702ddfc5-68cd-4d1d-a0de-f5f566f76d91` | Variables de test (X_test)    |
| `submission_format.csv`           | `SubmissionFormat.csv`                | Format de soumission attendu  |

## Règle d'or

Ne **jamais** modifier ces fichiers. Toute transformation doit écrire dans
`data/interim/` ou `data/processed/` afin de garantir la reproductibilité.
