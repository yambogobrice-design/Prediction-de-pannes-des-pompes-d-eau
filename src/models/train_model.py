"""Entraîne et évalue le modèle."""
import argparse

from src.config import ROOT, load_config


def train_model() -> None:
    cfg = load_config()
    interim = ROOT / cfg["data"]["interim_dir"]
    print(f"Chargement des données depuis {interim}")
    # TODO: charger interim/train.csv et interim/val.csv, construire les
    # features (src.features.build_features) puis entraîner/évaluer le modèle.
    raise NotImplementedError("Pipeline d'entraînement à implémenter.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Entraîne le modèle")
    parser.parse_args()
    train_model()
