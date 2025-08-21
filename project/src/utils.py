import pandas as pd
import datetime as dt
import os, pathlib

RAW = pathlib.Path(os.getenv('DATA_DIR_RAW')); RAW.mkdir(parents=True, exist_ok=True)

def get_summary_stats(df):
    return df.describe()

def ts():
    return dt.datetime.now().strftime('%Y%m%d-%H%M%S')

def save_csv(df: pd.DataFrame, prefix: str, **meta):
    mid = '_'.join([f"{k}-{v}" for k,v in meta.items()])
    path = RAW / f"{prefix}_{mid}_{ts()}.csv"
    df.to_csv(path, index=False)
    print('Saved', path)
    return path

def validate(df: pd.DataFrame, required):
    missing = [c for c in required if c not in df.columns]
    return {'missing': missing, 'shape': df.shape, 'na_total': int(df.isna().sum().sum())}
