# DC Roadway Attribution
This project contains a script to compute the surface area of roadway artifacts in order to conceptualize the breadth of space given to various vehicles.

## methodology

## source datasets
|dataset|description|file date|
|---|---|---|
|[Roadway Block](https://opendata.dc.gov/datasets/roadway-block)|Information about block by block roadway segments in DC|6/8/23|
|[Bicycle Lanes](https://opendata.dc.gov/datasets/bicycle-lanes)|Information about various kinds of bike lanes in DC|6/1/23|
|[Alleys and Parking](https://opendata.dc.gov/datasets/alleys-and-parking)|Information about alleyways and parking easements/lots in DC|6/8/23|

## usage
To run:
1. download the `GeoJSON`-formatted files for the above datasets, and place them in a `data` folder in the repo.
2. either use the included conda environment (requires Anaconda or [miniconda](https://docs.conda.io/en/latest/miniconda.html)) to pull package dependencies through an environment:

   ```shell
   conda env create
   conda activate dc-roadway-attribution
   ```

   or use `pip` (assumes python is already installed)

   ```shell
   pip install geopandas
   ```

3. run `compute.py`

   ```shell
   python comput.py
   ```
   
   or, within a Python terminal:

   ```python
    exec(open('compute.py').read())
    ```
