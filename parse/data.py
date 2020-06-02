"""
This module contains functions to load raw and clean data
"""

import pandas as pd
import numpy as np
import tqdm
import os

from utils import paths
from geo import geography as geof
from utils.common import numeric_fill, string_fill, country_order
from parse.dates import get_year


def _get_row_data(): return pd.read_csv(paths.raw_data_path)

def _clean_raw_data() -> pd.DataFrame:
    """ Loads the raw data and replaces missing values with the values specified in utils.common
    Returns:
        raw data with no missing values
    Examples:
        >>> _clean_raw_data().head(2).name.tolist()
        ['Aachen', 'Aarhus']
    """
    columns = ['name', 'id', 'nametype', 'recclass', 'mass (g)', 'fall', 'year', 'reclat', 'reclong', 'GeoLocation']
    raw_data = _get_row_data()
    non_numerical_columns = raw_data.select_dtypes([object]).columns
    numerical_columns = list(set(raw_data.columns) - set(non_numerical_columns))
    df_numerical_filled = raw_data[numerical_columns].fillna(numeric_fill)
    df_non_numerical_filled = raw_data[non_numerical_columns].fillna(string_fill)
    df_filled = pd.concat((df_numerical_filled, df_non_numerical_filled), axis=1).reindex(columns=columns)
    return df_filled


def _add_country_column(df: pd.DataFrame, write_csv=0) -> pd.DataFrame:
    """ Adds the column 'country' to the input dataframe `df` (must have and 'reclat' and 'reclong' columns)
    If the input dataframe has not the 'reclat' and 'reclong' columns, raises an error
    Args:
        df: dataframe with geographical data
        write_csv: if 1, writes data in a csv table (see default path in utils.paths)
    Returns:
        dataframe with the additional 'country' column
    """
    try:
        assert all(x in df.columns for x in ['reclat', 'reclong'])
    except AssertionError:
        print('Input dataframe has no information about latitude/longitude')
        raise

    with tqdm.tqdm(df.index) as pbar:
        for idx in df.index:
            country = geof.get_country_from_lat_long(*df.loc[idx, ['reclat', 'reclong']])
            df.loc[idx, 'country'] = country
            pbar.update(1)
    if write_csv:
        df.to_csv(paths.clean_data_path)
    return df


def _get_data() -> pd.DataFrame:
    """ Returns data in its final version.
    If the csv file exists, loads from it, otherwise, computes from the start
    Returns:
    Examples:
        >>> _get_data().country.head(2).tolist()
        ['Germany', 'Denmark']
    """
    if os.path.exists(paths.clean_data_path):
        df = pd.read_csv(paths.clean_data_path, index_col=0).rename(columns={'year': 'date'})
        df['year'] = df.date.apply(get_year)
        df['millenium'] = df.year.apply(lambda x: int(x / 1000) + 1)
        df['century'] = df.year.apply(lambda x: int(x / 100) + 1)
        df['mass'] = df['mass (g)'].replace(-1, 0) / 1000
        df['log_mass'] = df.mass.apply(lambda x: np.log10(x * 1000))
        df['country'] = df.country.str.replace("United States of America", "USA")
        df['country_alt'] = df.country.apply(lambda x: x if x in country_order else 'elsewhere')
        return df
    else:
        row_data = _clean_raw_data()
        _add_country_column(row_data, write_csv=1)
        return _get_data()


def get_fallen_meteorites() -> pd.DataFrame:
    """ Returns the meteorites flagged as 'Fell' and 'Valid", with a clear country
    Returns:

    """
    data = _get_data()
    fallen_meteorites = data[
        (data.fall == "Fell") & (data.country != 'no country') & (data.country != 'no coordinates') & (
                    data.nametype == "Valid")]
    return fallen_meteorites


def get_found_meteorites() -> pd.DataFrame:
    """ Returns the meteorites flagged as 'Found' and 'Valid", with a clear country
    Returns:

    """
    data = _get_data()
    found_meteorites = data[
        (data.fall == "Found") & (data.country != 'no country') & (data.country != 'no coordinates') & (
                    data.nametype == "Valid")]
    return found_meteorites