"""
This module contains functions and variables for plots
"""
import numpy as np

scatter_dot_size = (20, 7000)  # min and max size of dots for scatter plot


def map_variable_to_dot_size(x: list, n_of_sizes: int = 1000) -> np.array:
    """ Returns the dot size associated with each x
    Minimum value of x will be mapped as min(scatter_dot_size)
    Maximum value of x will be mapped as max(scatter_dot_size)
    number of possible "levels" is defined by n_of_sizes
    Args:
        x: numerical values to map to dot-size
        n_of_sizes:
    Returns:
    Examples:
        >>> map_variable_to_dot_size([20, 40, 90])
        array([  20.        , 2014.28571429, 7000.        ])
    """
    x = np.array(x)
    x_to_map = np.linspace(np.min(x), np.max(x), n_of_sizes)
    y = np.linspace(*scatter_dot_size, len(x_to_map))
    c = np.polyfit(x_to_map, y, deg=1)
    return np.polyval(c, x)


# settings for scatter plots
scatter_args = {'alpha': .5,
                'edgecolors': 'k',
                'color': 'red',
                'marker': 'o'}

scatter_args_alt = {'alpha': .4,
                    'edgecolors': 'k',
                    'color': 'lightgreen',
                    'marker': 'o'}

# settings for category plots
catplot_args = {'palette': 'deep',
                'linewidth': 1,
                'alpha': .7,
                's': 5,
                }
