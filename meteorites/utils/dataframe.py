"""
A collection of quick functions for common operations of pandas' DataFrame
"""
import pandas as pd


def get_number_of_na(df: pd.DataFrame) -> pd.Series:
    """ Returns the number of nan for each column
    Args:
        df:
    Returns:
    """
    return df.isna().sum()


def get_year_stats(df: pd.DataFrame) -> pd.DataFrame:
    """ Returns nr of entries and sum of masses per each year.
    Args:
        df: dataframe with columns ['year', 'name', 'mass']
    Returns:
        dataframe with columns ['nr', 'mass']
    """
    yearly = df.groupby('year')
    out = pd.DataFrame()
    out['nr'] = yearly.count().name
    out['mass'] = yearly.sum()['mass']
    return out
