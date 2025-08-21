import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def fill_missing_median(df, columns=None):
    """
    Fill missing numeric values in specified columns with the column median.

    Args:
        df (pandas.DataFrame): Input DataFrame.
        columns (list, optional): List of columns to fill. Defaults to all numeric columns.

    Returns:
        pandas.DataFrame: DataFrame with missing values filled.
    """
    df_copy = df.copy()
    if columns is None:
        columns = df.select_dtypes(include=np.number).columns
    for col in columns:
        df_copy[col] = df_copy[col].fillna(df_copy[col].median())
    return df_copy

def drop_missing(df, columns=None, threshold=None):
    """
    Drop rows with missing values based on columns or a missing value threshold.

    Args:
        df (pandas.DataFrame): Input DataFrame.
        columns (list, optional): Columns to check for missing values.
        threshold (float, optional): Minimum fraction of non-missing values required per row.

    Returns:
        pandas.DataFrame: DataFrame with rows dropped according to criteria.
    """
    df_copy = df.copy()
    if columns is not None:
        return df_copy.dropna(subset=columns)
    if threshold is not None:
        return df_copy.dropna(thresh=int(threshold*df_copy.shape[1]))
    return df_copy.dropna()

def normalize_data(df, columns=None, method='minmax'):
    """
    Normalize numeric columns using MinMax or Standard scaling.

    Args:
        df (pandas.DataFrame): Input DataFrame.
        columns (list, optional): Columns to normalize. Defaults to all numeric columns.
        method (str, optional): Scaling method, 'minmax' or 'standard'. Defaults to 'minmax'.

    Returns:
        pandas.DataFrame: DataFrame with normalized columns.
    """
    df_copy = df.copy()
    if columns is None:
        columns = df_copy.select_dtypes(include=np.number).columns
    if method=='minmax':
        scaler = MinMaxScaler()
    else:
        scaler = StandardScaler()
    df_copy[columns] = scaler.fit_transform(df_copy[columns])
    return df_copy

