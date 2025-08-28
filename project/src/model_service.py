"""
Model training, persistence, loading, and prediction utilities for the fraud project.

Functions here are designed for productization (Stage 13):
- train_model: fit a baseline classifier
- evaluate_model: compute PR AUC, F1, precision, recall
- save_model / load_model: persist model artifacts
- predict_proba / predict_label: inference helpers with validation and errors

Artifacts and data paths are resolved relative to the project root.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (average_precision_score, f1_score,
                             precision_score, recall_score)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


# ---------- Paths ----------

def get_project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def get_model_dir() -> Path:
    d = get_project_root() / "model"
    d.mkdir(parents=True, exist_ok=True)
    return d


def get_reports_dir() -> Path:
    d = get_project_root() / "reports"
    d.mkdir(parents=True, exist_ok=True)
    return d


def get_default_model_path() -> Path:
    return get_model_dir() / "model.pkl"


def find_default_dataset() -> Optional[Path]:
    """Find a cleaned dataset under project/data/processed.

    Prefers files containing "cleaned"; falls back to any large CSV.
    """
    processed = get_project_root() / "data" / "processed"
    if not processed.exists():
        return None
    cleaned = sorted(processed.glob("*cleaned*.csv"))
    if cleaned:
        return cleaned[0]
    csvs = sorted(processed.glob("*.csv"))
    return csvs[0] if csvs else None


# ---------- Data ----------

FEATURE_COLUMNS: List[str] = [
    "Time",
    *[f"V{i}" for i in range(1, 29)],
    "Amount",
]


def load_dataset(path: Optional[Path] = None) -> pd.DataFrame:
    if path is None:
        path = find_default_dataset()
    if path is None or not path.exists():
        raise FileNotFoundError("Could not locate processed dataset. Place a cleaned CSV under project/data/processed/.")
    df = pd.read_csv(path)
    if "Class" not in df.columns:
        raise ValueError("Dataset must include 'Class' column.")
    missing_feats = [c for c in FEATURE_COLUMNS if c not in df.columns]
    if missing_feats:
        raise ValueError(f"Dataset missing required feature columns: {missing_feats}")
    return df


# ---------- Model ----------

def build_pipeline() -> Pipeline:
    return Pipeline([
        ("scaler", StandardScaler()),
        ("logit", LogisticRegression(max_iter=1000, n_jobs=None, class_weight="balanced")),
    ])


@dataclass
class TrainResult:
    pipeline: Pipeline
    metrics: Dict[str, float]
    feature_columns: List[str]


def train_model(df: pd.DataFrame, random_state: int = 42) -> TrainResult:
    X = df[FEATURE_COLUMNS]
    y = df["Class"].astype(int)
    X_tr, X_te, y_tr, y_te = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=random_state
    )
    pipe = build_pipeline()
    pipe.fit(X_tr, y_tr)
    y_hat = pipe.predict(X_te)
    y_proba = pipe.predict_proba(X_te)[:, 1]
    metrics = {
        "pr_auc": float(average_precision_score(y_te, y_proba)),
        "f1": float(f1_score(y_te, y_hat)),
        "precision": float(precision_score(y_te, y_hat)),
        "recall": float(recall_score(y_te, y_hat)),
    }
    return TrainResult(pipeline=pipe, metrics=metrics, feature_columns=list(FEATURE_COLUMNS))


def save_model(model: Pipeline, path: Optional[Path] = None) -> Path:
    if path is None:
        path = get_default_model_path()
    payload = {
        "model": model,
        "feature_columns": FEATURE_COLUMNS,
    }
    joblib.dump(payload, path)
    return path


def load_model(path: Optional[Path] = None) -> Tuple[Pipeline, List[str]]:
    if path is None:
        path = get_default_model_path()
    if not path.exists():
        raise FileNotFoundError("Model artifact not found. Train and save a model first.")
    payload = joblib.load(path)
    return payload["model"], payload["feature_columns"]


# ---------- Prediction ----------

def _validate_row(row: Dict[str, float], feature_columns: List[str]) -> np.ndarray:
    missing = [c for c in feature_columns if c not in row]
    if missing:
        raise ValueError(f"Missing required features: {missing}")
    try:
        values = [float(row[c]) for c in feature_columns]
    except Exception as err:  # noqa: BLE001
        raise ValueError(f"Invalid types in input row: {err}")
    return np.array(values, dtype=float).reshape(1, -1)


def predict_proba(model: Pipeline, rows: List[Dict[str, float]], feature_columns: List[str]) -> List[float]:
    X = np.vstack([_validate_row(r, feature_columns) for r in rows])
    probs = model.predict_proba(X)[:, 1]
    return [float(p) for p in probs]


def predict_label(model: Pipeline, rows: List[Dict[str, float]], feature_columns: List[str], threshold: float = 0.5) -> List[int]:
    probs = predict_proba(model, rows, feature_columns)
    return [int(p >= threshold) for p in probs]


# ---------- One-shot helpers ----------

def train_and_save(default_data: Optional[Path] = None) -> Dict[str, str]:
    df = load_dataset(default_data)
    res = train_model(df)
    model_path = save_model(res.pipeline)
    return {
        "model_path": str(model_path),
        "pr_auc": f"{res.metrics['pr_auc']:.4f}",
        "f1": f"{res.metrics['f1']:.4f}",
        "precision": f"{res.metrics['precision']:.4f}",
        "recall": f"{res.metrics['recall']:.4f}",
    }


