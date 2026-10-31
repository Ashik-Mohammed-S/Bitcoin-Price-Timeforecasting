# Recovered data and execution

The public copies below match the filenames and schemas used by this notebook.
Original lost-file byte identity cannot be proved. URLs are pinned to source commits,
and SHA-256 checksums in dataset-sources.json prevent silent source changes.
Data is downloaded locally rather than added as new dataset blobs in this PR.

| File | Rows / tokens | Source |
| --- | --- | --- |
| `BTC_USD_2013-10-01_2021-05-18-CoinDesk.csv` | 2787 | [Pinned source](https://raw.githubusercontent.com/mrdbourke/tensorflow-deep-learning/bd065b806249f7b1155e5b1fabd130c5cfc9d184/extras/BTC_USD_2013-10-01_2021-05-18-CoinDesk.csv) |

Source repository license metadata: MIT License

```sh
python -m pip install -r requirements.txt
python scripts/fetch_data.py
python scripts/run_notebook.py --mode quick
python -m jupyterlab
```

Install the spaCy English model first where used: `python -m spacy download en_core_web_sm`.
The notebook also restores missing reference files automatically when run from the repository root.
Set DATA_DIR to use another directory containing these same reference files.
Existing files with a different checksum are left untouched and reported as mismatches.

Quick mode trains on the recovered price history with two epochs, two N-BEATS stacks, and a smaller ensemble. Full experiments are available with `--mode full`, or set RUN_MODE=full before
launching the notebook. Quick results demonstrate execution; they do not reproduce
the historical trained-model quality. The runner writes results/execution-report.json.

