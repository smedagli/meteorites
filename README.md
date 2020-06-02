# meteorites
Analysis of the Meteorite Landings db by NASA 

## prerequisites
create a conda environment using the file in `environment/pkg.txt`

```bash
conda create --name meteorites --file meteorites\environment\pkg.txt
```

## folder structure
```bash
|   meteorites.ipynb
|   __init__.py
|   
+---data
|       Meteorite_Landings.csv
|       meteors.csv
|       
+---environment
|       pkg.txt
|       
+---figures

|       
+---geo
|   |   geography.py
|   |   __init__.py
|   |   
|   \---world_map
|           ne_110m_admin_0_countries.cpg
|           ne_110m_admin_0_countries.dbf
|           ne_110m_admin_0_countries.prj
|           ne_110m_admin_0_countries.README.html
|           ne_110m_admin_0_countries.shp
|           ne_110m_admin_0_countries.shx
|           ne_110m_admin_0_countries.VERSION.txt
|           
+---graphic
|       parameters.py
|       __init__.py
|       
+---parse
|       data.py
|       dates.py
|       __init__.py
|       
\---utils
        common.py
        dataframe.py
        paths.py
        __init__.py
```

### components
#### parse
contains modules to parse data
* *data.py*: functions to load raw and clean data
* *dates.py*: functions to quick transform dates into standard format
#### geo
* *geograpy.py*: functions to deal with geographic data
#### utils
* *paths.py*: contains the paths of the components the project
* *dataframe.py*: a collection of quick functions for common operations of pandas' DataFrame
* *common.py*: contains common variables (useful to standardize formats)
