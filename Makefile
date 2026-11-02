.PHONY: help install train test predict clean

PYTHON ?= python
PYTEST ?= pytest

help: ## Affiche l'aide
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-12s\033[0m %s\n", $$1, $$2}'

install: ## Installe les dépendances de dev
	pip install -r requirements-dev.txt

train: ## Lance l'entraînement (src/models/train_model.py)
	$(PYTHON) -m src.models.train_model

predict: ## Lance la prédiction (src/models/predict_model.py)
	$(PYTHON) -m src.models.predict_model

test: ## Lance les tests
	$(PYTEST) tests

clean: ## Supprime les caches Python
	python -c "import pathlib, shutil; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('__pycache__')]"
