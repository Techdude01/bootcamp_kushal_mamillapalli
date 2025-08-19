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
# # Homework Starter — Stage 6: Data Preprocessing
# Use this notebook to apply your cleaning functions and save processed data.

# %%
import pandas as pd
from ../../project/src import cleaning

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
# df = cleaning.fill_missing_median(df, ['col1','col2'])
# df = cleaning.drop_missing(df, threshold=0.5)
# df = cleaning.normalize_data(df, ['col1','col2'])

# %% [markdown]
# ## Save Cleaned Dataset

# %%
# df.to_csv('../data/processed/sample_data_cleaned.csv', index=False)
