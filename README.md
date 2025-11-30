# Suggestions

New Recommendations study project

Status: WIP (work in progress) • Language: Python

## Overview

Suggestions is a small study project focused on recommendation systems. Its purpose is to serve as a playground for experimenting with recommendation algorithms, dataset preprocessing, evaluation metrics, and simple prototypes for research or learning.

This repository contains code, experiments and utilities to build, train, evaluate, and analyse recommender models. The project is intentionally lightweight and designed to be extended.

## Goals

- Provide a minimal, clear structure for recommendation system experiments
- Include utilities for data ingestion, preprocessing, and evaluation
- Offer example scripts to run training and evaluation cycles
- Serve as a starting point for research or learning about recommender algorithms

## Features (planned / suggested)

- Data loaders for common dataset formats (CSV, JSON)
- Preprocessing utilities (filtering, train/test splitting)
- Baseline recommenders (popularity, item-based, user-based)
- Evaluation metrics (Precision@K, Recall@K, MAP, NDCG)
- Experiment tracking with basic logs and reproducible seeds

## Tech stack

- Python 3.8+
- Common libraries (pandas, numpy, scikit-learn)
- Optional libraries for matrix factorization or deep learning: implicit, lightfm, PyTorch, TensorFlow

## Quickstart

1. Clone the repository:
```bash
git clone https://github.com/Gianfy/Suggestions.git
cd Suggestions
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```
If `requirements.txt` is not present, install commonly used packages:
```bash
pip install pandas numpy scikit-learn
```

4. Run an example (adjust path and module names to match repository layout):
```bash
python -m src.main   # or: python run_experiment.py
```

Note: Replace the example commands above with the actual entrypoint(s) in this repository (e.g., scripts in `src/` or `scripts/`).

## Usage ideas

- Prepare a dataset as CSV with columns: user_id, item_id, rating, timestamp (or adapt loaders).
- Use provided preprocessing utilities to filter users/items and create train/test splits.
- Run baseline recommenders to obtain reference metrics.
- Implement new algorithms and compare with baselines.

## Configuration

Use environment variables or a `config.yml`/`config.json` file to centralize parameters such as:
- dataset path
- random seed
- model hyperparameters
- output/log paths

Example config snippet (YAML):
```yaml
dataset:
  path: data/ratings.csv
training:
  seed: 42
  num_epochs: 20
evaluation:
  top_k: 10
```

## Development

- Formatting: black
- Linting: flake8 / pylint
- Tests: pytest

Example commands:
```bash
black .
flake8 .
pytest -q
```

## Contributing

Contributions are welcome. Suggested workflow:
1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Open a Pull Request describing your changes

Please open issues for feature requests or bug reports and reference them in PRs.

## Roadmap / Next steps

- Add concrete example datasets and scripts
- Provide ready-made baseline implementations and evaluation notebooks
- Introduce experiment tracking (e.g., MLflow or simple CSV logs)
- Add CI for tests and linting

## License

No license specified yet. If you want to open-source the project, consider adding an OSI-approved license such as MIT, Apache-2.0, or GPL-3.0. Example: add a `LICENSE` file containing the chosen license text.

## Contact

Repository owner: Gianfy — https://github.com/Gianfy
