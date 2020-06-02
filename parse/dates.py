"""
This module contains functions to manage dates
"""

def get_year(year_string: str) -> int:
    """ Returns the year from the standard date string
    If the year is not mentioned, returns -100
    Args:
        year_string:
    Returns:
    Examples:
        >>> get_year('01/01/1880 12:00:00 AM')
        1880
    """
    ys = year_string.split(' ')[0].split('/')[-1]
    return -100 if ys =='' else int(ys)