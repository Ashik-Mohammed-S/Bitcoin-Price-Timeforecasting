# Bitcoin Forecasting: A Baseline-First Study

[![Validation](https://github.com/Ashik-Mohammed-S/Bitcoin-Price-Timeforecasting/actions/workflows/validate.yml/badge.svg)](https://github.com/Ashik-Mohammed-S/Bitcoin-Price-Timeforecasting/actions/workflows/validate.yml)

Evaluate whether lagged-price regression improves on carrying the last observed closing price forward.

Independent public portfolio work; historical educational notebooks remain under `historical/`. The current implementation and results described here take precedence over historical in-sample numbers.

## Data and approach

2,787 daily historical closing observations; 2,205 training targets and 552 final test targets after 30-day lag construction.

Reserve the last 20% chronologically. Use expanding-window training CV and train-only scaling. Select the Ridge candidate or persistence before looking at final test performance.

## Current full-data result

| Measure | Current analysis | Baseline where applicable |
| --- | --- | --- |
| Selected persistence MAE | 571.06 | 571.06 |
| Selected persistence RMSE | 1,075.74 | 1,075.74 |
| Ridge candidate MAE | 581.20 | 571.06 |

Results are specific to the documented dataset and split. See generated `results/analysis.json` after execution for full metrics and assumptions.

## Run locally

Use the Python version in `.python-version`, then:

```sh
python -m pip install -r requirements.txt
python scripts/fetch_data.py
python scripts/run_notebook.py --mode full
```

Reference data is committed under `dataset/`, directly or as reconstructable compressed parts. The downloader verifies checksums and restores stored data offline. See [DATA.md](DATA.md) and [dataset-sources.json](dataset-sources.json) for provenance and upstream terms. Package installation and the spaCy model, where needed, require network access on a fresh machine.

## Review the implementation

Inspect training-period selection rather than choosing a winner after viewing the test set. Start with [scripts/analysis.py](scripts/analysis.py), then the root notebook. The workflow validates dependencies, smoke checks and full-data notebook execution with dataset downloads disabled.

## Limitations

Persistence wins and is the selected strategy. High price-level R² does not establish forecasting skill. This historical one-step experiment is not an investment recommendation or live trading model.

[Method notes](ANALYSIS.md) · [All portfolio projects](https://github.com/Ashik-Mohammed-S/Ashik-Mohammed-S/blob/main/PORTFOLIO.md)
