from __future__ import annotations

import base64
import io
from typing import Any, Dict, List

import matplotlib.pyplot as plt
from flask import Flask, jsonify, request

from src.model_service import (
    FEATURE_COLUMNS,
    find_default_dataset,
    load_dataset,
    load_model,
    predict_label,
    predict_proba,
    train_and_save,
)

app = Flask(__name__)

@app.get("/health")
def health() -> Any:
    return {"status": "ok"}

def _features_list_to_row(features: List[float]) -> Dict[str, float]:
    """Allow the payload: {"features": [...]}.

    If the list is shorter than required, pad zeros; if longer, truncate.
    Order is assumed to be: Time, V1..V28, Amount.
    """
    required = len(FEATURE_COLUMNS)
    vals = list(features[:required]) + [0.0] * max(0, required - len(features))
    return {col: float(vals[i]) for i, col in enumerate(FEATURE_COLUMNS)}

@app.post("/predict")
def predict() -> Any:
    try:
        payload: Dict[str, Any] = request.get_json(force=True)  # type: ignore[assignment]
        rows: List[Dict[str, float]] = payload.get("rows", [])
        features: List[List[float]] | None = payload.get("features")  # optional alternative
        threshold: float = float(payload.get("threshold", 0.5))

        if not rows and features:
            rows = [_features_list_to_row(feat) for feat in features]
        if not rows:
            return jsonify({"error": "Provide 'rows' (list of feature dicts) or 'features' (list of float lists)."}), 400

        model, feature_columns = load_model()
        probs = predict_proba(model, rows, feature_columns)
        labels = [int(p >= threshold) for p in probs]
        return jsonify({"probs": probs, "labels": labels})
    except Exception as err:  # noqa: BLE001
        return jsonify({"error": str(err)}), 400

@app.get("/predict/<float:amount>")
def predict_one(amount: float) -> Any:
    """Path-param demo: predict using only Amount; other features set to 0."""
    try:
        model, feature_columns = load_model()
        base: Dict[str, float] = {c: 0.0 for c in feature_columns}
        if "Amount" in base:
            base["Amount"] = float(amount)
        rows = [base]
        probs = predict_proba(model, rows, feature_columns)
        return jsonify({"probs": probs, "labels": [int(probs[0] >= 0.5)]})
    except Exception as err:  # noqa: BLE001
        return jsonify({"error": str(err)}), 400

@app.get("/predict/<float:amount>/<float:time>")
def predict_two(amount: float, time: float) -> Any:
    """Path-param demo: set Amount and Time; other features set to 0."""
    try:
        model, feature_columns = load_model()
        base: Dict[str, float] = {c: 0.0 for c in feature_columns}
        if "Amount" in base:
            base["Amount"] = float(amount)
        if "Time" in base:
            base["Time"] = float(time)
        probs = predict_proba(model, [base], feature_columns)
        return jsonify({"probs": probs, "labels": [int(probs[0] >= 0.5)]})
    except Exception as err:  # noqa: BLE001
        return jsonify({"error": str(err)}), 400

@app.get("/plot")
def plot() -> Any:
    """Return a tiny demo chart as inline PNG."""
    try:
        fig, ax = plt.subplots(figsize=(3, 2))
        ax.plot([0, 0.5, 1.0], [0, 0.6, 1.0], marker="o")
        ax.set_xlabel("Recall")
        ax.set_ylabel("Precision")
        ax.set_title("PR sketch")
        buf = io.BytesIO()
        fig.tight_layout()
        fig.savefig(buf, format="png", dpi=150)
        buf.seek(0)
        img_b64 = base64.b64encode(buf.read()).decode("utf-8")
        return f'<img src="data:image/png;base64,{img_b64}"/>'
    except Exception as err:  # noqa: BLE001
        return jsonify({"error": str(err)}), 400

@app.post("/run_full_analysis")
def run_full_analysis() -> Any:
    try:
        result = train_and_save(find_default_dataset())
        df = load_dataset(find_default_dataset())
        return jsonify({
            "message": "analysis complete",
            "rows": int(df.shape[0]),
            "cols": int(df.shape[1]),
            **result,
        })
    except Exception as err:  # noqa: BLE001
        return jsonify({"error": str(err)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
