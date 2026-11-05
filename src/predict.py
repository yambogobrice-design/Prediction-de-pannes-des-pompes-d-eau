"""Prédit l'état d'un point d'eau à partir d'un fichier JSON décrivant ses 10 variables.

Exemple (depuis la racine du projet) :
    python src/predict.py --exemple data/exemple.json

Le modèle utilisé est l'arbre enregistré par le notebook 03 (partie 6).
"""
import argparse
import json
import sys
from pathlib import Path

import joblib
import pandas as pd

RACINE = Path(__file__).resolve().parent.parent
MODELE = RACINE / "outputs" / "livrable3" / "arbre_10var.joblib"

# Les classes du modèle, traduites pour l'utilisateur
FRANCAIS = {
    "functional": "fonctionnel",
    "functional needs repair": "fonctionnel mais à réparer",
    "non functional": "hors service",
}


def lire_exemple(chemin, attendues):
    """Lit le fichier JSON et vérifie qu'il contient bien les variables du modèle."""
    with open(chemin, encoding="utf-8") as f:
        exemple = json.load(f)
    manquantes = [v for v in attendues if v not in exemple]
    if manquantes:
        sys.exit(f"Erreur : variables manquantes dans {chemin} : {', '.join(manquantes)}")
    return pd.DataFrame([exemple])[attendues]   # une ligne, colonnes dans l'ordre attendu


def modalites_inconnues(modele, exemple):
    """Liste les valeurs jamais vues à l'entraînement : le modèle les ignore sans rien dire."""
    encodeur = modele[0].named_transformers_["texte"]
    inconnues = []
    for colonne, connues in zip(encodeur.feature_names_in_, encodeur.categories_):
        valeur = exemple.loc[0, colonne]
        if valeur not in connues:
            inconnues.append(f"{colonne} = {valeur}")
    return inconnues


def main():
    p = argparse.ArgumentParser(description="Prédit l'état d'un point d'eau.")
    p.add_argument("--exemple", required=True, help="fichier JSON avec les 10 variables du point d'eau")
    a = p.parse_args()

    if not Path(a.exemple).exists():
        sys.exit(f"Erreur : fichier introuvable : {a.exemple}")
    if not MODELE.exists():
        sys.exit(f"Erreur : modèle introuvable : {MODELE}. Exécutez d'abord le notebook 03.")

    modele = joblib.load(MODELE)
    exemple = lire_exemple(a.exemple, list(modele.feature_names_in_))

    # Une valeur inconnue fausserait la réponse sans le dire : on prévient l'utilisateur
    for texte in modalites_inconnues(modele, exemple):
        print(f"Attention, valeur jamais vue à l'entraînement : {texte}")

    probas = pd.Series(modele.predict_proba(exemple)[0], index=modele.classes_)
    etat = probas.idxmax()

    print(f"État prédit : {FRANCAIS[etat]} (probabilité {probas[etat]:.3f})")
    print("Détail :")
    for classe, proba in probas.sort_values(ascending=False).items():
        print(f"  {FRANCAIS[classe]} : {proba:.3f}")


if __name__ == "__main__":
    main()
