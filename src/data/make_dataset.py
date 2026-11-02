"""Construit le jeu de données : charge le brut et fige le découpage train/val/test."""
import pandas as pd
from sklearn.model_selection import train_test_split

from src.config import ROOT, load_config


def make_dataset(cfg: dict | None = None) -> None:
    """Fusionne X/y et écrit train/val/test (stratifié) dans data/interim."""
    cfg = cfg or load_config()
    raw = ROOT / cfg["data"]["raw_dir"]
    interim = ROOT / cfg["data"]["interim_dir"]
    interim.mkdir(parents=True, exist_ok=True)

    X = pd.read_csv(raw / cfg["data"]["train_values"])
    y = pd.read_csv(raw / cfg["data"]["train_labels"])

    assert (X["id"] == y["id"]).all(), "Les id de X et y ne correspondent pas."
    df = X.merge(y, on="id")

    target = cfg["model"]["target"]
    seed = cfg["model"]["seed"]
    test_size = cfg["model"]["test_size"]
    val_size = cfg["model"]["val_size"]

    train, test = train_test_split(
        df, test_size=test_size, random_state=seed, stratify=df[target]
    )
    train, val = train_test_split(
        train, test_size=val_size, random_state=seed, stratify=train[target]
    )

    for name, sub in [("train", train), ("val", val), ("test", test)]:
        sub.to_csv(interim / f"{name}.csv", index=False)

    split = pd.concat(
        [train.assign(part="train"), val.assign(part="val"), test.assign(part="test")]
    )
    split[["id", "part"]].sort_values("id").to_csv(interim / "split.csv", index=False)

    print(f"Découpage écrit dans {interim} : {len(train)}/{len(val)}/{len(test)}")


if __name__ == "__main__":
    make_dataset()
