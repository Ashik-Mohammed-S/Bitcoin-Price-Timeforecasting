# Current stable Python environment

Dependencies are pinned to stable releases checked against PyPI on 2026-11-01.
Run from this repository's root with Python 3.13.18 (see `.python-version`):

```sh
python -m venv .venv
# Activate .venv using your shell's activation command.
python -m pip install -r requirements.txt
python scripts/validate_notebooks.py
python scripts/smoke_test.py
python -m jupyterlab
```

Open the notebook and run cells in order. The kernel must use `.venv`.
Python 3.13.18 is selected for the compiled dependency stack. Python 3.12.16
was also used for baseline compatibility checks. Python 3.15.2 requires source
builds for dependencies without published wheels (including PyYAML, wordcloud,
and python-crfsuite where used). The Windows validation environment has no C++
build tools, so this change uses the newest runtime with available dependency wheels.

## Data and validation

Put these original input files under `dataset/`, or set the `DATA_DIR` environment variable: `BTC_USD_2013-10-01_2021-05-18-CoinDesk.csv`.

The validation script checks notebook structure, compiles all transformed code cells,
and imports declared dependencies. It does not execute training or claim to
reproduce results without the original datasets. Saved code-cell outputs were cleared to avoid presenting results from the old
environment as current. Rerun to generate results.

Model diagrams also require the Graphviz system executable (`dot`) on PATH.

Retrain models in notebook order to create `.keras` checkpoints. The committed legacy SavedModel directories are historical artifacts and cannot be loaded with Keras 3 `load_model`. Model 6 also requires retraining because its checkpoint is not committed. Training the N-BEATS and ensemble sections can take substantial time.


TensorFlow 2.21.0 currently publishes wheels through Python 3.13. Python 3.14/3.15 cannot install this release from wheels.

Version sources: [PyPI](https://pypi.org/), [Python releases](https://www.python.org/downloads/), [checkout releases](https://github.com/actions/checkout/releases), and [setup-python releases](https://github.com/actions/setup-python/releases).
