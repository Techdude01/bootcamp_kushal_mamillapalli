# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.2
#   kernelspec:
#     display_name: Python 3
#     language: python

#     name: python3
# ---

# %% [markdown]
# # Setup: Generate Sample Dataset
#
# This cell creates the required folder structure (`data/raw/` and `data/processed/`) relative to the notebook, and generates the sample CSV dataset with missing values.
# This ensures the dataset is ready for cleaning functions and saves it to `data/raw/sample_data.csv`.

# %%
import os
import pandas as pd
import numpy as np

# Define folder paths relative to this notebook
raw_dir = '../data/raw'
processed_dir = '../data/processed'

# Create folders if they don't exist
os.makedirs(raw_dir, exist_ok=True)
os.makedirs(processed_dir, exist_ok=True)

# Define the sample data
data = {
    'age': [34, 45, 29, 50, 38, np.nan, 41],
    'income': [55000, np.nan, 42000, 58000, np.nan, np.nan, 49000],
    'score': [0.82, 0.91, np.nan, 0.76, 0.88, 0.65, 0.79],
    'zipcode': ['90210', '10001', '60614', '94103', '73301', '12345', '94105'],
    'city': ['Beverly', 'New York', 'Chicago', 'SF', 'Austin', 'Unknown', 'San Francisco'],
    'extra_data': [np.nan, 42, np.nan, np.nan, np.nan, 5, np.nan]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV in raw data folder
csv_path = os.path.join(raw_dir, 'sample_data.csv')
if not os.path.exists(csv_path):
    df.to_csv(csv_path, index=False)
    print(f'Sample dataset created and saved to {csv_path}')
else:
    print(f'File already exists at {csv_path}. Skipping CSV creation to avoid overwrite.')


# %% [markdown]
# # Homework Starter — Stage 6: Data Preprocessing
# Use this notebook to apply your cleaning functions and save processed data.

# %%
import pandas as pd
from src import cleaning

# %% [markdown]
# ## Load Raw Dataset

# %%
df = pd.read_csv('../data/raw/sample_data.csv')
df.head()

# %% [markdown]
# ## Apply Cleaning Functions

# %%
# TODO: Apply your functions here
# Example:
df = cleaning.fill_missing_median(df, ['col1','col2'])
df = cleaning.drop_missing(df, threshold=0.5)
df = cleaning.normalize_data(df, ['col1','col2'])

# %% [markdown]
# ## Save Cleaned Dataset

# %%
df.to_csv('../data/processed/sample_data_cleaned.csv', index=False)
