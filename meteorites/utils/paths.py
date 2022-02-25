"""
Paths of the components the project
"""
from pathlib import Path

import meteorites


# project_path = os.path.dirname(__file__) # path of the project
_module_path = Path(meteorites.__file__).parent
raw_data_path = str(_module_path / 'data' / 'Meteorite_landings.csv')
clean_data_path = str(_module_path / 'data' / 'meteors.csv')
