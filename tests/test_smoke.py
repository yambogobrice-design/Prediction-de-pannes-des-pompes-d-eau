"""Tests de fumée : vérifient la configuration et la présence des données."""
import pytest

from src.config import ROOT, load_config

RAW_NAMES = [
    "train_values.csv",
    "train_labels.csv",
    "test_values.csv",
    "submission_format.csv",
]


def test_config_loads():
    cfg = load_config()
    assert "data" in cfg
    assert "model" in cfg
    assert cfg["model"]["target"] == "status_group"


def test_config_paths_exist():
    cfg = load_config()
    assert (ROOT / cfg["data"]["raw_dir"]).exists()


@pytest.mark.skipif(
    not all((ROOT / "data" / "raw" / name).exists() for name in RAW_NAMES),
    reason="données brutes absentes (non versionnées dans Git)",
)
def test_raw_data_present():
    for name in RAW_NAMES:
        assert (ROOT / "data" / "raw" / name).exists(), f"{name} manquant"
