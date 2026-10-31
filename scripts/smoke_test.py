"""Check notebook helpers and Keras 3 checkpoint round-trips with tiny synthetic models."""
import ast
import json
import os
import tempfile
from pathlib import Path
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
from IPython.core.inputtransformer2 import TransformerManager

root = Path(__file__).resolve().parents[1]
nb = json.loads((root / "Main.ipynb").read_text(encoding="utf-8"))
namespace = {"tf": tf, "os": os, "layers": layers, "np": np, "WINDOW_SIZE": 7, "HORIZON": 1}
for cell in nb["cells"]:
    if cell["cell_type"] != "code":
        continue
    tree = ast.parse(TransformerManager().transform_cell("".join(cell["source"])))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == "model_4" for target in node.targets) and isinstance(node.value, ast.Call) and ast.unparse(node.value.func) == "tf.keras.Sequential":
            exec(compile(ast.Module(body=[node], type_ignores=[]), "notebook Conv1D", "exec"), namespace)
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name in {
            "NBeatsBlock", "create_model_checkpoint", "mean_absolute_scaled_error", "evaluate_preds", "get_labelled_window", "make_windows"
        }:
            exec(compile(ast.Module(body=[node], type_ignores=[]), "notebook helper", "exec"), namespace)
            if node.name == "evaluate_preds":
                result = namespace[node.name]([1., 2., 3.], [1., 2., 4.])
                assert np.isclose(result["mae"], 1 / 3)

windows, labels = namespace["make_windows"](np.arange(40), window_size=30, horizon=7)
assert windows.shape == (4, 30)
assert labels.shape == (4, 7)
np.testing.assert_array_equal(labels[0], np.arange(30, 37))
block = namespace["NBeatsBlock"]
x = np.arange(28, dtype=np.float32).reshape(4, 7) / 28
y = np.ones((4, 1), dtype=np.float32)
inputs = layers.Input(shape=(7,))
_, forecast = block(input_size=7, theta_size=8, horizon=1, n_neurons=8, n_layers=2)(inputs)
models = [
    tf.keras.Model(inputs, forecast),
    namespace["model_4"],
    tf.keras.Sequential([layers.Input(shape=(7,)), layers.Reshape((1, 7)), layers.LSTM(4), layers.Dense(1)]),
]
with tempfile.TemporaryDirectory() as directory:
    callback = namespace["create_model_checkpoint"]("smoke", directory)
    assert callback.filepath.endswith(".keras")
    for index, model in enumerate(models):
        model.compile(optimizer="adam", loss="mae")
        assert np.isfinite(model.train_on_batch(x, y))
        before = model(x).numpy()
        assert before.shape == (len(x), 1), before.shape
        target = Path(directory) / f"model{index}.keras"
        model.save(target)
        restored = tf.keras.models.load_model(target)
        np.testing.assert_allclose(before, restored(x).numpy(), rtol=1e-5, atol=1e-5)
print("Keras helper, metric, training, and checkpoint smoke checks passed.")

print("Scientific stack smoke checks passed.")
