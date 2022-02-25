"""
Contains functions to deal with geographic data
"""
import geopandas as gpd
from geopy.geocoders import Nominatim


def get_country_from_lat_long(lat: float, long: float) -> str:
    """ Returns the country name from latitude and longitude
    if coordinates are not valid, returns 'no coordinates'
    if coordinates are -1, -1 (selected placeholder), returns 'no country'
    Args:
        lat: latitude coordinate
        long: longitude coordinate
    Returns:
        english name of the country
    Examples:
        >>> get_country_from_lat_long(20, 19)
        'Chad'
        >>> get_country_from_lat_long(1, 1)
        'no coordinates'
    """
    if lat == 0 and long == 0:
        return 'Null Island'
    if lat == -1 and long == -1:
        return 'no country'
    else:
        locator = Nominatim(user_agent="geoapiExercises")
        coordinates = f"{lat}, {long}"
        location = locator.reverse(coordinates, language='en')
        if list(location.raw.keys()) == ['error']:
            return 'no coordinates'
        else:
            return location.raw['address']['country']


def load_world_data(no_antarctica: bool = True) -> gpd.GeoDataFrame:
    """ Returns the geopandas dataframe of the world
    Args:
        no_antarctica: removes Antarctica (in order to get better-looking maps)
    Returns:
    """
    shapefile = 'geo/world_map/ne_110m_admin_0_countries.shp'
    gdf = gpd.read_file(shapefile)[['ADMIN', 'ADM0_A3', 'geometry']]
    gdf.rename(columns={"ADMIN": 'country', 'ADM0_A3': 'country_code'}, inplace=True)
    if no_antarctica:
        gdf.drop(gdf[gdf.country == 'Antarctica'].index, inplace=True)
    return gdf
