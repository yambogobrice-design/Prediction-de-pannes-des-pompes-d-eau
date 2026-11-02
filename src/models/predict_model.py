"""Produit les prédictions sur le test et génère outputs/submission.csv."""
import argparse

from src.config import ROOT, load_config


def predict_model() -> None:
    cfg = load_config()
    outputs = ROOT / "outputs"
    outputs.mkdir(parents=True, exist_ok=True)
    print(f"Sorties écrites dans {outputs}")
    # TODO: charger le modèle entraîné, prédire sur test_values.csv et écrire
    # outputs/submission.csv au format attendu (id, status_group).
    raise NotImplementedError("Pipeline de prédiction à implémenter.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Génère la soumission")
    parser.parse_args()
    predict_model()
