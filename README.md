# POAI Project

This repository contains a small machine learning project for a course (POAI) that explores models and data related to mental health and music genre classification.

## Repository contents

- `Mental Health Dataset.csv` - CSV dataset related to mental health (used by experiments).
- `music_genre.csv` - CSV dataset for music genre classification experiments.
- `health_tester.joblib` - A saved model or artifact (joblib format).
- `test.py` - A small script used to test or run the model.
- `desc.ipynb` - Description and exploratory notebook.
- `dt.dot`, `modelvis.dot` - Graphviz DOT files (model visualizations).
- `requirements.txt` - Python dependencies used by the project.

## Project summary

The project explores preprocessing, modelling, and evaluation for classification tasks. It includes notebooks and scripts to reproduce training and inference steps, plus visualizations exported as DOT files.

## Setup

1. Create and activate a Python virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. (Optional) If working with notebooks, install Jupyter:

```powershell
pip install jupyterlab
jupyter lab
```

## How to run

- To open the exploratory notebook, run Jupyter Lab or Notebook and open `desc.ipynb`.
- To run the quick test script:

```powershell
python test.py
```

- To load the saved model artifact from `health_tester.joblib` (example):

```python
from joblib import load
model = load('health_tester.joblib')
# then use model.predict(X)
```

## Notes and next steps

- Add descriptions of the datasets and preprocessing steps in `desc.ipynb` or a dedicated `data/README.md`.
- Provide clear training scripts that accept a `--train` or `--predict` flag.
- Add a license and contribution guidelines if this repo will be shared.

## Contact

If you need help reproducing results, open an issue with the commands you ran and the error output.
